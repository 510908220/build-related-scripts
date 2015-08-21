#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import optparse
import time
import sys
import win32com.client
from ftplib import FTP

import config


SIGN_FTP = FTP()

OLD_FILELIST = []
NEW_FILELIST = []

HAVE_YEAR_MONTH_DIR = False
HAVE_DAY_DIR = False


def CheckSign(file_path):
	s = win32com.client.gencache.EnsureDispatch('capicom.signedcode', 0)
	s.FileName = file_path
	signer = s.Signer
	print (signer.Certificate.IssuerName, signer.Certificate.SerialNumber)


def _FtpLogin():
	SIGN_FTP.set_pasv(True)
	SIGN_FTP.connect(config.FTP_SERVER, config.FTP_PORT)
	SIGN_FTP.login(config.FTP_USERNAME, config.FTP_PASSWORD)
	SIGN_FTP.cwd(config.FTP_UPLOAD_DIR)
	print SIGN_FTP.getwelcome()


def _UploadFile(local_file, remote_file):
	print (local_file, remote_file)
	file_handler = open(local_file, 'rb')
	print SIGN_FTP.storbinary('STOR %s' % remote_file, file_handler, 64 * 1024)
	file_handler.close()


def _ExtractFilename(line):
	pos = line.rfind(':')
	while line[pos] != ' ':
		pos += 1
	while line[pos] == ' ':
		pos += 1
	return line[pos:]


def _AddFileNameToFileList(filelist, line):
	filename = _ExtractFilename(line)
	if filename not in ['.', '..']:
		filelist.append(filename)


def _AddFileNameToOldFileList(line):
	_AddFileNameToFileList(OLD_FILELIST, line)


def _ChangeToYearMonthPath():
	global HAVE_YEAR_MONTH_DIR
	if HAVE_YEAR_MONTH_DIR:
		return True
	try:
		SIGN_FTP.cwd(config.NOW_YEAR_MONTH)
		HAVE_YEAR_MONTH_DIR = True
	except:
		print '%s not exist' % config.NOW_YEAR_MONTH
	return HAVE_YEAR_MONTH_DIR


def _ChangeToDayPath():
	global HAVE_DAY_DIR
	if HAVE_DAY_DIR:
		return True
	try:
		SIGN_FTP.cwd(config.NOW_DAY)
		HAVE_DAY_DIR = True
	except:
		print '%s not exist' % config.NOW_DAY
	return HAVE_DAY_DIR


def _CollectOldFileList():
	if not _ChangeToYearMonthPath() or not _ChangeToDayPath():
		return False
	SIGN_FTP.dir(_AddFileNameToOldFileList)
	return True


def _AddFileNameToNewFileList(line):
	_AddFileNameToFileList(NEW_FILELIST, line)


def _DiffFileList():
	for file_item in NEW_FILELIST:
		print file_item
	if file_item not in OLD_FILELIST and file_item.find('\xe6\xb8\xb8\xe6\x99\xb6') != -1:
		file_handler = open(os.path.split(os.path.realpath(__file__))[0] + '\\' + file_item, 'wb')
		print SIGN_FTP.retrbinary('RETR %s' % file_item, file_handler.write)
		file_handler.close()
		return file_item
	return None


def _CollectNewFileList():
	sys.stdout.flush()
	try_count = 0
	while try_count <= 100:
		time.sleep(10)
		if _ChangeToYearMonthPath() and _ChangeToDayPath():
			SIGN_FTP.dir(_AddFileNameToNewFileList)
			res_file = _DiffFileList()
		if res_file:
			print 'sleep 10 * %ds, waiting digit sign ...' % try_count
			return res_file
		print '[waitsign]waitsign is not ok, wait next 10s\n'
		try_count += 1
		sys.stdout.flush()
	return None


def _SignOnWeb(sign_remote_dir):
	# sign_cmd = r'%SIKULI_HOME%\Sikuli-IDE.bat -r ' + os.path.split(os.path.realpath(__file__))[0] \
	# + '\\sign.sikuli --args "' + sign_remote_dir + '"'
	sign_cmd = "{sign} {param}".format(sign=os.path.join(os.path.dirname(__file__), "do_sign.py"),
	                                   param=sign_remote_dir)
	print sign_cmd
	os.system(sign_cmd)


def _UnPackageSignedRes(res_file, sign_src_dir):
	if res_file:
		sign_zip = os.path.split(os.path.realpath(__file__))[0] + '\\' + res_file
		_un7zcmd = config.TOOLS_DIR + '\\7zip\\7z.exe e ' + sign_zip + ' -o' + sign_src_dir + ' -y'
		print _un7zcmd
		os.system(_un7zcmd)
		os.remove(sign_zip)
	else:
		raise ValueError, 'sign step failed'


def BeginSign(sign_src_dir, sign_remote_dir, files):
	try_count = 0
	while try_count < 30:
		try:
			_BeginSign(sign_src_dir, sign_remote_dir, files)
			break
		except Exception, e:
			print "Exception:", e
			try:
				SIGN_FTP.quit()
			except Exception, e:
				SIGN_FTP.close()
				print 'SIGN_FTP.quit fail'
			print 'BeginSign %s fail, try again' % sign_remote_dir
			time.sleep(10)
			try_count += 1


def _BeginSign(sign_src_dir, sign_remote_dir, files):
	global OLD_FILELIST, NEW_FILELIST, HAVE_YEAR_MONTH_DIR, HAVE_DAY_DIR
	OLD_FILELIST = []
	NEW_FILELIST = []
	HAVE_YEAR_MONTH_DIR = False
	HAVE_DAY_DIR = False
	_FtpLogin()
	try:
		SIGN_FTP.cwd(sign_remote_dir)
	except:
		SIGN_FTP.mkd(sign_remote_dir)
		SIGN_FTP.cwd(sign_remote_dir)

	for file_item in files:
		_UploadFile(sign_src_dir + '\\' + file_item, file_item)
	SIGN_FTP.cwd('..\\..\\down')

	_CollectOldFileList()
	_SignOnWeb(sign_remote_dir)


def EndSign(sign_src_dir):
	_UnPackageSignedRes(_CollectNewFileList(), sign_src_dir)
	try:
		SIGN_FTP.quit()
	except:
		pass


def Sign(sign_src_dir, sign_remote_dir, files):
	BeginSign(sign_src_dir, sign_remote_dir, files)
	EndSign(sign_src_dir)


def _ParseArguments():
	"""Parse the sys.argv command-line arguments, returning the options."""

	parser = optparse.OptionParser()
	parser.add_option('--sign_src_dir', dest='sign_src_dir', type='str')
	parser.add_option('--sign_remote_dir', dest='sign_remote_dir', type='str')
	parser.add_option('--files', dest='files', type='str')
	(opts, args) = parser.parse_args()
	return opts


def Main():
	opts = _ParseArguments()
	print 'sign_src_dir:%s,sign_remote_dir:%s, files:%s\n' % (opts.sign_src_dir, opts.sign_remote_dir,
	                                                          opts.files)
	Sign(opts.sign_src_dir, opts.sign_remote_dir, opts.files)
	return 0


if __name__ == '__main__':
	sys.exit(Main())

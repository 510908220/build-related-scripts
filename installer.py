# -*- coding: utf-8 -*-
import os
import subprocess
import config
import util


def set_nis_info(nsi_path, version):
	"""
	设置安装包生成脚本的版本号
	:param nsi_path:
	:param version:
	:return:
	"""
	if not os.path.exists(nsi_path):
		raise (Exception, "nis not exists!")

	nsi_data = ""
	with open(nsi_path) as f:
		for line in f:
			if line.startswith("!define"):
				if line.find("FILE_VERSION") != -1:
					line = "!define FILE_VERSION '{version}'\n".format(version=version)
				elif line.find("FILE_INSTVERSION") != -1:
					line = "!define FILE_INSTVERSION '{version}'\n".format(version=version)
				elif line.find("PACKAGE_OUTPUT") != -1:
					line = "!define PACKAGE_OUTPUT '{out}'\n".format(out=config.PACKAGE_OUT)

				nsi_data += line
			else:
				nsi_data += line
	with open(nsi_path, "w") as f:
		f.write(nsi_data)


def make_installer(version):
	set_nis_info(config.NSI_SCRIPT, version)
	cmd = '{nsi_tool} /X"SetCompressor  /FINAL lzma" {nsi_script}'.format(nsi_tool=config.NSI_TOOL, nsi_script=config.NSI_SCRIPT)

	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while p.poll() == None:
		util.report( p.stdout.readline())


if __name__ == "__main__":
	util.report("Begin Installer.....")
	make_installer(util.get_new_version())
	util.report("End Installer.....")

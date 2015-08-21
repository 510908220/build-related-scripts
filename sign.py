# -*- coding: utf-8 -*-
import os
import shutil
import waitsign
import config
import util
import uninstaller
from optparse import OptionParser


def post_signature():
	sign_src_dir = os.path.join(config.PACKAGE_OUT, "bin")
	uninstall = os.path.join(sign_src_dir, config.UNINSTALL_NAME)
	new_uninstall = os.path.join(config.PACKAGE_OUT, u"魔幻英雄卸载.exe")
	shutil.copy(uninstall, new_uninstall)
	os.remove(uninstall)


def do_digital_signature():
	unsign_names = util.get_unsign_list(os.path.join(config.PACKAGE_OUT, "bin"))
	sign_remote_dir = util.get_new_version() + '_setup_files'
	sign_src_dir = os.path.join(config.PACKAGE_OUT, "bin")
	waitsign.Sign(sign_src_dir, sign_remote_dir, unsign_names)


def sign_files():
	util.report("Begin Signature Files.....")
	uninstaller.make_uninstaller(util.get_new_version())
	do_digital_signature()
	post_signature()
	util.report("End Signature Files.....")


def sign_setup():
	util.report("Begin Signature Setup.....")
	setup_name = "Strife-{version}-setup.exe".format(version=util.get_new_version())
	unsign_names = [setup_name]
	sign_remote_dir = util.get_new_version() + '_setup_final'
	sign_src_dir = config.PACKAGE_OUT
	waitsign.Sign(sign_src_dir, sign_remote_dir, unsign_names)
	util.report("End Signature Setup.....")


def main():
	parser = OptionParser()
	parser.add_option("-s", "--setup",
	                  action="store_true", dest="setup_flag", default=False,
	                  help="sign bin files or setup")

	(options, args) = parser.parse_args()

	if options.setup_flag:
		sign_setup()
	else:
		sign_files()


if __name__ == "__main__":
	main()

# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import util
import config


def _get_new_setup():
	setup_name = u"魔幻英雄-{version}-setup.exe".format(version=util.get_new_version())
	return os.path.join(config.PACKAGE_OUT, setup_name)


def _get_publish_dir():
	return os.path.join(config.UPDATE_GEN_DIR, "setup", util.get_new_version())


def publish_pdb(publish_dir):
	pdb_dir = os.path.join(config.STRIFE_DIR, "bin")
	pdb_files = [os.path.join(pdb_dir, file_name) for file_name in os.listdir(pdb_dir) if ".pdb" in file_name]
	publish_pdb_dir = os.path.join(publish_dir, "pdb")
	if not os.path.exists(publish_pdb_dir):
		os.makedirs(publish_pdb_dir)

	for pdb_file in pdb_files:
		dst_file = os.path.join(publish_pdb_dir, os.path.basename(pdb_file))
		shutil.copyfile(pdb_file, dst_file)


def publish_setup(publish_dir):
	src_setup = _get_new_setup()
	dst_setup = os.path.join(publish_dir, os.path.basename(src_setup))
	if os.path.exists(src_setup):
		shutil.copyfile(src_setup, dst_setup)
		os.remove(src_setup)
	else:
		raise Exception("can not fine new setup:%s" % os.path.basename(src_setup))

def PublishDataReportTools(publish_dir):
	data_report_output_dir = os.path.join(config.ROOT_DIR, "build/data_report")
	dest_dir = os.path.join(publish_dir, os.path.basename(data_report_output_dir))
	if os.path.exists(dest_dir):
		shutil.rmtree(dest_dir)
	
	shutil.copytree(data_report_output_dir, dest_dir)

def main():
	publish_dir = _get_publish_dir()
	if not os.path.exists(publish_dir):
		os.makedirs(publish_dir)

	publish_setup(publish_dir)
	publish_pdb(publish_dir)
	PublishDataReportTools(publish_dir)

if __name__ == "__main__":
	util.report("Begin Publish Installer...")
	main()
	util.report("End Publish Installer...")

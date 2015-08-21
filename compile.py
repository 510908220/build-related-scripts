#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import optparse
import sys
import genversion
import config
import buildsln
import util
import subprocess

def _build_slns(opts):
	for mt_target in config.BUILD_MT_TARGETS:
		sln = os.path.join(config.PROJECT_DIR, mt_target)
		for project in config.BUILD_MT_TARGETS[mt_target]:
			buildsln.build_sln(opts.rebuild, sln, "Release MT", project)

	for md_target in config.BUILD_MD_TARGETS:
		sln = os.path.join(config.PROJECT_DIR, md_target)
		for project in config.BUILD_MD_TARGETS[md_target]:
			buildsln.build_sln(opts.rebuild, sln, "Release", project)


def _parse_arguments():
	"""Parse the sys.argv command-line arguments, returning the options."""

	parser = optparse.OptionParser()
	parser.add_option('--svn_revision', dest='revision', type='int', default=0)
	parser.add_option('--rebuild', action='store_true', dest='rebuild', default=False)
	(opts, args) = parser.parse_args()
	return opts
	
def CompileGoProject(package_main):
	old_cwd = os.path.abspath(os.getcwd())
	try:
		output_dir = os.path.join(config.ROOT_DIR, "build/data_report")
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		os.chdir(output_dir)
		
		cmd = ['go', 'build', package_main]
		ret_code = subprocess.check_call(cmd)
		if ret_code != 0:
			raise Exception('compile go project[%s] failed.' % package_main)
	finally:
		os.chdir(old_cwd)
	
def CompileDataReport():
	if 'GOPATH' not in os.environ:
		os.environ['GOPATH'] = ''
	os.environ['GOPATH'] = os.path.normpath(os.path.join(config.ROOT_DIR, "src/tools/data_report/msg_code_generator")) + \
		";" + os.environ['GOPATH']
		
	data_report_projects = [
		os.path.join(config.ROOT_DIR, "src/tools/data_report/msg_to_disk/src/msg_to_disk.go"),
		os.path.join(config.ROOT_DIR, "src/tools/data_report/msg_to_mysql/src/msg_to_mysql.go")
	]
	for project in data_report_projects:
		CompileGoProject(project)
	
def main():
	opts = _parse_arguments()
	genversion.gen_version(opts)
	sys.stdout.flush()
	CompileDataReport()
	_build_slns(opts)

if __name__ == '__main__':
	util.report("Begin Compile.....")
	sys.exit(main())
	util.report("End Compile.....")

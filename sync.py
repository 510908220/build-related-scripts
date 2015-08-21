# -*- coding: utf-8 -*-
"""
文件同步:
1. 使用微软的SyncToy将变化的文件同步到svn目录下
2. svn提交变化的文件
"""

import subprocess
import config
import util
import os


def sync_local(pair_name):
	cmd = '''{tool} -R "{pair_name}"'''.format(tool=config.SYNC_TOOL, pair_name=pair_name)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while p.poll() == None:
		util.report(p.stdout.readline())


def write_version(version):
	version_file = os.path.join(config.SYNC_SVN_DIR, "version.txt")
	if not os.path.exists(config.SYNC_SVN_DIR):
		os.makedirs(config.SYNC_SVN_DIR)
	with open(version_file, "w") as f:
		f.write(version)


def commit_files():
	old_dir = os.getcwd()
	resource_dir = config.SYNC_SVN_DIR
	os.chdir(resource_dir)
	add_cmd = "svn add * --force"

	p = subprocess.Popen(add_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while p.poll() == None:
		util.report(p.stdout.readline())

	commit_cmd = '''svn commit -m "strife update files sync"'''

	p = subprocess.Popen(commit_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print commit_cmd
	while p.poll() == None:
		util.report(p.stdout.readline())
	os.chdir(old_dir)


if __name__ == "__main__":
	util.report("Begin sync files")
	sync_local("strife update")
	write_version(util.get_new_version())
	commit_files()
	util.report("End sync files")

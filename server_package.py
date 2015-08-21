# -*- coding: utf-8 -*-
"""
服务端资源打包（server_windows）
1. 服务端默认版本是0.0.0.0， 故新版本号为0.0.1.0
2. 打包完后svn进行提交
"""
import os
import subprocess
import util
import config


def do_package():
	def get_commands():

		login_cmd = "Login hzz@yy.com 123456"
		load_spec_cmd = "LoadSpec {spec}".format(spec=config.RELEASE_SPEC)
		build_update_cmd = "BuildUpdate server_windows {newVersion} {oldVersion} ".format(
			newVersion=config.VER_INCREMENT_LOCATION, oldVersion=util.get_local_version())

		package_out = os.path.join(config.ROOT_DIR, "StrifeServer").replace("\\", "/")
		gen_dir = os.path.join(config.ROOT_DIR, "tmp/update_server").replace("\\", "/")

		set_var = "set updategen_distDir %s" % gen_dir
		manifest = os.path.join(gen_dir, "manifests/strife-cn_prod-server-windows-x86",
		                        util.get_new_version() + ".xml").replace("\\", "/")

		build_install_cmd = "BuildInstall {manifest} {package_out}".format(manifest=manifest,
		                                                                   package_out=package_out)
		quit_cmd = "quit"
		cmds = ";".join(
			[set_var, login_cmd, load_spec_cmd, build_update_cmd, build_install_cmd,quit_cmd])
		return cmds

	util.clear_package_log()
	util.update_cvar()
	util.update_host()

	old_cwd = os.getcwd()
	os.chdir(config.STRIFE_DIR)
	cmd = '{update_generator} -autoexec "{cmds}"'.format(update_generator=config.UPDATE_GENERATOR, cmds=get_commands())
	print cmd
	os.system(cmd)
	os.chdir(old_cwd)


def commit_resource():
	old_dir = os.getcwd()
	resource_dir = os.path.abspath(os.path.join(config.ROOT_DIR, "StrifeServer"))
	os.chdir(resource_dir)
	print os.getcwd()
	cmd = '''svn commit -m "server resource"'''
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while p.poll() == None:
		util.report(p.stdout.readline())
	os.chdir(old_dir)


if __name__ == "__main__":
	util.report("Begin Server Package.....")
	do_package()
	commit_resource()
	util.report("End Server Package.....")

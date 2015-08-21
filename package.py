# -*- coding: utf-8 -*-
import config
import os
import subprocess
import util
import shutil


def generated_files():
	"""
	作用:将可以缓存的游戏资源缓存下来，真正游戏打包时用的是缓存文件
	日志文件:D:\strife\Strife\generateresources.txt
	"""
	cmd = '{strife} -generateresources 0'.format(strife=config.STRIFE_EXE)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()

	cmd = '{strife} -generateresources 1'.format(strife=config.STRIFE_EXE)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()

	cmd = '{strife} -generateresources 2'.format(strife=config.STRIFE_EXE)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()

	cmd = '{strife} -generateresources 3'.format(strife=config.STRIFE_EXE)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()

	cmd = '{strife} -generateresources 4'.format(strife=config.STRIFE_EXE)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()

	cmd = '{strife} -generateresources 5'.format(strife=config.STRIFE_EXE)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()

def copy_nsi():
	nsi_names = ["uninstaller.nsi", "installer.nsi"]
	for nsi_name in nsi_names:
		src_file = os.path.join(config.SCRIPT_DIR, nsi_name)
		shutil.copy(src_file, config.PACKAGE_OUT)


def do_package():
	def get_commands():
		login_cmd = "Login hzz@yy.com 123456"
		load_spec_cmd = "LoadSpec {spec}".format(spec=config.RELEASE_SPEC)
		build_update_cmd = "BuildUpdate windows {newVersion} {oldVersion} ".format(newVersion = config.VER_INCREMENT_LOCATION, oldVersion = util.get_local_version())
		pending_request_cmd = "ProcessPendingRequests"
		# set_live_cmd = "SetManifestLive windows"
		build_install_cmd = "BuildInstall {manifest} {package_out}".format(manifest=util.get_new_manifest(),
		                                                                   package_out=config.PACKAGE_OUT)
		quit_cmd = "quit"
		cmds = ";".join(
			[login_cmd, load_spec_cmd, build_update_cmd, pending_request_cmd, build_install_cmd, quit_cmd])
		return cmds

	util.clear_package_log()
	util.update_cvar()
	util.update_host()

	old_cwd = os.getcwd()
	os.chdir(config.STRIFE_DIR)
	cmd = '{update_generator} -autoexec "{cmds}"'.format(update_generator=config.UPDATE_GENERATOR, cmds=get_commands())

	os.system(cmd)
	os.chdir(old_cwd)

if __name__ == "__main__":
	util.report("Begin Package[generated_files].....")
	generated_files()
	util.report("Begin Package[do_package].....")
	do_package()
	copy_nsi()
	util.report("End Package.....")



# -*- coding: utf-8 -*-
import os

from win32com.shell import shellcon, shell
import config
import subprocess
import time


def report(message):
	print "Message:", message


def update_local_version():
	last_version = ""
	if os.path.exists(config.PACKAGE_NEW_VERSION):
		with open(config.PACKAGE_NEW_VERSION) as f:
			last_version = f.read()
	else:
		last_version = "0.0.0.0"

	with open(config.PACKAGE_VERSION, "w") as f:
		f.write(last_version)


def get_local_version():
	if not os.path.exists(config.PACKAGE_VERSION):
		with open(config.PACKAGE_VERSION, "w") as f:
			f.write("0.0.0.0")

	with open(config.PACKAGE_VERSION) as f:
		version = f.read()
	return version


def get_new_version():
	current_version = get_local_version()
	vers = current_version.split(".")
	inc_pos = config.VER_INCREMENT_RULE[config.VER_INCREMENT_LOCATION]
	vers[inc_pos] = str(int(vers[inc_pos]) + 1)
	new_version = ".".join(vers)
	with open(config.PACKAGE_NEW_VERSION, "w") as f:
		f.write(new_version)
	return new_version


def get_new_manifest():
	gen_dir = config.UPDATE_GEN_DIR
	gen_dir = gen_dir.replace("\\\\", "\\")
	manifests_dir = os.path.join(gen_dir, "manifests", "strife-cn_prod-client-windows-x86")
	manifest_file = os.path.join(manifests_dir, get_new_version() + ".xml")
	manifest_file = manifest_file.replace("\\", "\\\\")
	return manifest_file


def update_host():
	host_file = r"C:\Windows\System32\drivers\etc\HOSTS"
	if os.path.exists(host_file):
		host_data = ""
		with open(host_file, "r") as f:
			host_data = f.read()

		if config.S2GI_DOMAIN not in host_data or config.CHAT_DOMAIN not in host_data:
			with open(host_file, "w") as f:
				host_data += "\n"
				if config.S2GI_DOMAIN not in host_data:
					host_data += config.S2GI_IP + " " + config.S2GI_DOMAIN + "\n"
				if config.CHAT_DOMAIN not in host_data:
					host_data += config.CHAT_IP + " " + config.CHAT_DOMAIN + "\n"
				f.write(host_data)
	else:
		raise Exception("no host...")


def update_cvar():
	"""
	更新打包程序使用的环境变量
	:return:
	"""

	def get_update_generator_config():
		document_dir = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, 0, 0)
		config_path = os.path.join(document_dir, "S2 Games", "Update Generator", "config.gcl")
		return config_path

	config_path = get_update_generator_config()
	if os.path.exists(config_path):
		os.remove(config_path)

	config_data = {
		"updategen_masterServerAddress": config.S2GI_IP,
		"updategen_distDir": config.UPDATE_GEN_DIR,
		"package_log_file": config.PACKAGE_LOG,
		"new_version_file": config.PACKAGE_VERSION
	}

	dir_path = os.path.dirname(config_path)
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

	with open(config_path, "w") as f:
		data = ""
		for config_key in config_data:
			config_item = 'Set "{name}" "{value}"'.format(name=config_key, value=config_data[config_key])
			data += (config_item + "\n")
		f.write(data)


def get_unsign_list(bin_dir):
	"""
	:param bin_dir:
	:return:未签名的文件列表
	"""
	sigcheck = os.path.join(config.TOOLS_DIR, "sigcheck.exe")
	output = os.path.join(config.SCRIPT_DIR, "sigcheck.txt")
	cmd = """{check_tool} -s -q -e -u "{dir}" > {output}""".format(check_tool=sigcheck, dir=bin_dir, output=output)
	os.system(cmd)

	unsign_names = []
	with open(output) as f:
		for line in f:
			if line.strip().endswith(":"):
				unsign_names.append(os.path.basename(line.strip())[0:-1])
	return unsign_names


def clear_package_version():
	if os.path.exists(config.PACKAGE_VERSION):
		os.remove(config.PACKAGE_VERSION)


def clear_package_log():
	if os.path.exists(config.PACKAGE_LOG):
		os.remove(config.PACKAGE_LOG)

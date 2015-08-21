#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import time
import email_util

def get_profile_path():
	firfox_profile_dir = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles"
	file_names = os.listdir(firfox_profile_dir)

	profile_name = None
	for file_name in file_names:
		if len(file_name.split(".")) == 2 and file_name.split(".")[1] == "default":
			profile_name = file_name

	if profile_name:
		profile_name = os.path.join(firfox_profile_dir, profile_name)

	return profile_name



def error_email(version):
	mailto_list=["youjing@yy.com","huzhongzhong@yy.com"]
	em = email_util.EmailManage()
	error_info = "sign  error:%s" % version
	flag = em.send( "数字签名失败".decode("utf-8"), error_info, mailto_list)

def login_repair(driver):
	pass

def is_login(driver):
	try:
		user = driver.find_element_by_css_selector('a[href="/jenkins/user/youjing"]')
		return True
	except:
		return False

def sign_imp(profile_path, version):
	ret = False

	fp = webdriver.FirefoxProfile(profile_path)

	driver = webdriver.Firefox(fp)
	driver.get("https://ci.yypm.com/jenkins/job/remote_digitalsign/build")

	#检验是否已经登录,如果登录过期，则尝试修复
	if not is_login(driver):
		login_repair(driver)

	elems = driver.find_elements_by_class_name("setting-input   ")

	time.sleep(5)

	if len(elems) == 2:
		elems[0].send_keys(version)
		print "Send version:",version
		try_times = 5
		while elems[0].get_attribute("value") != version and try_times > 0:
			print "Send version:%s,again!" % version
			elems[0].send_keys(version)
			time.sleep(5)

		elems[1].send_keys("sign by youjing")
		print "Send signer:","sign by youjing"
		try_times = 10
		while elems[1].get_attribute("value") != "sign by youjing" and try_times > 0:
			print "Send signer:%s,again!" % "sign by youjing"
			elems[1].send_keys("sign by youjing")
			time.sleep(5)

		build = driver.find_element_by_id(r"yui-gen1-button")
		build.click()
		time.sleep(5)
		ret = True

	driver.close()
	driver.quit()

	return ret


def sign(profile_path, version):
	ret = sign_imp(profile_path, version)
	print "sign_imp_return:",ret
	return ret

if __name__ == '__main__':
	version = sys.argv[1]
	profile_path = get_profile_path()
	print "profile_path:", profile_path
	if not profile_path:
		error_info = "sign error:%s,%s not exists" % (version, profile_path)
		print error_info
		error_email(error_info)
	else:
		ret = sign(profile_path, version)
		if not ret:
			error_info = "sign error:%s" % version
			print error_info
			error_email(error_info)
		else:
			print "sign success!!!"


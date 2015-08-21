#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os

import util
import config


def get_file_version(svn_revision):
	"""
	获取文件版本信息
	:param svn_revision:
	:return:
	"""
	now_time = time.localtime()
	year = '%04d' % now_time.tm_year
	month = '%02d' % now_time.tm_mon
	day = '%02d' % now_time.tm_mday
	file_version = ",".join([year, month, day, str(svn_revision)])
	return file_version


def update_k2_version(svn_revision):
	"""
	将文件版本信息和产品版本信息写入k2_version.h,后续构建会将此信息编入pe文件版本信息内
	:param svn_revision:
	:return:
	"""
	def write_k2_version(k2_version_file, version_info):
		with open(k2_version_file, "w") as f:
			f.write(version_info)

	version_info = "#ifndef K2_VERSION_H_\n"
	version_info += "#define K2_VERSION_H_\n"

	file_version=get_file_version(svn_revision)
	str_file_version = file_version.replace(",", ".")
	str_product_version = util.get_new_version()
	util.report("New Version Is:%s" % str_product_version)
	product_version = str_product_version.replace(".", ",")

	version_info += '#define FILE_VERSION  {file_version}\n'.format(file_version=file_version)
	version_info += '#define STR_FILE_VERSION  "{str_file_version}"\n'.format(str_file_version=str_file_version)
	version_info += '#define PRODUCT_VERSION  {product_version}\n'.format(product_version=product_version)
	version_info += '#define STR_PRODUCT_VERSION  "{str_product_version}"\n'.format(str_product_version=str_product_version)

	version_info += '#define COMPANY_NAME  "{company_name}"\n'.format(company_name="S2 Games")
	version_info += '#define LEGAL_COPY_RIGTE  "{legal_copy_write}"\n'.format(
		legal_copy_write="Copyright (C) 2013 S2 Games")
	version_info += '#define PRODUCT_NAME  "{product_name}"\n'.format(product_name="Strife")
	version_info += "#endif  //! #ifndef K2_VERSION_H_\n"

	k2_version_file = os.path.join(config.SRC_DIR, "k2", "k2_version.h")
	write_k2_version(k2_version_file, version_info)


def gen_version(opts):
	update_k2_version(opts.revision)


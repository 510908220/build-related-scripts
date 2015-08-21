#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import time

SCRIPT_DIR = os.path.split(os.path.abspath(sys.argv[0]))[0]
ROOT_DIR = os.path.join(SCRIPT_DIR, '..')
SRC_DIR = os.path.join(ROOT_DIR, 'src')
PROJECT_DIR = os.path.join(SRC_DIR, 'projects', "vs2013")
STRIFE_DIR = os.path.join(ROOT_DIR, 'strife')
PACKAGE_DIR = os.path.join(ROOT_DIR, 'package')
TOOLS_DIR = os.path.join(SCRIPT_DIR, 'tools')

# 打包与安装包
STRIFE_EXE = os.path.join(STRIFE_DIR, "bin", "strife.exe")
UPDATE_GENERATOR = os.path.join(STRIFE_DIR, "bin", "update_generator.exe")
RELEASE_SPEC = os.path.join(SCRIPT_DIR, "release.spec")
RELEASE_SPEC = RELEASE_SPEC.replace("\\", "\\\\")
UPDATE_GEN_DIR = r"g:\gen".replace("\\", "\\\\")
PACKAGE_OUT = r"g:\strife".replace("\\", "\\\\")
PACKAGE_LOG = os.path.join(SCRIPT_DIR, "package.log").replace("\\", "\\\\")
PACKAGE_VERSION = os.path.join(SCRIPT_DIR, "package.version").replace("\\", "\\\\")
PACKAGE_NEW_VERSION = os.path.join(SCRIPT_DIR, "package_new.version").replace("\\", "\\\\")
NSI_SCRIPT = os.path.join(PACKAGE_OUT, "installer.nsi")
NSI_SCRIPT_UNINSTALL = os.path.join(PACKAGE_OUT, "uninstaller.nsi")
NSI_TOOL = os.path.join(TOOLS_DIR, "nsi", "makensis.exe")

UNINSTALL_NAME = "uninstall.exe"
# 同步文件
SYNC_SVN_DIR = r"G:\for_uplive_sync\sync\gen"
SYNC_TOOL = os.path.join(TOOLS_DIR, "SyncToy", "SyncToyCmd.exe")

# 待编译的工程
BUILD_MD_TARGETS = {"Strife.sln": ["strife"]
                    }

BUILD_MT_TARGETS = {"launcher.sln": ["launcher"]
                    }


# s2gi和chat
S2GI_DOMAIN = "cn.s2ogi.strife.com"
CHAT_DOMAIN = "cn.chat.strife.com"
S2GI_IP = "125.90.93.210"
CHAT_IP = "125.90.93.210"


# 签名ftp://sign.yypm.com/down/201402/13/
FTP_SERVER = '172.19.108.44'
FTP_PORT = 21
FTP_USERNAME = 'signer'
FTP_PASSWORD = '0gPDB8XB'
FTP_UPLOAD_DIR = 'file'

# 当前时间
NOW_TIME = time.localtime()
NOW_YEAR = '%04d' % NOW_TIME.tm_year
NOW_YEAR_MONTH = '%04d%02d' % (NOW_TIME.tm_year, NOW_TIME.tm_mon)
NOW_MONTH = '%02d' % NOW_TIME.tm_mon
NOW_DAY = '%02d' % NOW_TIME.tm_mday

# 版本号递增位
VER_INCREMENT_LOCATION = "incrementhotfix"
VER_INCREMENT_RULE = {
	"incrementmajor": 0,
	"incrementminor": 1,
	"incrementmicro": 2,
	"incrementhotfix": 3

}

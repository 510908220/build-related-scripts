import shutil
import os
import util
import config

util.clear_package_log()
util.update_local_version()
if os.path.exists(config.PACKAGE_OUT):
	shutil.rmtree(config.PACKAGE_OUT)

sigcheck_result = os.path.join(config.SCRIPT_DIR, "sigcheck.txt")
if os.path.exists(sigcheck_result):
	os.remove(sigcheck_result)


import requests
from bs4 import BeautifulSoup
import time
import util

server_jenkins_build_url = r"http://125.90.93.210:8080/jenkins/job/client_version_update/build?token=bef5017211218f6c780d530cde055c33"
server_jenkins_job_url = r"http://125.90.93.210:8080/jenkins/job/client_version_update/"


def do_build():
	r = requests.get(server_jenkins_build_url)
	if str(r.status_code).startswith("2"):
		return True


def get_build_num():
	r = requests.get(server_jenkins_job_url)
	html = r.text
	soup = BeautifulSoup(html)
	build_history_table = soup.find(id="buildHistory")
	build_row_tr = build_history_table.find_all("tr", class_="build-row no-wrap ")[0]
	build_num = build_row_tr.get_text().split("\n")[1]
	return int(build_num.replace("#", ""))


def get_log_url(build_num):
	return "http://125.90.93.210:8080/jenkins/job/client_version_update/%d/console" % build_num


def get_log(build_num):
	log_url = get_log_url(build_num)
	r = requests.get(log_url)
	html = r.text
	soup = BeautifulSoup(html)
	consol_pre = soup.find("pre", class_="console-output")
	return consol_pre.get_text()


def get_log_state(log):
	if "Finished: SUCCESS" in log:
		return 1
	elif "Finished: FAILURE" in log:
		return 0
	else:
		return -1


def main():
	old_build_num = get_build_num()
	new_build_num = old_build_num + 1

	util.report("last build num is %d" % old_build_num)
	rv = do_build()
	if not rv:
		raise Exception("do_build() failed")

	times = 20
	while times > 0:
		build_num = get_build_num()
		if build_num != new_build_num:
			time.sleep(5)
			times -= 1
		else:
			break
	if times == 0:
		raise Exception("can not find new build num: %d" % new_build_num)

	while 1:
		log = get_log(new_build_num).encode("gbk")
		state = get_log_state(log)
		util.report(log)
		if state == 1:
			break
		elif state == 0:
			raise Exception(" Server Build Failed")
			break


if __name__ == "__main__":
	util.report("Server Build Begin...")
	main()
	util.report("Server Build End...")

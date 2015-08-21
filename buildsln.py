#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import sys
import subprocess
import config
from win32pipe import PeekNamedPipe
from msvcrt import get_osfhandle
from util import report


def _get_devenv():
	devenv = os.path.join(os.environ.get('VS120COMNTOOLS'), r'..\IDE\devenv.com')
	if not os.path.exists(devenv):
		raise ValueError, '[_GetMSBuild]not exist %s' % devenv
	return os.path.abspath(devenv)


def build_sln(rebuild, sln, build_type, project):
	report("Build:" +  project)
	out = os.path.join(config.PROJECT_DIR, project + '.log')
	if os.path.exists(out):
		os.remove(out)
	devenv = _get_devenv()
	sln = os.path.abspath(sln)
	if rebuild:
		cmd = '{devenv} {sln} /rebuild "{build_type}" /project {project} /out {out}' \
			.format(devenv=devenv, sln=sln, build_type=build_type, project=project, out=out)
	else:
		cmd = '{devenv} {sln} /build "{build_type}" /project {project} /out {out}' \
			.format(devenv=devenv, sln=sln, build_type=build_type, project=project, out=out)

	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	sys.stdout.flush()
	while True:
		if p.poll() != None:
			break
		line = non_block_read_line(p.stdout)
		line = line.strip()
		if line:
			print(line)
			sys.stdout.flush()
		line = non_block_read_line(p.stderr)
		line = line.strip()
		if line:
			print(line)
			sys.stdout.flush()
		time.sleep(0.1)
	out, err = p.communicate()
	for line in out.splitlines():
		line = line.strip()
		if line:
			print(line)
	for line in err.splitlines():
		line = line.strip()
		if line:
			print(line)

	if p.returncode != 0:
		raise ValueError, 'BuildSlnEx return failed'
	sys.stdout.flush()


def non_block_read_line(obj):
	try:
		handle = get_osfhandle(obj.fileno())
		(read, nAvail, nMessage) = PeekNamedPipe(handle, 0)
		if nAvail > 0:
			return obj.readline()
	except:
		pass
	return ""

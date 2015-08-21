# encoding:utf-8
import chardet
import sys
from pathlib import Path

print sys.getdefaultencoding()
print sys.stdout.encoding
s = "你"
print s.decode("utf-8")
print chardet.detect(s)

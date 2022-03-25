# -*-coding:utf8;-*-
import os
import sys
"""
QPy CMD extension
name: tar
description: tar program with python tarfile module.
version: v0.1
author: guangrei
require: ""
"""
argv = sys.argv # argv
path = os.environ["EXT_DIR"] # your extension path
if __name__ == "__main__":
	del argv[0]
	py = sys.executable
	com = "{0} -m tarfile {1}".format(py,' '.join(argv))
	os.system(com)

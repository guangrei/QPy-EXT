# -*-coding:utf8;-*-
import os
import sys
"""
QPy CMD extension
name: zip
description: zip program with python zipfile module.
version: v0.1
author: guangrei
require: ""
"""
argv = sys.argv # argv
path = os.environ["EXT_DIR"] # your extension path
if __name__ == "__main__":
	del argv[0]
	py = sys.executable
	com = "{0} -m zipfile {1}".format(py,' '.join(argv))
	os.system(com)

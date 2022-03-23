# -*-coding:utf8;-*-
import os
import sys
"""
QPy CMD extension
name: sl4a-installer
description: Sl4a module installer.
version: v0.1
author: guangrei
require: ""
"""
argv = sys.argv  # argv
path = os.environ["EXT_DIR"]  # your extension path
if __name__ == "__main__":

print("installing sl4a module..")
py = sys.executable
com = "{0} {1} install".format(py, path+"/setup.py")
os.system(com)
print("done!")

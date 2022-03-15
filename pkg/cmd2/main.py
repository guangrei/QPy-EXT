# -*-coding:utf8;-*-
import os
import sys
"""
QPy CMD extension
name: cmd2
description: native terminal launcher
version: v1.0
author: guangrei
require: ""
"""

print("###\nWelcome to second Qpy CMD, this is just native terminal! type \"exit\" for back to QPy CMD.\npython bin: " +sys.executable.split("/")[-1] + "\n###")
os.system("sh")

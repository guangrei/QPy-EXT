# -*-coding:utf8;-*-
import os
import sys
from pprint import pprint
"""
QPy CMD extension
name: test
description: test extension.
version: v1.0
author: guangrei
require: ""
"""
argv = sys.argv
del argv[0]
print("this is test extension!")
if len(argv) > 0:
    print("you have args: ", len(argv))
    print("your args:")
    pprint(argv)
else:
    print("you have args: ", len(argv))
print("your extension path: "+os.environ["EXT_DIR"])

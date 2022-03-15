# -*-coding:utf8;-*-
from urllib import parse
try:
    import androidhelper as sl4a
except ImportError:
    import android as sl4a
import sys

"""
QPy CMD extension
name: urldecode
description: decode url and copy its result to clipboard.
version: v1.0
author: guangrei
require: ""
"""
argv = sys.argv
droid = sl4a.Android()
try:
    res = parse.unquote(argv[1])
    s = droid.setClipboard(res)
    if s.error == None:
        droid.makeToast("copied!")
    else:
        droid.makeToast("copy failed!")
    print("[<]: " + res)
except IndexError:
    print("Usage: urldecode <string>")

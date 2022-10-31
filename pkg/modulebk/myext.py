# -*-coding:utf8;-*-
import os
import sys
import importlib

argv = sys.argv # argv
path = os.environ["EXT_DIR"] # your extension path

def main():
	if len(argv) == 2:
		mod = importlib.import_module(argv[1])
		mn = mod.__file__
		mp = os.path.basename(mn)
		if mp == "__init__.py":
			import shutil
			mp = os.path.dirname(mn)
			shutil.make_archive(argv[1], 'zip', mp)
			print("success backup %s"%argv[1])
		else:
			import zipfile
			zipfile.ZipFile(argv[1]+'.zip', mode='w').write(mn, mp)
			print("success backup %s"%argv[1])
	else:
		print("Usage: modulebk <module name>")
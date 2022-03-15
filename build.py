import re
import os
import sys
import json
from pprint import pprint
import time
from os import listdir
from os.path import isfile, isdir, join


def list_files(mypath):
    ret = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return ret


def list_dir(mypath):
    ret = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    return ret


readme = """Extension for QPy CMD v2.0 and up!\n
"""
readme_add = """
### {no}.{ext_name}

***name:*** {name}

***author:*** {author}

***description:*** {description}

***version:*** {version}\n
"""
readme_end = """
> If you want add your own extension, just fork this repository and add your extension to directory pkg then make pull request."""
ext = {}
ext["META"] = {}
ext["META"]["prefix"] = "https://raw.githubusercontent.com/guangrei/Qpy-EXT/main/pkg/"
ext["META"]["udated"] = time.strftime("%Y-%m-%d %H:%M:%S")
doc = re.compile('"""(.*?)"""', re.S)
description = re.compile('description:(.*?)\n', re.S)
nama = re.compile('name:(.*?)\n', re.S)
author = re.compile('author:(.*?)\n', re.S)
version = re.compile('version:(.*?)\n', re.S)
require = re.compile('require: "(.*?)"', re.S)
path = "./pkg/"
list = list_dir(path)
for i in list:
    print("processing ", i)
    with open(path+i+"/main.py", "r") as f:
        text = f.read()
        fi = doc.findall(text)[0]
        ext[i] = {}
        requires = require.search(fi).group(1)
        requires = requires.strip()
        if requires != "":
            requires = requires.split(",")
        else:
            requires = []
        ext[i]["name"] = nama.search(fi).group(1).strip()
        ext[i]["author"] = author.search(fi).group(1).strip()
        ext[i]["description"] = description.search(fi).group(1).strip()
        ext[i]["version"] = version.search(fi).group(1).strip()
        ext[i]["require"] = requires
        ext[i]["files"] = list_files(path+i)
        with open(path+i+"/.version", "w") as f2:
            f2.write(version.search(fi).group(1).strip())

js = json.dumps(ext, indent=4, sort_keys=True)
with open("meta.json", "w") as f3:
    f3.write(js)
js2 = json.loads(js)
del js2["META"]
n = 1
for k, v in js2.items():
    tmp_text = readme_add.format(ext_name=v["name"].upper(
    ), name=v["name"], author=v["author"], description=v["description"], version=v["version"], no=n)
    n = n+1
    readme = readme+tmp_text
readme = readme+readme_end
with open("README.md", "w") as f4:
    f4.write(readme)

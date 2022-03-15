# -*-coding:utf8;-*-
import time
import os
import sys
"""
QPy CMD extension
name: download
description: simple file downloader.
version: v1.0
author: guangrei
require: ""
"""
argv = sys.argv


def get_contents(url):
    try:
        import ssl
        import urllib.request
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except:
        try:
            import requests
            response = requests.get(url, verify=False)
            return response.text
        except:
            return False


def valid_name(nm):
    check = not os.path.exists(nm)
    if check:
        return True
    else:
        print("%s is already exists!" % nm)
        return False


def put_contents(fn, tx):
    fn = str(fn)
    with open(fn, "w") as f:
        f.write(tx)


def valid_url(url):
    try:
        from urlparse import urlparse  # python2
    except:
        from urllib.parse import urlparse
    try:
        result = urlparse(url)
        c = all([result.scheme, result.netloc])
        if c:
            return True
        else:
            print("invalid url!")
            return False
    except:
        print("invalid url!")
        return Fale


if __name__ == "__main__":

    if len(argv) == 3:
        if valid_url(argv[1]) and valid_name(argv[2]):
            print("downloading %s" % argv[1])
            ts = int(time.time())
            res = get_contents(argv[1])
            if res != False:
                put_contents(argv[2], res)
                ts = int(time.time()) - ts
                print("download success in %d sec" % ts)
            else:
                print("failed to fetch content!")
    else:
        print("Usage: download <url> <file-name>")

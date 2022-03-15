# -*-coding:utf8;-*-
import os
"""
QPy CMD extension
name: ext-maker
description: extension maker.
version: v0.1
author: guangrei
require: ""
"""
path = os.environ["EXT_DIR"].split("/")
del path[-1]
path = "/".join(path)
tmp = """# -*-coding:utf8;-*-
import os
import sys
\"\"\"
QPy CMD extension
name: {name}
description: {description}
version: v0.1
author: {author}
require: "{require}"
\"\"\"
argv = sys.argv # argv
path = os.environ["EXT_DIR"] # your extension path
if __name__ == "__main__":
    print("Hello World!")
"""
while True:
    name = input("your extension name (required) : ")
    if name=="":
        pass
    else:
        name = name.replace(" ","-")
        if not os.path.isdir(path+"/"+name):
            os.mkdir(path+"/"+name)
            break
        else:
            print("extension name already exists!")

while True:
    description = input("your extension description (required): ")
    if description=="":
        pass
    else:
        break

while True:
    author = input("your name (required): ")
    if author=="":
        pass
    else:
        break
require = input("your extension dependency (separate with comma, optional): ")

end = tmp.format(name=name,author=author,description=description,require=require)

with open(path+"/"+name+"/main.py", "w") as f1:
    f1.write(end)

with open(path+"/"+name+"/.version", "w") as f2:
    f2.write("v0.01")

print("Success creating extension, now you can edit your extension at ", path+"/"+name)    
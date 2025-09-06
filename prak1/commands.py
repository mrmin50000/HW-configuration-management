import os
import re

def cd(path):
    try:
        os.chdir(path)
    except:
        print("not found directory")

def echo(text):
    print(parse(text))

def ls():
    print("ls")

def parse(var):
    pattern = r'^\$\w+$'
    match = re.search(pattern, var)
    if match:
        return os.environ.get(var[1:])
    else:
        return var



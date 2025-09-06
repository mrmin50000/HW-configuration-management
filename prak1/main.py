import socket
import os
from pathlib import Path
from commands import *
import sys

HOSTNAME = socket.gethostname()
USERNAME = os.getlogin()
CWD = os.getcwd()
HOME = Path.home()
VFS_PATH = sys.argv[1]
SHITRC_PATH = sys.argv[2]
i = 0

if not os.path.isfile(VFS_PATH):
    print("not found vfs file")
    exit()
if not os.path.isfile(SHITRC_PATH):
    print("not found shitrc file")
    exit()
print(f'vfs file: {VFS_PATH}, shitrc file: {SHITRC_PATH}')

with open(SHITRC_PATH, "r", encoding="utf-8") as file:
    content = file.readlines()

while True:
    CWD = os.getcwd()
    print(f'{HOSTNAME}@{USERNAME}:{CWD}$ ', end="")

    if i < len(content):
        command = content[i].strip()
        i+=1
        print(f'{command}')
    else:
        command = input()

    if command == "exit":
        exit()
    elif command[:3] == "cd ":
        cd(command[3:])
    elif command == "ls":
        ls()
    elif command == "":
        continue
    elif command[:4] == "echo":
        echo(command[5:])
    else:
        print("unknown command")

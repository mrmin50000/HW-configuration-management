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

if not os.path.isfile(VFS_PATH):
    print("not found vfs file")
    exit()
if not os.path.isfile(SHITRC_PATH):
    print("not found shitrc file")
    exit()
print(f'vfs file: {VFS_PATH}, shitrc file: {SHITRC_PATH}')

while True:
    CWD = os.getcwd()
    print(f'{HOSTNAME}@{USERNAME}:{CWD}$ ', end="")
    command = input()
    if command == "exit":
        break
    elif command[:3] == "cd ":
        print(command)
    elif command == "ls":
        print(command)
    elif command == "":
        continue
    elif command[:4] == "echo":
        echo(command[5:])
    else:
        print("unknown command")

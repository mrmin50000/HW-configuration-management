import socket
import os
from pathlib import Path
from commands import *

HOSTNAME = socket.gethostname()
USERNAME = os.getlogin()
CWD = os.getcwd()
HOME = Path.home()


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

import subprocess
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

subprocess.run(["python", "../main.py", "../vfs/test.csv", "./.egrc"])


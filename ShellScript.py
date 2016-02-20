import subprocess
import os

cwd = os.getcwd()
print subprocess.Popen("git status", cwd = cwd, shell=True, stdout=subprocess.PIPE).stdout.read()

print subprocess.Popen("ls", cwd = cwd, shell=True, stdout=subprocess.PIPE).stdout.read()

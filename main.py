import os
import getpass

print("whoami = " + getpass.getuser())

cwd = os.getcwd()
print(cwd)

os.chdir("/opt/render/.cache/")
cwd = os.getcwd()
print(cwd)

f = open("myfile.txt", "x")
f.write("THIS IS A TEST")
f.close()

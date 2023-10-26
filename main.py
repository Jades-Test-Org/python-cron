import os
import getpass

print("whoami = " + getpass.getuser())

print("Current directory is" + os.getcwd())

print("Changing directory to /opt/render/")
os.chdir("/opt/render/")

print("List files and directories")
print(os.listdir())

f = open("/opt/render/.cache/myfile.txt", "x")
f.write("THIS IS A TEST")
f.close()

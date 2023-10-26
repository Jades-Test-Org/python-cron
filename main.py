import os

cwd = os.getcwd()
print(cwd)

f = open("/opt/render/.cache/myfile.txt", "x")
f.write("THIS IS A TEST")
f.close()

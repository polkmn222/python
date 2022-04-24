# 라이브러리

import sys
print(sys.argv)

sys.exit()

print(sys.path)

print(sys.path.append("C:/Users/user/Desktop/python/chap05"))

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

import os
print(os.environ)

print(os.environ['PATH'])

print(os.chdir("C:\WINDOWS"))

print(os.getcwd())

print(os.system("dir"))

import os
f = os.popen("dir")
print(f.read())

import shutil
shutil.copy("test.txt", "test1.txt")

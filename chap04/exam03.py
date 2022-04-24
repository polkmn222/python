# 파일 읽고 쓰기

"""
f = open("새파일.txt", 'w')
f.close()
"""

f = open("C:/test/새파일.txt", 'w')
f.close()

"""
나혼자 코딩
복습.txt 파일을 C:/test 디렉터리에 만들어보자.
"""
f = open("C:/test/복습.txt", 'w')
f.close()

f = open("C:/test/복습.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

f = open("C:/test/복습.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("C:/test/복습.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

"""
while 1:
    data = input()
    if not data: break
    print(data)
"""

f = open("C:/test/복습.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/test/복습.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("C:/test/복습.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

"""
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
"""
"""
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
"""
import sys

args = sys.argv[1:]
for i in args:
    print(i)

import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end = ' ')

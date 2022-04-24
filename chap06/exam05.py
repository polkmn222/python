# 탭을 4개의 공백으로 바꾸기

import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)

# C:\Users\user\Desktop\python\chap06
# tabto4.py a.txt b.txt

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)

# tabto4.py a.txt b.txt

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
f = open(dst, 'w')
f.write(space_content)
f.close()

# tabto4.py a.txt b.txt

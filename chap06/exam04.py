# 간단한 메모장

# C:/Users/user/Desktop/python/chap06/memo.py

import sys

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)


#cd C:\Users\user\Desktop\python\chap06
#python memo.py -a "Life is too short"

# C:/Users/user/Desktop/python/chap06/memo.py

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.text', 'a')
    f.write(memo)
    f.write('\n')
    f.close()


# python memo.py -a "Life is too short"
# python memo.py -a "You need python"
# python memo.py -v

import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.text', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = f.read()
    f.close()
    print(memo)
    
# python memo.py -v
# Life is too short
# You need python

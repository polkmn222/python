# 파이썬은 인간다운 언어이다

if 4 in [1, 2, 3, 4]: print("4가 있습니다")

languages = ['python', 'perl', 'c', 'java']

for lang in languages:
        if lang in ['python', 'perl']:
                print("%6s need interpreter" % lang)
        elif lang in ['c', 'java']:
                print("%6s need compiler" % lang)
        else:
                print("should not reach here")
                
# 파이썬 기초 문법

print(1 + 1)

print(1 + 2)

print(3 / 2.4)

print(3 * 9)

a = 1
b = 2
print(a + b)

a = "Python"
print(a)

a = "Python"
a
'Python'
a = 3
if a > 1:
    print("a is greater than 1")

for a in [1, 2, 3]:
    print(a)

i = 0
while i < 3:
    i = i + 1
    print(i)

	
def add(a, b):
    return a + b

add(3, 4)

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
print(len(a))

"""
나 혼자 코딩
'You need python' 문장을
문자열로 만들고 길이를 구해보자.
"""
a = "You need python"
print(a)
print(len(a))

a = "Life is too short, You need Python"
print(a[3])

print(a[0])

print(a[-1])

print(a[-0])

print(a[-2])

print(a[-5])

b = a[0] + a[1] + a[2] + a[3]
print(b)

print(a[0:4])

print(a[0:3])

print(a[0:5])

print(a[0:2])

print(a[5:7])

print(a[12:17])

print(a[19:])

print(a[:17])

print(a[:])

print(a[19:-7])

a = "20220415Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

year = a[:4]
day = a[4:8]
wheather = a[8:]

print(year)
print(day)
print(weather)

a = "Pithon"
b = a[:1] + 'y' + a[2:]
print(b)

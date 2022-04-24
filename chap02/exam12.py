# 변수

a = [1, 2, 3]
print(id(a))

b = a
print(id(b))

print(a is b)

a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
a = [1, 2, 3]
b = copy(a)

print(a)
print(b)
print(b is a)

a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']

a = b = 'python'

a = 3
b = 5
a,b = b, a
print(a)
print(b)

"""
나 혼자 코딩
"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

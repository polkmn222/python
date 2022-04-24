#튜플

t1 = ()
print(t1)

t2 = (1,)
print(t2)

t3 = (1, 2, 3)
print(t3)

t4 = 1, 2, 3
print(t4)

t5 = ('a', 'b', ('ab', 'cd'))
print(t5)

t1 = (1, 2, 'a', 'b')
"""
del t1[0]
"""
"""
t1[0] = 'c'
"""

print(t1[0])

print(t1[3])

print(t1[1:])

t2 = (3, 4)
print(t1 + t2)

print(t2 * 3)

print(len(t1))

"""
나 혼자 코딩
(1, 2, 3)이라는 튜플에 값 4를 추가하여 (1, 2, 3, 4)를 만들어 보자.
"""
t1 = (1, 2, 3)
t2 = (4,)
print(t1 + t2)

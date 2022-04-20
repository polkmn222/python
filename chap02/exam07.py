a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

a = [1, 2, 3]
print(a * 3)

print(len(a))

"""
a[2] + "hi"
"""

str(a[2]) + "hi"

a[2] = 4
print(a)

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))

print(a.index(1))

"""
a.index(0)
"""
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)

a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)
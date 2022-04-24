# 리스트 자료형

odd = [1, 3, 5, 7, 9]
print(odd)

a = []
print(a)

b = [1, 2, 3]
print(b)

c = ['Life', 'is', 'too', 'short']
print(c)

d = [1, 2, 'Life', 'is']
print(d)

e = [1, 2, ['Life','is']]
print(e)

# 리스트 인덱싱과 슬라이싱

a = [1, 2, 3]
print(a)

print(a[0])

print(a[0] + a[2])

print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a)

print(a[0])

print(a[-1])

print(a[3])

print(a[-1][0])

print(a[-1][1])

print(a[-1][2])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = "12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

"""
나 혼자 코딩
A = [1, 2, 3, 4, 5] 리스트에서 슬라이싱 기법을 사용하여 리스트 [2, 3]를 만들어보자.
"""
A = [1, 2, 3, 4, 5]
print(A[1:3])

a = [1, 2, 3, ['a','b','c'], 4, 5]
print(a[2:5])
print(a[3][:2])

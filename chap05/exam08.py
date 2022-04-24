def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

print(hex(234))

print(hex(3))

a = 3
print(id(3))

print(id(a))

b = a

print(id(b))

print(id(4))

a = input()
print(a)

b = input("Enter: ")
print(b)

print(int('3'))

print(int(3.4))

print(int('11', 2))

print(int('1A', 16))

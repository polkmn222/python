class Person: pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))

print(len("python"))

print(len([1, 2, 3]))

print(len((1, 'a')))

print(list("python"))

print(list((1, 2, 3)))

a = [1, 2, 3]
b = list(a)
print(b)

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x): return x*2

print(list(map(two_times, [1, 2, 3, 4])))

print(list(map(lambda a: a*2, [1, 2, 3, 4])))

print(max([1, 2, 3]))
print(max("python"))

print(min([1, 2, 3]))
print(min("python"))

print(oct(34))
print(oct(12345))

f = open("binary_file", "rb")

fread = open("read_mode.txt", 'r')
fread2 = open("read_mode.txt")

fappend = open("append_mod.txt", 'a')

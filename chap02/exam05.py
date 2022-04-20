a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a = "Life is too short"
print(a.index('t'))
#print(a.index('k'))

print(",".join('abcd'))

print(",".join(['a','b','c','d']))

a = "hi"
print(a.upper())

a = "HI"
print(a.lower())

a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

print(a.split())

b = "a:b:c:d"
print(b.split(':'))
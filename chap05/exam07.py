# 내장 함수

print(abs(3))

print(abs(-3))

print(abs(-1.2))

print(all([1, 2, 3]))

print(all([1, 2, 3, 0]))

print(any([1, 2, 3, 0]))

print(any([0, ""]))


print(chr(97))

print(chr(48))

print(dir([1, 2, 3]))

print(dir({'1' : 'a'}))

print(divmod(7,3))

print(7 // 3)

print(7 % 3)

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print(eval('1+2'))

print(eval("'hi' + 'a'"))

print(eval('divmod(4, 3)'))

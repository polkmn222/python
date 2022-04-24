# 문자열 포매팅

from ctypes.test.test_pickling import name
print("I eat %d apples."  % 3)

print("I eat %s apples."  % "five")

number = 3
print("I eat %d apples."  % number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days."  %(number, day))

print("I have %s apples"  % 3)

print("rate is %s"  % 3.234)

print("Error is %d%%." % 98)

print("%10s" % "hi")

print("%-10sjane" % 'hi')

print("%0.4f" %3.42134234)

print("%10.4f" %3.42134234)

print("I eat {0} apples".format(3))

print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples".format(number))

number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days".format(number, day))

print("I eat {number} apples. so I was sick for {day} days".format(number=10, day=3))

print("I eat {0} apples. so I was sick for {day} days".format(10, day=3))

print("{0:<10}".format("hi"))

print("{0:>10}".format("hi"))

print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))

print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))

print("{0:10.4f}".format(y))

print("{{ and }}".format())

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age' : 30}
print(f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')

print(f'{"hi":>10}')

print(f'{"hi":^10}')

print(f'{"hi":=^10}')

print(f'{"hi":!<10}')

y = 3.42134234
print(f'{y:0.4f}')

print(f'{y:10.4f}')

print(f'{{ and }}')

"""
나 혼자 코딩
format 함수 또는 f 문자열 포매팅을 사용해 '!!!python!!!' 문자열을 출력해보자
"""
print(f'{"!!!python!!!"}')
print(f'{"pyhton":!^12}')
"{0:!^12}".format('python')

# 예외처리

"""
f = open("나 없는 파일" 'r')
"""

"""
4/0
"""

"""
a = [1, 2, 3]
a[4]
"""

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

"""
나 혼자 코딩
앞에서 나온 3번 방법을 사용해 IndextError가 발생할 때 오류 메시지를
출력하는 소스를 작성해보자.
"""

try:
    a = [1, 2, 3]
    a[4]
except IndexError as e:
    print(e)

"""
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
"""

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

try:
    a = [1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
   
try:
    f = open("나 없는 파일", 'r')
except FileNotFoundError:
    pass

"""
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
"""
class Bird:
    def fly(self):
        print("very fast")

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
say_nick("천사")
"""
say_nick("바보")
"""
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)   

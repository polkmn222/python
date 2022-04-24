"""
Q1. 다음은 Calculator 클래스이다.
"""
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

"""
위 클래스를 상속하는 UpgradeCalculator를 만들고 뺄 수 있는 minus 메서드를
추가해보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.
"""
class UpgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

"""
Q2. 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator
클래스를 만들어보자. 즉 다음과 같이 동작해야 한다.
단 반드시 Calculator 클래스를 상속해서 만들어야 한다.
"""
class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100
            
        
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

"""
Q3. 다음 결과를 예측해보자.
"""
# 1 all([1, 2, abs(-3)-3])
print(all([1, 2, abs(-3)-3]))

# 2 chr(ord('a')) == 'a'
print(chr(ord('a')) == 'a')

"""
Q4. filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3] 에서 음수를 모두 제거해보자.
"""
def positive(x):
    return x > 0

print(list(filter(positive, [1, -2, 3, -5, 8, -3])))
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

"""
Q5. 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
"""
print(hex(234))
"""
이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해보자.
"""
print(int(0xea))

"""
Q6. map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진
[3, 6, 9, 12] 를 만들어보자.
"""
print(list(map(lambda a: a*3, [1, 2, 3, 4])))

"""
Q7. 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
[-8, 2, 7, 5, -3, 5, 0, 1]
"""
print(max([-8, 2, 7, 5, -3, 5, 0, 1]))
print(min([-8, 2, 7, 5, -3, 5, 0, 1]))

"""
Q8. 17 / 3 의 결과는 다음과 같다.
"""
print(17 / 3)
"""
위와 같은 결괏값 5.666666666666667을 소숫점 4자리까지만 반올림하여 표시해보자.
"""
print(round(17 / 3, 4))

"""
Q9. 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해보자.
"""
import sys

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)

print(result)

#cd C:\Users\user\Desktop\python\chap05
#exam0.py 1 2 3 4 5 6 7 8 9 10

"""
Q10. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해보자.
"""

import os
os.chdir("C:/Users/user/Desktop/python/chap05")
result = os.popen("dir")
print(result.read())

"""
Q11. glob 모듈을 사용하여 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는
프로그램을 작성해보자.
"""
import glob
print(glob.glob("C:/Users/user/Desktop/python/chap05/*.py"))

"""
Q12. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
2022/04/20 17:42:32
"""
import time
print(time.strftime('%Y/%m/%d %H:%M:%S'))

"""
Q13. random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자
(단 중복된 숫자가 있으면 안 됨).
"""
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)        

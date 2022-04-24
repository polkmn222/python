"""
Q6. 숫자의 총합 구하기
사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는
프로그램을 작성하시오.(단 숫자는 콤마로 구분하여 입력한다.)
65,45,2,3,45,8
"""
x = input('number : ')
numbers = x.split(",")
total = 0
for i in numbers:
    total += int(i)

print(total)

"""
Q7. 한 줄 구구단
사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오.
실행 예)
구구단을 출력할 숫자를 입력하세요(2~9): 2
2 4 6 8 10 12 14 16 18
"""
x = input('구구단을 출력할 숫자를 입력하세요(2~9): ')
number = 0
for i in range(1, 10):
    number = int(x) * i
    print(number, end = ' ')
    
"""
Q8. 역순 저장
다음과 같은 내용의 파일 abc.txt가 있다.
AAA
BBB
CCC
DDD
EEE

이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
EEE
DDD
CCC
BBB
AAA
"""
f = open("abc.txt", 'w')
f.write("AAA\n")
f.write("BBB\n")
f.write("CCC\n")
f.write("DDD\n")
f.write("EEE\n")
f.close()

f= open("abc.txt", 'w+')
f.write("EEE\n")
f.write("DDD\n")
f.write("CCC\n")
f.write("BBB\n")
f.write("AAA\n")
f.close()

"""
Q9. 평균값 구하기
오른쪽과 같이 총 10줄로 이루어진 sample.txt 파일이 있다. sample.txt파일의 숫자 값을 모두 읽어
총합과 평균 값을 구한 후 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
"""
f = open("samlpe.txt", 'w')
f.write("70\n")
f.write("60\n")
f.write("55\n")
f.write("75\n")
f.write("95\n")
f.write("90\n")
f.write("80\n")
f.write("80\n")
f.write("85\n")
f.write("100\n")
f.close()


f = open("samlpe.txt", 'r')
total = 0
avg = 0
while True:
    line = f.readline()
    if not line:
        break
    total += int(line)

avg = total / 10
f.close()

f = open("result.txt", 'w')
f.write(str(avg))
f.close()

f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
avg = total / len(lines)    

f = open("result.txt", 'w')
f.write(str(avg))
f.close()

"""
Q10. 사칙연산 계산기
다음과 같이 동작하는 클래스 Calculator를 작성하시오.
cal1 = Calculator([1, 2, 3, 4, 5])
cal1.sum()
cal1.avg()
cal2 = Calculator([6, 7, 8, 9, 10])
cal2.sum()
cal2.avg()
"""
class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        result = 0
        for i in self.numberList:
            result += i
        return result / len(self.numberList)    


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())


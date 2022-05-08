"""
Q11. 모듈 사용 방법
C:\Users\user\Desktop\python\chap08 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자.
명령 프롬포트 창에서 파이썬 셀을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.
(즉 다음과 같이 import mymod를 수행할때 오류가 없어야 한다.
import mymod
"""
import sys
sys.path.append("C:/Users/user/Desktop/python/chap08")
import mymod


"""
set PYTHONPATH=C:\Users\user\Desktop\python\chap08
python
import mymod
"""
"""
cd C:\Users\user\Desktop\python\chap08
python
import my mod
"""

"""
Q12. 오류와 예외 처리
다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.
"""
result = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0

except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
"""
IndexError 가 실행되고 finally는 무조건 실행되서 7
"""

"""
Q13. DashInsert 함수
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면
*를 추가하는 기능을 가지고 있다. DashInsert 함수를 완성하시오.
입력 예시 : 4546793
출력 예시 : 454*67-9-3
"""
def DashInsert(n):
    result = []
    for i in range(len(n)-1):
        result.append(n[i])
        if(int(n[i])%2 == 0 and int(n[i+1])%2 == 0):
           result.append('*')
        elif(int(n[i])%2 == 1 and int(n[i+1])%2 == 1):
            result.append('-')

        if(i == len(n)-2):
           result.append(n[len(n)-1])

    return result

print(''.join(DashInsert(list(input("입력 :")))))

"""
Q14. 문자열 압축하기
문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.
입력 예시 : aaabbbcccccca
출력 예시 : a3b2c6a1
"""
def compress(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compress("aaabbcccccca"))

"""
Q15. Duplicate Numbers
0~9 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만
사용한 것인지 확인하는 함수를 작성하시오.
입력 예시 : 0123456789 01234 01234567890 6789012345 012322456789
출력 예시 : True False False True False
"""
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10


print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))
print(chkDupNum("012322456789"))

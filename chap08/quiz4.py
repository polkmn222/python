"""
Q16. 모스 부호 해독
문자열 형식으로 입력받은 모스 부호(dot: . dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
- 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
"""
dic = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}


def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


"""
Q17. 기초 메타 문자
다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?
1. acccb
2. a....b
3. aaab
4. a.cccb
"""

import re

p = re.compile("a[.]{3,}b")

print(p.match("acccb"))
print(p.match("a....b")) # 정답
print(p.match("aaab"))
print(p.match("a.cccb"))


"""
Q18. 문자열 검색
다음 코드의 결괏값은 무엇일까?
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()
"""

import re

p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start() + m.end())
# 10



"""
Q19. 그루핑
다음과 같은 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식을 사용하여 작성하시오.

park 010-9999-9988
kim 010- 9909-7789
lee 010-8789-7768

"""

import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)


"""
Q20. 전방탐색
다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr
등과 매치된다. 긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을
작성하시오.
"""

import re

pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))
# 프로그래밍 시작

"""
result = GuGu(2)

def GuGu(n):
    print(n)

def GuGu(n):
    result = []
"""
def GuGu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result

print(GuGu(2))

i = 1
while i < 10:
    print(i)
    i = i + 1
    
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2))

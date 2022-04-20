import mod1
print(mod1.add(3,4))

print(mod1.sub(4,2))

from mod1 import add
print(add(3, 4))

from mod1 import add, sub
from mod1 import *

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI, 4.4))

"""
나혼자 코딩
mod2.py 모듈을 사용해 반지름이 5인 원의 넓이를 계산해보자.
"""
a = mod2.Math()
print(a.solv(5))

import mod2
result = mod2.add(3, 4)
print(result)


"""
a.b

a[.]b

ca*t

ca+t

ca{2}t

ca{2,5}t

ab?c
"""
import re
p = re.compile('ab*')

import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

"""
p = re.compile(정규 표현식)
m = p.match("조사할 문자열")
if m:
    print('Match found: ', m.group())
else:
    print('No match')
"""

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)

for r in result: print(r)

import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())

print(m.start())

print(m.end())

print(m.span())

m = p.search("3 python")
print(m.group())

print(m.start())

print(m.end())

print(m.span())

p = re.compile('[a-z]+')
m = p.match("python")
m = re.match('[a-z]+', "python")

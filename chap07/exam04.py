import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

print(re.search('^Life', 'Life is too short'))

print(re.search('^Life', 'My Life'))

print(re.search('short$', 'Life is too short'))

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))

print(p.search('the declassified algorithm'))

print(p.search('one subclass is'))

p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))

print(p.search('the declassified algorithm'))

print(p.search('one subclass is'))

# (ABC)+

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)

print(m.group(0))

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

# (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)

p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())


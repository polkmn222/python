import re
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

# .*[.]. *$

# .*[.][^b].*$

# .*[.]([^b]..|.[^a].|..[^t])$

# .*[.]([^b].?.?|.9^a]?.?|..?[^t]?)$

# .*[.](?!bat$).*$

# .*[.](?!bat$|exe$).*$

p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))

print(p.sub('colour', 'blue socks and red shoes', count=1))

print(p.subn('colour', 'blue socks and red shoes'))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+[-]\d+)")
print(p.sub("\g<phone>\g<name>", "park 010-1234-1234"))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+[-]\d+)")
print(p.sub("\g<2>\g<1>", "park 010-1234-1234"))

def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))

s = '<html><head><title>Title</title>'
print(len(s))

print(re.match('<.*>', s).span())

print(re.match('<.*>', s).group())

print(re.match('<.*?>', s).group())

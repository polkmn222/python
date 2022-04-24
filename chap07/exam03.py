import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]', re.I)
print(p.match('python'))

print(p.match('Python'))

print(p.match('PYTHON'))

import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]
 (
   0[0-7]+
 | [0-9]+
 | x[0-9a-fA-F]+
 )
 ;
 """, re.VERBOSE)

# \section
# [ \t\n\r\f\v]ection
# \\section

p = re.compile('\\section')

p = re.compile('\\\\section')

p = re.compile(r'\\\section')

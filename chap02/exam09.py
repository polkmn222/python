# 딕셔너리 자료형

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(dic)

a = {1: 'hi'}
print(a)

a = {'a': [1, 2, 3]}
print(a)

a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1:'a', 2:'b'}
print(a[1])
print(a[2])

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a = {1:'a', 1:'b'}
print(a)

"""
a = {[1,2] : 'hi'}
"""

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.keys())

print(list(a.keys()))

print(a.values())

print(a.items())

a.clear()
print(a)

a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

print(a.get('nokey'))

"""
print(a['nokey'])
"""

print(a.get('foo', 'bar'))

print('name' in a)

print('email' in a)

"""
나 혼자 코딩
"""
a = {'name': '홍길동', 'birth':1128, 'age':30}
print(a)

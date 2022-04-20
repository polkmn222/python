money = True
if money:
    print("택시를 타고가라")
else:
    print("걸어 가라")

x = 3
y = 2

print(x > y)        

print(x < y)

print(x == y)

print(x != y)

money = 2000
if money >= 3000:
    print("택시를 타고가라")
else:
    print("걸어가라")

money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타고가라")
else:
    print("걸어가라")
        
print(1 in [1, 2, 3])        

print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

"""
나 혼자 코딩
'주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라'
는 문장을 조건문으로 만들어 보자.
"""
pocket = ['card', 'cellphone', 'money']
if 'card' in pocket:
    print('버스를 타고가라')
else:
    print('걸어가라')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어가라")
             
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고가라')
else:
    if card:
        print('택시를 타고가라')
    else:
        print('걸어가라') 

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고가라')
elif card:
    print('택시를 타고가라')
else:
    print('걸어가라') 

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

score = 80
if score >= 60:
    message = "success"
else:
    message = "failure"                       

message = "success" if score >= 60 else "failure"
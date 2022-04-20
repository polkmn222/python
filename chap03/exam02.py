treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 딸어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
money = 300
while money:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 딸어졌습니다. 판매를 중지합니다.")
        break  

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

"""
나혼자 코딩
1부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력해보자
"""
a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)  

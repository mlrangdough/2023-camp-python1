import random
com = random.randrange(101)
cnt = 1
while True:
    num = int(input("숫자를 하나 입력해주시오(1~100):"))
    if num>com:
        print("DOWN!")
    elif num<com:
        print("UP!")
    elif num==com:
        print("정답!숫자:%d"%com)
        print("%d번째에 맞췄습니다!"%cnt)
    else:
        print("잘못 입력했습니다")
    cnt+=1
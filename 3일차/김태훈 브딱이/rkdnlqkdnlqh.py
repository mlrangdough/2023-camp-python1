import random
print("+++++++++++++++가위바위보 게임++++++++++++")
user = input("가위바위보 중 하나를 입력 하시오:")
com = random.randrange(1,4)
if com ==1:
    if user == '가위':
        print("User:%s vs Com:가위"%user)
        print("비겼습니다 아쉽네요")
    elif user == '바위':
        print("User:%s vs Com:가위"%user)
        print("이겼습니다")
    if user == '보':
        print("User:%s vs Com:가위"%user)
        print("졌습니다")
elif com ==2:
    if user == '가위':
        print("User:%s vs Com:가위"%user)
        print("졌습니다 아쉽네요")
    elif user == '바위':
        print("User:%s vs Com:가위"%user)
        print("비겼습니다")
    if user == '보':
        print("User:%s vs Com:가위"%user)
        print("이겻습니다")
if com ==3:
    if user == '가위':
        print("User:%s vs Com:가위"%user)
        print("이겼습니다 아쉽네요")
    elif user == '바위':
        print("User:%s vs Com:가위"%user)
        print("졌습니다")
    if user == '보':
        print("User:%s vs Com:가위"%user)
        print("비겼습니다")
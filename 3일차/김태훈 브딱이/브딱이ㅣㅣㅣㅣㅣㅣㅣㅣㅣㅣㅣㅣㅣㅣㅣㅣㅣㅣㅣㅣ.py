a = int(input('삼각형의 크기를 입력하시오'))
for i in range(a+1,1,-1):
    for j in range(i):
        print("*",end="")
    print()
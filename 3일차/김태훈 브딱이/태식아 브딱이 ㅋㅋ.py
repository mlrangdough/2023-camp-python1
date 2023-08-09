a= int(input("숫자입력"))
for i in range(1,a+1) :
    if i == 3 or i==6 or i == 9:
        print("짝",end=" ")
    else :
        print(i,end=" ")
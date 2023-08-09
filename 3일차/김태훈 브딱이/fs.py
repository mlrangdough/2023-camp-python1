a = float(input("키를 입력하시오."))
b = float(input("체중을 입력하시오."))
c = b/(a**2)
if c <= 18.5 :
    print("저체중 입니다")
elif c < 22.9 and c>= 18.5 :
    print("정상 입니다")
elif c<= 24.9 and c>= 23 :
    print("과체중 입니다")
elif c <= 29.9 and c>=25 :
    print("비만입니다")
elif c >=30 :
    print("고도비만 입니다")
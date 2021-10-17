a=int(input("清輸入你買的汽水數量:"))
b=a
c=0
while a>=3:
    a=a-3
    a+=1
    c+=1
print("你買了",b,"罐","\n","你共可以喝",b+c,"罐")
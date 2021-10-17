num=str(input("請輸入一個數字:"))
sum = 0
for i in range(len(num)):
    sum += int(num[i])
print("共",len(num),"位數","\n","各位數總和為:",sum)
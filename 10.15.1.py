import random as ran
list1=[]
for i in range (1,11):
    n=ran.uniform(-200,200)
    a=round(n,2)
    list1.append(a)
b=max(list1)
c=min(list1)
print(list1)
print(list,"最大值=",b,"最小值=",c)
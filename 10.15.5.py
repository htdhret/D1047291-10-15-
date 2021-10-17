n=int(input())
a=0
c=0
for i in range(1,n+1):
    a+=1
    b=a*(a+1)
    c+=b
print(c)
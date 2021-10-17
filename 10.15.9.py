n=int(input("n="))
a=0
for i in range(0,n//2):
    sum=0
    j=i
    list1=[]
    for i in range(0,n//2):
        j+=1
        sum+=j
        list1.append(j)
        s=str(list1)
        if sum==n:
            a+=1
            print(s.replace(",","+").replace("[","").replace("]",""),"\n")
if a==0:
    print("No","\n")
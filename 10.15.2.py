x = int(input("輸入第一個數字"))
y = int(input("輸入第二個數字"))
if x > y :
    a = x
else:
    a = y
for k in range(a, 2, -1):
    if x % k == 0 and x % k == 0:
        print(k)
        break
x = int(input("輸入第一個數字"))
y = int(input("輸入第二個數字"))
if x > y :
    a = x
else:
    a = y
m = (x + 1) * (y + 1)
for k in range(a, m):
    if k % x == 0 and k % y == 0:
        print(k)
        break
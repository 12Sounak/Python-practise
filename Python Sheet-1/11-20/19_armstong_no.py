# 19.Write a Python Program to Check Armstrong Number?
def Armstrong(n):
    sum = 0
    t=n
    x=str(t)
    y=len(x)
    while t>0:
        r = int(t%10)
        sum = sum + r**y
        t = t/10
    print(sum)
    if sum == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

a = int(input("Enter a number :"))
Armstrong(a)
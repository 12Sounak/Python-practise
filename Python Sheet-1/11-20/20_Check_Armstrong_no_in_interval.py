# 20.Write a Python Program to Find Armstrong Number in an Interval?
def Armstrong(a,b):
    for i in range(a,b+1):
        sum = 0
        t=i
        x=str(t)
        y=len(x)
        while t>0:
            r = int(t%10)
            sum = sum + r**y
            t = t/10
        print(sum)
        if sum == i:
            print("Armstrong")
        else:
            print("Not Armstrong")

a = int(input("Enter a number :"))
b = int(input("Enter the limit :"))
Armstrong(a,b)
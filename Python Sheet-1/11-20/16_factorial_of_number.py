# 16.Write a Python Program to Find the Factorial of a Number?
# 5! = 1*2*3*4*5
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    print(f)

n = int(input("Enter the number :"))
fact(n)
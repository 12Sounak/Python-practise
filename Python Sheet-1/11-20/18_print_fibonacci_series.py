# 18.Write a Python Program to Print the Fibonacci sequence?
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fibo(n):
    t1 = 0
    t2 = 1
    next = t1+t2
    print("Fibonaci series is :",t1,t2)
    for i in range(3,n+1):
        print(next)
        t1 = t2
        t2 = next
        next = t1+t2

n =int(input("Enter a number :"))
fibo(n)
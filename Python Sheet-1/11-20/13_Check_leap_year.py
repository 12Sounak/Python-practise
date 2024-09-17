# 13.Write a Python Program to Check Leap Year?

"""
# Method - 1 (using inbuild functions and method)
import calendar

z = calendar.isleap(2004)
print(z)
"""

def check_prime(n):
    c = 0
    for i in range(2,n):
        if(n%i==0):
            c += 1
            print(c)
    if c==0:
        print("prime")
    else:
        print("not prime")
n = int(input("Enter a number :"))
check_prime(n)
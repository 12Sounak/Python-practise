# 10.Write a Python program to swap two variables without temp variable?
def swap2(a,b):
    a = a+b
    b = a-b
    a = a-b
    print(a,b)
a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))

print("Values before swap", a, b)
swap2(a,b)
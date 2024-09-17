# 17.Write a Python Program to Display the multiplication Table?
def table(n):
    for i in range(1,10+1):
        print(f"{n} * {i} =  {n*i}")

n = int(input("Enter a number :"))
table(n)
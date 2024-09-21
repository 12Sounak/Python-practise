# 21.Write a Python Program to Find the Sum of Natural Numbers?
def sum_of_naturalno(n):
    sum = 0
    for i in range(0,n+1):
        sum = sum + i

    print("The Sum of Natural no is :",sum)

n = int(input("Enter a number :"))
sum_of_naturalno(n)
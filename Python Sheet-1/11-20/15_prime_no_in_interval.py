# 15.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


def check_prime_range(a,b):
    c = 0
    temp = 0
    l = []
    nl = []
    for j in range(a,b+1):
        if j>1:
            for i in range(2,j):
                if(j%i==0):
                    c+=1
                    break
            else:
                l.append(j)
    print(l)
a = int(input("Enter 1st number :"))
b = int(input("Enter till range number :"))
check_prime_range(a,b)
# 22.Write a Python Program to Find LCM?
def lcm(n,m):
    x=set()
    y=set()
    for i in range(1,n+1):
        if n % i == 0:
            x.add(i)
    for j in range(1,m+1):
        if m % j == 0:
            y.add(j)
    

    z= x.intersection(y) 




    p = max(z)
    return (n*m) // p
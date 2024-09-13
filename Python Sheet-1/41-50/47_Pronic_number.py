def pronic_number(n):
    f = 0
    for i in range(0,n):
        if i*(i+1) == n:
                f = 1
    if f == 1:
        print("pronic number")
    else:
        print("not")


n = int(input("Enter a number:"))
pronic_number(n)
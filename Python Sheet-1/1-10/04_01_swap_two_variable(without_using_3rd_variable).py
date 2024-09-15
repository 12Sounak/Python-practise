def swap(a,b):
    a,b = b,a
    print("Variables After swap :",a,"",b)

x = int(input("Enter a number :"))
y = int(input("Enter a number :"))
print("Variables before swap :",x,"",y)
swap(x,y)
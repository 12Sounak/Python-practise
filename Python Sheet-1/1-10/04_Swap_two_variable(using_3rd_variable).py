# 4.  Write a Python program to swap two variables?
def swap(a,b):
    t = a 
    a = b 
    b = t 
    print("Values after swap:",a,"",b)

x = int(input("Enter a number :"))
y = int(input("Enter a number :"))
print("Values Before swap :",x,"",y)
swap(x,y)
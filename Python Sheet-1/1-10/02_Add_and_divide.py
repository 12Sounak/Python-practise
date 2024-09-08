def add(a,b):
    num = a+b 
    return num

def div(a,b):
    num1 = a/b
    return num1
    
x = int(input("Enter a number :"))
y = int(input("Enter another number :"))

result = add(x,y)
print("The Sum of 2 Numbers is:",result)

result1 = div(x,y)
print("The division is :",result1)

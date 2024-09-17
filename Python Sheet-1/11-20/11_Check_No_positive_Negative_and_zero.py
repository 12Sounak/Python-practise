# 11.Write a Python Program to Check if a Number is Positive, Negative or Zero?
def checkpnz(a):
    if(a==0):
        print("Zero")
    elif(a<0):
        print("Negative")
    else: 
        print("Positive")

n = int(input("Enter a number u want ot check :"))
checkpnz(n)
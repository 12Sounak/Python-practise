# 7. Write a Python program to convert Celsius to Fahrenheit?
def converttemp(c):
    f = 1.8*c + 32  
    print("The Temp is Farenheit is ",f)


temp_c=int(input("Enter the Temp in Celcius :"))
converttemp(temp_c)
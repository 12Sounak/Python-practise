# 6. Write a Python program to convert kilometers to miles?
def convert(km):
    result = km/1.6
    print("km Distance in miles is :",result)
    
km = int(input("Enter Distance in km to get converted in miles :"))
convert(km)
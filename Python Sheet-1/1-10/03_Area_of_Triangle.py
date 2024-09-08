# 2> Area of a triangle

def area(base,height):
    area = 1/2 * base * height
    return area

a = int(input("Enter The Base of the Triangle :"))
b = int(input("Enter The Height of the Triangle : "))
result = area(a,b)
print("The Area of the Triangle is :" ,result)
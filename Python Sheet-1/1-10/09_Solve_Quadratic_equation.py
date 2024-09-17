#9> Solve quadratic equation
# a**2 + b*x + c = 0
def quad(a,b,c):
    d = b**2 - (4*a*c)
    print(d)
    n1 = ((-b - d**(1/2))/(2*a))
    n2 = ((-b +d**(1/2))/(2*a))
    print(n1,n2)

a = int(input())
b = int(input())
c = int(input())
quad(a,b,c)
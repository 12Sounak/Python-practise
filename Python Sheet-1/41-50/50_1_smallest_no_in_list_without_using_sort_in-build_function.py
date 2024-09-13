def small(l):
    n = len(l)
    t=0
    for i in range(n-1):
        for j in range(i+1,n):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
                
    print(l[0])
a = eval(input("Enter the list :"))
small(a)
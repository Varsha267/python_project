import math
a=input("Enter a number or numbers: ")
if a.isdigit():
    a=a.split(",")
    l1=[]#b'coz it have multiple inputs we use list function for store them into list
    for i in a:
        l1.append(int(i))
        l1=sorted(l1)
    def isperfectsquare(x):
        s=int(math.sqrt(x))
        return s*s==x
    def isfibo(n):
        return isperfectsquare(5*n*n+4) or isperfectsquare(5*n*n-4)
    for i in l1:
        if (isfibo(i)==True):
            print(i,"is a Fibonacci Number")
        else:
            print(i,"is not a Fibonacci Number")
else:
    print("enter integers only")
a=int(input())
b=int(input())
c=int(input())

def getTri(a,b,c):
    if a<=0 or b<=0 or c<=0:
        print("not a triangle")
    elif a==b==c:
        print("equilateral triangle")
    elif a+b>c and a+c>b and b+c>a:
        if a==b or b==c or a==c:
            print("isosceles triangle")
        elif a*a==b*b+c*c or c*c==a*a+b*b or b*b==a*a+c*c: 
            print("right triangle")
        elif a*a>b*b+c*c or c*c>a*a+b*b or b*b>a*a+c*c : 
            print("obtuse triangle")
        else:
            print("acute triangle")
    else:
        print("not a triangle")
getTri(a,b,c)
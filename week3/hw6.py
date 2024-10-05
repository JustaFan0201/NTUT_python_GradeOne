import math
a=int(input())
b=int(input())
c=int(input())
T=b*b-4*a*c
if T>=0:
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    print("%.1f" %(x1))
    print("%.1f" %(x2))
else:
    x1 =-b/(2*a)
    x2 =-b/(2*a)
    x11=math.sqrt(-T)/2.0/a
    x22=math.sqrt(-T)/2.0/a
    print("%.1f+%.1fi" %(x1,x11))
    print("%.1f-%.1fi" %(x2,x22))

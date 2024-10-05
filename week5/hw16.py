import math
def getTri(a:int,b:int,c:int,flag:int,area):
    if a<=0 or b<=0 or c<=0:
        print("not a triangle")
        flag+=1
    elif a==b==c:
        print("equilateral triangle "+format(area,'.2f'))
    elif a+b>c and a+c>b and b+c>a:
        if a==b or b==c or a==c:
            print("isosceles triangle "+format(area,'.2f'))
        elif a*a==b*b+c*c or c*c==a*a+b*b or b*b==a*a+c*c: 
            print("right triangle "+format(area,'.2f'))
        elif a*a>b*b+c*c or c*c>a*a+b*b or b*b>a*a+c*c : 
            print("obtuse triangle "+format(area,'.2f'))
        else:
            print("acute triangle "+format(area,'.2f'))
    else:
        print("not a triangle")
        flag+=1
    return flag
    
flag=0
tri=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
area=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num=int(input())
for i in range(num):
    tri[i]=input()
    tri[i]=tri[i].split(" ",-1)

for i in range(num):
    s=(float(tri[i][0])+float(tri[i][1])+float(tri[i][2]))/2.0
    if (s*(s-float(tri[i][0]))*(s-float(tri[i][1]))*(s-float(tri[i][2])))>0:
        area[i]=math.sqrt(s*(s-float(tri[i][0]))*(s-float(tri[i][1]))*(s-float(tri[i][2])))
        area[i]=round(area[i],2)
    else:
        pass
    flag=getTri(int(tri[i][0]),int(tri[i][1]),int(tri[i][2]),flag,area[i])

if flag==num:
    print("All inputs are not triangles!")
else:
    max=0
    min=1000.0
    for i in range(len(area)):
        if float(area[i])>max:
            max=float(area[i])
        if float(area[i])<min and float(area[i])!=0:
            min=float(area[i])
    print(format(max,'.2f'))
    print(format(min,'.2f'))
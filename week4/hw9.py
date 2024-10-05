def sol(x1:int,x2:int):
    for i in range (x1,x2,1):
        total[i]=1
total=[]
sum=int(0)
for i in range (-20,41,1):
    total.append(int(0))
a1=int(input())
a2=int(input())
b1=int(input())
b2=int(input())
c1=int(input())
c2=int(input())
sol(a1,a2)
sol(b1,b2)
sol(c1,c2)

for i in range (-20,41,1):
    if total[i]==1:
        sum=sum+1
print(sum)


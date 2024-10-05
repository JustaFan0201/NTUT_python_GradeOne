def sol(x1:int,x2:int):
    for i in range (x1,x2,1):
        total[i]=1
total=[]
sum=int(0)
for i in range (-20,41,1):
    total.append(int(0))
num=int(input())
for i in range(num):
    save1=input()
    x1=save1.split(" ",-1)
    sol(int(x1[0]),int(x1[1]))

for i in range (-20,41,1):
    if total[i]==1:
        sum=sum+1
print(sum)


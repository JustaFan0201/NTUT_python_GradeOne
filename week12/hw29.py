def sol(save,num:int):
    if num==8:
        return 0
    if save[num]=="1":
        return 2**(7-num)+sol(save,num+1)
    elif save[num]=="0":
        return 0+sol(save,num+1)
def solve(result,num):
    if num==0.5:
        return ""
    if result-num>=0:
        return "1"+solve(result-num,num/2)
    elif result-num<0:
        return "0"+solve(result,num/2)
count=1
total=[]
while(1):
    save=input()
    if save=='0':
        count+=1
    elif save=='-1':
        break
    else:
        total.append(int(sol(save,0)))
result=[0 for k in range (count)]
for i in range(count):
    if total[i]==1:
        total[i]=0
    total[i]=int(total[i])
i=0
while(1):
    if total[i]==0:
        i+=1
        if i==count:
            break
    elif total[i]%2==0:
        total[i]=int(total[i]/2)
        result[i]+=1
    elif total[i]==1:
        total[i]=0
        result[i]+=1
    else:
        total[i]=int((total[i]+1)/2)
        result[i]+=1
for i in range(count):
    result[i]-=1
    print(solve(result[i],8))

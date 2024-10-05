def sol(put,num):
    if num==10:
        return 0
    if put[num]=="1":
        return 2**(9-num)+sol(put,num+1)
    else:
        return 0+sol(put,num+1) 
def solve(num):
    if num==0:
        return -1
    elif num%2==0:
        return 1+solve(int(num/2))
    elif num==1:
        return 1+solve(0)
    else:
        return 1+solve(int((num+1)/2))
def solve_FIN(result,num):
    if num==0.5:
        return ""
    if result-num>=0:
        return "1"+solve_FIN(result-num,num/2)
    elif result-num<0:
        return "0"+solve_FIN(result,num/2)
total=[]
result=[]
count=0
while(1):
    temp=input()
    if temp=="-1":
        break
    else:
        total.append(sol(temp,0))
        result.append(0)
        count+=1
for i in range(count):   
    for j in range(total[i]+1):
        if j==0 or j==1:
            pass
        else:
            result[i]+=solve(j)
    print(solve_FIN(result[i],8192))
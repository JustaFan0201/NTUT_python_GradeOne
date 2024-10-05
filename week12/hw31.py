def solve_FIN(result,num):
    if num==0.5:
        return ""
    if result-num>=0:
        return "1"+solve_FIN(result-num,num/2)
    elif result-num<0:
        return "0"+solve_FIN(result,num/2)
def sol(aBit,num,save,fin):
    if num==fin:
        return ""
    if num==0:
        return str(save)+sol(aBit,num+1,save,fin)
    elif aBit[num]==save:
        return "0"+sol(aBit,num+1,aBit[num],fin)
    else:
        return "1"+sol(aBit,num+1,aBit[num],fin)
count=0
result=[]
resu=[]
while(1):
    temp=input().split(" ")
    if temp[0]=="-1":
        break
    else:
        total=2**int(temp[0])
        for i in range(total):
            tempsave=solve_FIN(i,2**(int(temp[0])-1))
            result.append(sol(tempsave,0,tempsave[0],int(temp[0])))
        resu.append(result[int(temp[1])])
    result.clear()
    count+=1
for i in range(count):
    print(resu[i])
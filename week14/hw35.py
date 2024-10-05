def sol(data:dict,check:dict):
    result=[]
    result2={}
    resultTotal2=[]
    catch=data.keys()
    for i in catch:
        all_length=0
        temp=dict(data[i])
        checkForSame=[]
        for j in range (len(check)):
            temp2=dict(check[str(j)])
            length=0
            big=0
            for k in temp2.values():
                if k in temp.values() and k not in checkForSame:
                    checkForSame=checkForSame+[k]
                    all_length+=1
                if k in temp.values():
                    length+=1
            if all_length>big:
                big=all_length
                result2[i]=all_length
            if length==len(temp2) and i not in result:
                result=result+[i]
    ans=sorted(result2.items(),key=lambda x:x[1],reverse=True)
    ans=dict(ans)
    k=0
    for i,j in ans.items():
        if k==0:
            greater=j
            k+=1
        if j==greater:
            resultTotal2=resultTotal2+[i]
    return result,resultTotal2
lib={"GF":0,"BC":1,"NC":2,"CT":3,"NS":4,"NM":5,"HL":6,"NL":7}
data={}
result=[]
result2=[]
num=int(input())
for i in range(num):
    temp=input().split(" ")
    data[temp[0]]={}
    for j in range (1,len(temp)):
        data[temp[0]][temp[j]]=lib[temp[j]]
num_check=int(input())
i=0
count=0
while(1):
    if num_check==count:
        break
    check={}
    temp=input().split(" ")
    check[str(i)]={}
    for j in range (len(temp)):
        if temp[j]=="+":
            check[str(i+1)]={}
            i+=1
        else:
            check[str(i)][temp[j]]=lib[temp[j]]
    tempsave,tempsave2=sol(data,check)
    result=result+[tempsave]
    result2=result2+[list(tempsave2)]
    count+=1
    i=0
way=input()
if way=="0":
    for i in range(len(result)):
        for j in range(len(result[i])):           
            print(result[i][j],end=" ")
        print()
else:
    for i in range(len(result2)):
        for j in range(len(result2[i])):           
            print(result2[i][j],end=" ")
        print()
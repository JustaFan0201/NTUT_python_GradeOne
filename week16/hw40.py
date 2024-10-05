def check(data:str,start:list,end:list,startflag:int,endflag:int):
    mid=start+end
    for i in range(startflag+len(start[0]),endflag-len(end[0]),1):
        current=data[i:i+3]
        if current in mid :
            return 0
    return 1
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
start=[x for x in input().split(" ") if x!=""]
end=[x for x in input().split(" ") if x!=""]
data=input()
if data[-1]==" ":
    data=data[1:-2]
mid=[start]+[end]
startflag=[]
endflag=[]
result=[]
for i in range(len(data)):  
    if i<len(data)-len(start[0])+1:
        startcurrent=data[i:i+len(start[0])]
        if startcurrent in start:
            startflag+=[i]
    if i<len(data)-len(end[0])+1:
        endcurrent=data[i:i+len(end[0])]
        if endcurrent in end:
            endflag+=[i]
for i in startflag:
    for j in endflag:
        now=data[i+len(start[0]):j]
        if i<j and check(data,start,end,i,j)==1 and len(now)!=0 and is_prime(len(now))==1:
            result+=[data[i+len(start[0]):j]]
result=sorted(result)
result=sorted(result,key=lambda x:len(x))
if result:
    for i in range(len(result)):
        print(result[i])
else:
    print("No gene")
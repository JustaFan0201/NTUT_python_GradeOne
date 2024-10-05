import math
amount=int(input())
day=int(input())

infect=[]
infect.append(0)
infect.append(int(input()))

spread=float(input())
recoverday=int(input())
buff=float(input())

infect_people=[]
infect_people.append(0)
infect_people.append(infect[1])

recovernum=[]
recovernum.append(0)
recovernum.append(0)
total=0
for i in range(1,day+1):
    print(i,infect[i],infect_people[i],recovernum[i])
    spreadnum=float((spread/float(recoverday)*(1-buff))*float(infect[i]))
    maxinfect=float(amount*(1-buff))
    maxinfect=(math.ceil(maxinfect*10.0)/10.0)
    if i<recoverday:
        if maxinfect>=int(infect[i]+spreadnum):
            infect_people.append(int(spreadnum))
            infect.append(int(infect[i]+spreadnum))
            recovernum.append(0)
            total+=infect_people[i]
        else:
            infect_people.append(int(maxinfect-infect[i]))
            infect.append(int(maxinfect))
            recovernum.append(0)
            total+=infect_people[i]
    else:
        if maxinfect>float(infect[i]+spreadnum):
            infect_people.append(int(spreadnum))
            infect.append(int(infect[i]+spreadnum-infect_people[i-recoverday+1]))
            recovernum.append(infect_people[i-recoverday+1])
            buff+=infect_people[i-recoverday+1]/amount
            total+=infect_people[i]
        else:
            infect_people.append(int(maxinfect-infect[i]))
            infect.append(int(maxinfect-infect_people[i-recoverday+1]))
            recovernum.append(infect_people[i-recoverday+1])
            buff+=infect_people[i-recoverday+1]/amount
            total+=infect_people[i]
print(total)
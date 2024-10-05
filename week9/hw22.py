def fail():
    print('Error input')
    exit()

num=int(input())
if num<2 or num>5:
    print('Error input')
    exit()

card_str=[]
numName=[]

cardNum_1=[]
cardNum_2=[]
cardNum_3=[]
cardNum_4=[]

cardColor=[]
saveForNum=[[0 for i in range(0)] for j in range(num)]
card=[[0 for i in range(0)] for j in range(num)]
cardtemp=[[0 for i in range(0)] for j in range(num)]
cardNum= [[0 for i in range(0)] for j in range(num)]
cardColor=[[0 for i in range(0)] for j in range(num)]

for i in range(0,num,1):
    card_str=input()
    cardtemp[i]=(card_str.split(" "))
    for j in range(0,6,1):
        if j==0:
            numName.append(cardtemp[i][0])
        else:
            card[i].append(cardtemp[i][j])

temp=[0,0,0,0,0]
constant=[0,0,0,0,0]
samecolor=[0,0,0,0,0]
sameCard=[0,0,0,0,0]
countForPair=[0,0,0,0,0]
sameCardForPair=[5,5,5,5,5]
result=[0,0,0,0,0]
rank=[0,0,0,0,0]
flag=0

for i in range(0,num,1):
    for j in range(0,5,1):
        if len(card[i][j])==2:
            cardNum[i].append(card[i][j][0])
            cardColor[i].append(card[i][j][1])
        elif len(card[i][j])==3:
            if card[i][j][0]=='1' and card[i][j][1]=='0':
                cardNum[i].append('10')
                cardColor[i].append(card[i][j][2]) 
            else:
                fail()
        else:
            fail()

for i in range(0,num,1):
    for j in range(0,5,1):
        if cardNum[i][j]=='10' or 49<ord(cardNum[i][j])<58 or cardNum[i][j]=='A' or cardNum[i][j]=='J' or cardNum[i][j]=='Q' or cardNum[i][j]=='K':
            pass
        else:
            fail()
        if cardColor[i][j]=='S' or cardColor[i][j]=='H' or cardColor[i][j]=='D' or cardColor[i][j]=='C':
            pass
        else:
            fail()              
        for k in range(0,5,1):
            if cardNum[i][j]==cardNum[i-1][k] and cardColor[i][j]==cardColor[i-1][k]:
                flag=1
if flag==1:
    print('Duplicate deal')
    exit()     
for i in range(0,num,1):
    for j in range(0,5,1):
        if cardNum[i][j]=='A':
            cardNum[i][j]='1' 
        if cardNum[i][j]=='J':
            cardNum[i][j]='11'
        if cardNum[i][j]=='Q':
            cardNum[i][j]='12'
        if cardNum[i][j]=='K':
            cardNum[i][j]='13'
        cardNum[i][j]=int(cardNum[i][j])
    cardNum[i].sort()


for i in range(0,num,1):
    if cardColor[i][0]==cardColor[i][1]==cardColor[i][2]==cardColor[i][3]==cardColor[i][4]:
        samecolor[i]=1
    if cardNum[i][0]==1 and cardNum[i][4]==13:
        for j in range(0,5,1):
            if cardNum[i][j]<5:
                saveForNum[i].append(int(int(cardNum[i][j])+13))
            else:
                saveForNum[i].append(int(cardNum[i][j]))
            saveForNum[i].sort()

for i in range(0,num,1):
    for j in range(1,5,1):
        if cardNum[i][0]==1 and cardNum[i][4]==13:
            if (saveForNum[i][j]-saveForNum[i][j-1])==1:
                constant[i]+=1
        else:
            if (cardNum[i][j]-cardNum[i][j-1])==1:
                constant[i]+=1
for i in range(0,num,1):
    for j in cardNum[i]:
        if(sameCard[i]<cardNum[i].count(j)):
            sameCard[i]=cardNum[i].count(j)
        if(cardNum[i].count(j)==2 and temp[i]<j):
            temp[i]=j
            countForPair[i]+=1
    if constant[i]==4 and samecolor[i]==1:
        result[i]=9
    elif sameCard[i]==4:
        result[i]=8
    elif sameCard[i]==3 and sameCardForPair[i]==2:
        result[i]=7
    elif samecolor[i]==1:
        result[i]=6
    elif constant[i]==4:
        result[i]=5
    elif sameCard[i]==3:
        result[i]=4
    elif countForPair[i]==2:
        result[i]=3
    elif countForPair[i]==1:
        result[i]=2
    else:
        result[i]=1

for i in range (0,num):
    for j in range (0,num):
        if i==j:
            pass
        elif result[i]>result[j]:
             rank[i]+=1
for i in range(num,-1,-1):
    for j in range(0,num):
        if rank[j]==i:
            print(numName[j],result[j])
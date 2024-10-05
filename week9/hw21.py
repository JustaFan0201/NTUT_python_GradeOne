def fail():
    print('Error input')
    exit()
card_str=input()
card=card_str.split(" ")

cardNum=[]
cardColor=[]
saveForNum=[]

flag=1
constant=0
samecolor=0
sameCard=0
countForPair=0
sameCardForPair=5

temp=0
for i in range(0,len(card),1):
    if len(card[i])==2:
        cardNum.append(card[i][0])
        cardColor.append(card[i][1])
    elif len(card[i])==3:
        if card[i][0]=='1' and card[i][1]=='0':
            cardNum.append('10')
            cardColor.append(card[i][2]) 
        else:
            fail()
    else:
        fail()

for i in range(0,len(card),1):
    if cardNum[i]=='10' or 49<ord(cardNum[i])<58 or cardNum[i]=='A' or cardNum[i]=='J' or cardNum[i]=='Q' or cardNum[i]=='K':
        pass
    else:
        fail()
    if cardColor[i]=='S' or cardColor[i]=='H' or cardColor[i]=='D' or cardColor[i]=='C':
        pass
    else:
        fail()
    for j in range(0,len(card),1):
        if i==j:
            pass
        elif cardNum[i]==cardNum[j] and cardColor[i]==cardColor[j]:
            print('Duplicate deal')
            exit()
for i in range(0,len(cardNum),1):
    if cardNum[i]=='A':
        cardNum[i]='1' 
    if cardNum[i]=='J':
        cardNum[i]='11'
    if cardNum[i]=='Q':
        cardNum[i]='12'
    if cardNum[i]=='K':
        cardNum[i]='13'
    cardNum[i]=int(cardNum[i])
cardNum.sort()

if cardColor[0]==cardColor[1]==cardColor[2]==cardColor[3]==cardColor[4]:
    samecolor=1

if cardNum[0]==1 and cardNum[4]==13:
    for i in range(0,len(cardNum),1):
        if cardNum[i]<5:
            saveForNum.append(int(int(cardNum[i])+13))
        else:
                saveForNum.append(int(cardNum[i]))
        saveForNum.sort()
for i in range(1,len(cardNum),1):
    if cardNum[0]==1 and cardNum[4]==13:
        if (saveForNum[i]-saveForNum[i-1])==1:
            constant+=1
    else:
        if (cardNum[i]-cardNum[i-1])==1:
            constant+=1
for i in cardNum:
    if(sameCard<cardNum.count(i)):
        sameCard=cardNum.count(i)
    if(cardNum.count(i)==2) and temp<i:
        temp=i
        sameCardForPair=2
        countForPair+=1
if constant==4 and samecolor==1:
    print('9')
elif sameCard==4:
    print('8')
elif sameCard==3 and sameCardForPair==2:
    print('7')
elif samecolor==1:
    print('6')
elif constant==4:
    print('5')
elif sameCard==3:
    print('4')
elif countForPair==2:
    print('3')
elif countForPair==1:
    print('2')
else:
    print('1')

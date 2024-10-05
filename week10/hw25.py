def Error_input():
    print('Error input')
    exit()
def Color(Card):
    temp=[]
    ColorLib=['S','H','D','C']  
    for i in range (0,len(Card)):
        if Card[i][0] in ColorLib:
            temp.append(Card[i][0])
        else:
            Error_input()
    return temp
def Num(Card):
    temp=[]
    CardLib=[1,2,3,4,5,6,7,8,9,10,11,12,13] 
    for i in range (0,len(Card)):
        if len(Card[i])==2:
            temp.append(Card[i][1])
        elif len(Card[i])==3 and Card[i][1]=='1' and Card[i][2]=='0':
            temp.append(10)
        else:
            Error_input()
        if temp[i]=='A':
            temp[i]=1
        elif temp[i]=='J':
            temp[i]=11
        elif temp[i]=='Q':
            temp[i]=12
        elif temp[i]=='K':
            temp[i]=13
        else:
            temp[i]=int(temp[i]) 
    for i in range (0,len(temp)):
        if temp[i] in CardLib:
            pass
        else:
            Error_input()
    return temp
def check(player_Num,public_Num,player_Color,public_Color):
    ColorLib=['S','H','D','C']
    combinCard=player_Num+public_Num
    combinColor=player_Color+public_Color
    tempCard=[]
    tempColor=[]
    biggest=0
    for i in range(0,6):
        samecolor=0
        twopair=0
        threekind=0
        fourkind=0
        stright=0
        lastone=0
        result=0
        tempCard.clear()
        tempColor.clear()
        for j in range(0,5):
            tempCard.append(combinCard[i-j])
            tempColor.append(combinColor[i-j])
        tempCard.sort()
        for k in ColorLib:
            if tempColor.count(k)==5:
                samecolor=1
        if tempCard[0]==1 and tempCard[4]==13:
            for l in range(0,5):
                if tempCard[l]<5:
                    tempCard[l]=tempCard[l]+13
        tempCard.sort()
        for l in range(1,5):
            if tempCard[l]==tempCard[l-1]+1:
                stright+=1

        for l in tempCard:
            if tempCard.count(l)==4:
                fourkind=1
            elif tempCard.count(l)==3:
                threekind=1
            if tempCard.count(l)==2 and l!=lastone:
                lastone=l
                twopair+=1
        if samecolor==1 and stright==4:
            result=9
        elif fourkind==1:
            result=8
        elif threekind==1 and twopair==1:
            result=7
        elif samecolor==1:
            result=6
        elif stright==4:
            result=5  
        elif threekind==1:
            result=4
        elif twopair==2:
            result=3 
        elif twopair==1:
            result=2   
        else:
            result=1
        if result>biggest:
            biggest=result
    return biggest
playerOne=input().split(" ")
palyerTwo=input().split(" ")
public=input().split(" ")
playerOne_Color=Color(playerOne)
playerTwo_Color=Color(palyerTwo)
public_Color=Color(public)
playerOne_Num=Num(playerOne)
playerTwo_Num=Num(palyerTwo)
public_Num=Num(public)
record=[]
all=playerOne+palyerTwo+public
for i in range(0,len(all)):
    if all[i] not in record:
        record.append(all[i])
    else:
        print('Duplicate deal')
        exit()
result_one=check(playerOne_Num,public_Num,playerOne_Color,public_Color)
result_two=check(playerTwo_Num,public_Num,playerTwo_Color,public_Color)
if result_one>result_two:
    print("A "+str(result_one))
elif result_one==result_two:
    print("Tie")
else:
    print("B "+str(result_two))
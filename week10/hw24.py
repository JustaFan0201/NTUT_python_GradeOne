def fix_num(playerNum,CardForPlayer):
    additional_add=["J","Q","K"]
    for i in range (0,playerNum):
        if CardForPlayer[i]=="A":
            CardForPlayer[i]=1.0
        if CardForPlayer[i] in additional_add:
            CardForPlayer[i]=0.5
    return CardForPlayer
def small_card(playerNum,CardForPlayer,perfectCard):
    small=99.0
    for i in range(0,playerNum):
        if i not in perfectCard and small>CardForPlayer[i]:
            small=CardForPlayer[i]
    return small

playerNum=int(input())
PlayerMoney = input().split(" ")
CardForPlayer = input().split(" ")
CardForComputer=[]
CardForaddComputer=['0']
CardForComputer.append(CardForPlayer[0])
CardForPlayer.pop(0)

TotalMoneyPlayer=[0,0,0,0,0,0,0,0,0,0,0,0]
TotalMoneyComputer=0

CardForPlayer=fix_num(playerNum,CardForPlayer)
CardForComputer=fix_num(1,CardForComputer)
CardForComputer[0]=float(CardForComputer[0])

smallest=0
bombCard=[]
perfectCard=[]
additional_add=["J","Q","K"]

count=0
while(count<playerNum):
    Request = input().split(" ")
    CardForPlayer[count]=float(CardForPlayer[count])
    if Request[0]=="Y":
        if Request[1] in additional_add:
            CardForPlayer[count]+=float(0.5)
        elif Request[1]=="A":
            CardForPlayer[count]+=float(1.0)
        else:
            CardForPlayer[count]+=float(Request[1])
        if CardForPlayer[count]>10.5:
            bombCard.append(count)
            TotalMoneyPlayer[count]=('-'+str(PlayerMoney[count]))
            TotalMoneyComputer+=int(PlayerMoney[count])
            count+=1
        elif CardForPlayer[count]==10.5:
            bombCard.append(count)
            perfectCard.append(count)
            TotalMoneyPlayer[count]=('+'+str(PlayerMoney[count]))
            TotalMoneyComputer-=int(PlayerMoney[count])
            count+=1
    else:
        count+=1
smallest=small_card(playerNum,CardForPlayer,perfectCard)

while(smallest>=CardForComputer[0] and len(bombCard)!=playerNum):
    CardForaddComputer[0]=input()
    CardForaddComputer=fix_num(1,CardForaddComputer)
    CardForComputer[0]+=float(CardForaddComputer[0])
    if CardForComputer[0]>10.5:
        for i in range (0,playerNum):
            if i in bombCard:
                pass
            else:
                TotalMoneyPlayer[i]=('+'+str(PlayerMoney[i]))
                TotalMoneyComputer-=int(PlayerMoney[i])
                bombCard.append(i)
        CardForComputer[0]=0
        break
    elif CardForComputer[0]==10.5:
        for i in range (0,playerNum):
            if i in bombCard:
                pass
            else:
                TotalMoneyPlayer[i]=('-'+str(PlayerMoney[i]))
                TotalMoneyComputer+=int(PlayerMoney[i])
                bombCard.append(i)
        break
for i in range(0,playerNum):
    if i not in bombCard and len(bombCard)!=playerNum:
        if CardForComputer[0]>=CardForPlayer[i]:
            TotalMoneyComputer+=int(PlayerMoney[i])
            TotalMoneyPlayer[i]=('-'+str(PlayerMoney[i]))
        else:
            TotalMoneyComputer-=int(PlayerMoney[i])
            TotalMoneyPlayer[i]=('+'+str(PlayerMoney[i]))
for i in range(0,playerNum):
    print('Player'+str(i+1)+' ',end='')
    print(TotalMoneyPlayer[i])
if TotalMoneyComputer>=0:
    print('Computer +'+str(TotalMoneyComputer))
else:
    print('Computer '+str(TotalMoneyComputer))
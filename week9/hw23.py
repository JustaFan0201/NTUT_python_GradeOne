choose='Y'
card_player=[]
card_computer=[]
Total_player=0
Total_computer=0
i=0
j=0
judge=0
while(choose=='Y' or ((Total_computer<=8 or Total_computer<Total_player)and judge==0)):
    if choose=='Y':
        card_player.append(input())
        if card_player[i]=='A':
            card_player[i]='1' 
        if card_player[i]=='J':
            card_player[i]='0.5'
        if card_player[i]=='Q':
            card_player[i]='0.5'
        if card_player[i]=='K':
            card_player[i]='0.5'
        card_player[i]=float(card_player[i])
        Total_player+=card_player[i]
    if Total_player>10.5:
        print('computer win')
        exit()
    i+=1

    if (Total_computer<=8 or Total_computer<Total_player)and judge==0:
        card_computer.append(input())
        if card_computer[j]=='A':
            card_computer[j]='1' 
        if card_computer[j]=='J':
            card_computer[j]='0.5'
        if card_computer[j]=='Q':
            card_computer[j]='0.5'
        if card_computer[j]=='K':
            card_computer[j]='0.5'
        card_computer[j]=float(card_computer[j])
        Total_computer+=card_computer[j]
        if Total_computer>10.5:
            print('player win')
            exit()
    else:
        judge=1
    j+=1
    if(choose=='Y'): 
        choose=input()
    


if Total_computer==Total_player:
    print('it\'s a tie')
elif Total_computer<Total_player:
    print('player win')
else:
    print('computer win')
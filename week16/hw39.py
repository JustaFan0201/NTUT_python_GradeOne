def battle(playerOne,playerTwo,squ_num,choose):
    lineOne=0
    lineTwo=0
    for i in range(squ_num):
        countOne=0
        countTwo=0
        for j in range(squ_num):
            if playerOne[squ_num*i+j] in choose:
                countOne+=1
            if playerTwo[squ_num*i+j] in choose:
                countTwo+=1
        if countOne==squ_num:
            lineOne+=1
        if countTwo==squ_num:
            lineTwo+=1
    for i in range(squ_num):
        countOne=0
        countTwo=0
        for j in range(squ_num):
            if playerOne[i+squ_num*j] in choose:
                countOne+=1
            if playerTwo[i+squ_num*j] in choose:
                countTwo+=1
        if countOne==squ_num:
            lineOne+=1
        if countTwo==squ_num:
            lineTwo+=1
    countOne=0
    countTwo=0
    for j in range(squ_num):
        if playerOne[(squ_num+1)*j] in choose:
            countOne+=1
        if playerTwo[(squ_num+1)*j] in choose:
            countTwo+=1
    if countOne==squ_num:
            lineOne+=1
    if countTwo==squ_num:
        lineTwo+=1
    countOne=0
    countTwo=0
    for j in range(squ_num):
        if playerOne[(squ_num-1)*j] in choose:
            countOne+=1
        if playerTwo[(squ_num-1)*j] in choose:
            countTwo+=1
    if countOne==squ_num:
            lineOne+=1
    if countTwo==squ_num:
        lineTwo+=1

    if lineOne>lineTwo:
        return "A Win"
    elif lineOne<lineTwo:
        return "B Win"
    else:
        return "Tie"
squ_num=int(input())
chooseNum=int(input())
playerOne=input().split(" ")
playerTwo=input().split(" ")
choose=input().split(" ")
result=battle(playerOne,playerTwo,squ_num,choose)
print(result)
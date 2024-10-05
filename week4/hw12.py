point=[0,0.5,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
name1=input()
card1=[]
card1.append(input())
card1.append(input())
card1.append(input())
total1=float(0)

name2=input()
card2=[]
card2.append(input())
card2.append(input())
card2.append(input())
total2=float(0)
for i in range(0,3,1):
    if card1[i]=="A":
        card1[i]="1"
    if card2[i]=="A":
        card2[i]="1"
    if card1[i]=="J":
        card1[i]="11"
    if card2[i]=="J":
        card2[i]="11"
    if card1[i]=="Q":
        card1[i]="12"
    if card2[i]=="Q":
        card2[i]="12"
    if card1[i]=="K":
        card1[i]="13"
    if card2[i]=="K":
        card2[i]="13"

for i in range(1,len(point),1):
    if i==float(card1[0]):
        total1+=float(point[i])
    if i==float(card1[1]):
        total1+=float(point[i])
    if i==float(card1[2]):
        total1+=float(point[i])

    if i==float(card2[0]):
        total2+=float(point[i])
    if i==float(card2[1]):
        total2+=float(point[i])
    if i==float(card2[2]):
        total2+=float(point[i])

if total1>10.5:
    total1=0
if total2>10.5:
    total2=0
if total1==0:
    print(name2+" Win")
elif total1==total2:
    print("Tie")
elif total1>total2:
    print(name1+" Win")
else:
    print(name2+" Win")


if total1==total2:
    print("Tie")
elif total1>total2:
    print(name1+" Win")
else:
    print(name2+" Win")
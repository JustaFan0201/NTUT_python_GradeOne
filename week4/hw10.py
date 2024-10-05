first_ball=[]
second_ball=[]
flag2=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
flag1=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
sp_num=[]
sum=int(0)
for i in range(0,2):
    first_ball.append(int(input()))
    if i==1:
        if first_ball[i]==10:
            sp_num.append(int(input()))
            sp_num.append(int(input()))
            second_ball.append(int(0))
        else:
            second_ball.append(int(input()))
            if second_ball[i]+first_ball[i]==10:
                sp_num.append(int(input()))
            else:
                pass

    elif first_ball[i]==10:
        second_ball.append(int(0))
        flag2.insert(i ,int(i))                                
    else: 
        second_ball.append(int(input()))
        if int(second_ball[i])+int(first_ball[i])==10:
            flag1.insert(i ,int(i))
        else:
            pass
for i in range(0,2):
    sum=sum+int(first_ball[i])+int(second_ball[i])
    if flag2[i]==i:
        if second_ball[i+1]!=0:
            sum=sum+int(first_ball[i+1])+int(second_ball[i+1])
        elif i==(len(first_ball))-2:
            sum=sum+int(first_ball[i+1])+sp_num[0]
        else:
            sum=sum+int(first_ball[i+1])+int(first_ball[i+2])
    elif flag1[i]==i:
        sum=sum+int(first_ball[i+1])
if len(sp_num)==0:
    pass
elif len(sp_num)==1:
    sum=sum+sp_num[0]
else:
    sum=sum+sp_num[1]+sp_num[0]
print(sum)
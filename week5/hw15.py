import math
def bmi(w:float,h=0):
    if h!=0:
        bmi=w/h/h
    else:
        bmi=w
    bmi=(math.floor(bmi*1000)/1000.0)
    beta_str=str(int(bmi*1000))

    if beta_str[len(beta_str)-1]=='5':
        beta_bmi=(math.floor(bmi*100)/100.0)
        if beta_bmi*100%2==0:
            bmi=(math.floor(bmi*100)/100.0)
        else:
            bmi=(math.ceil(bmi*100)/100.0)
    else:
        bmi=round(bmi,2)
    bmi=math.floor(bmi*100)/100.0
    return bmi

data=[]
total=[]
count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
data=[]
num=int(input())
for i in range(num):
    data.append(input())
    data[i]=data[i].split(" ",-1)
    h=float(data[i][0])
    w=float(data[i][1])        
    total.append(bmi(w,h))

print("%.2f"%max(total))
print("%.2f"%min(total))
total.sort()
if len(total)%2==0:
    leng=int(len(total)/2)
    save=bmi((total[leng]+total[leng-1])/2.0)
    print("%.2f"%save)
else:
    leng=int(len(total)/2)
    save=bmi((total[leng]))
    print("%.2f"%save)

for i in range(0,len(total)):
    if total[i]==total[i-1]:
        data.append(total[i])
        count[i]+=1
    else:
        data.append(total[i])
        count[i]+=1
temp=0
for i in total:
    if(temp<total.count(i)):
        a=i
        temp=total.count(i)
save=bmi(a)
print(a)
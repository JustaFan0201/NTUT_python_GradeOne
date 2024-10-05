class_id=[]
hours=[]
class_time=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
record1=[]
record2=[]
record3=[]
flag=1
save1=[]
save2=[]
save3=[]
num=int(input())
if num>10 and num<2:
    flag=0
for i in range (num):
    class_id.append(input())
    hours.append(int(input()))
    for j in range (hours[i]):
        class_time[i][j]=input()
        sh=class_time[i][j]
        if 1<=int(sh[0])<=5 and (57>=int(ord(sh[1]))>=49 or 97<=int(ord(sh[1]))<=99):
            pass
        else:
            flag=0;

for i in range (len(hours)):
    for j in range (len(hours)):
        if i==j:
            pass
        else:    
            for k in range(hours[j]):
                if class_time[i][0]==class_time[j][k]:
                    record1.append(class_id[i])
                    record2.append(class_id[j])
                    record3.append(class_time[i][0])
                if class_time[i][1]==class_time[j][k]:
                    record1.append(class_id[i])
                    record2.append(class_id[j])
                    record3.append(class_time[i][1])   
                if class_time[i][2]==class_time[j][k]:
                    record1.append(class_id[i])
                    record2.append(class_id[j])
                    record3.append(class_time[i][2])

for i in range(len(record3)):
    for j in range(len(record3)):
        if i==j:
            pass
        else:
            if record1[i]==record2[j] and record2[i]==record1[j] and record3[i]==record3[j]:
                record1[j]="A"
                record2[j]="A"
                record3[j]="A"

if flag==0:
    print('-1')  
elif flag==1 and len(record1)==0:
    print('correct')
else:
    for i in range (len(record3)):
        if record1[i]=="A":
            pass
        else:
            print(record1[i] + ',' + record2[i] + ',' + record3[i])

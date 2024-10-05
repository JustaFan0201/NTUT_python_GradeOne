class_id=[]
hours=[]
class_time1=[]
class_time2=[]
class_time3=[]
record1=[]
record2=[]
record3=[]
flag=1
for i in range (3):
    class_id.append(input())
    hours.append(int(input()))
    for j in range (hours[i]):
        if(i==0):
            class_time1.append((input()))
            sh=class_time1[j]
            if 1<=int(sh[0])<=5 and (57>=int(ord(sh[1]))>=49 or 97<=int(ord(sh[1]))<=99):
                pass
            else:
                flag=0;
                
        elif(i==1):
            class_time2.append((input()))
            sh=class_time2[j]
            if 1<=int(sh[0])<=5 and (57>=int(ord(sh[1]))>=49 or 97<=int(ord(sh[1]))<=99):
                pass
            else:
                flag=0;

        elif(i==2):
            class_time3.append((input()))
            sh=class_time3[j]
            if 1<=int(sh[0])<=5 and (57>=int(ord(sh[1]))>=49 or 97<=int(ord(sh[1]))<=99):
                pass
            else:
                flag=0;
                

for i in range (hours[0]):
    for j in range (hours[1]):
        if class_time1[i]==class_time2[j]:
            record1.append(class_id[0])
            record2.append(class_id[1])
            record3.append(class_time1[i])
            
for i in range (hours[0]):
    for j in range (hours[2]):
        if class_time1[i]==class_time3[j]:
            record1.append(class_id[0])
            record2.append(class_id[2])
            record3.append(class_time1[i])
            
for i in range (hours[1]):
    for j in range (hours[2]):
        if class_time2[i]==class_time3[j]:
            record1.append(class_id[1])
            record2.append(class_id[2])
            record3.append(class_time2[i])
if flag==0:
    print('-1')  
elif flag==1 and len(record1)==0:
    print('correct')
else:
    for i in range (len(record3)):
        print(record1[i] + ',' + record2[i] + ',' + record3[i])

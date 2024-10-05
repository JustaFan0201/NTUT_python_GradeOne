import math    
c=0    
total=[]
check=[]
compare=[99,99,99]
result=[[""for i in range(8)]for j in range(3)]
num=int(input())
for i in range(num):
    temp=input().split(" ")
    total.append(temp)
    for j in range(4):
        total[i][j]=int(total[i][j])
for i in range(num):
    for j in range(num):
        d=math.sqrt((total[i][1]-total[j][1])**2 + (total[i][2]-total[j][2])**2 + (total[i][3]-total[j][3])**2 )
        if i!=j and [j,i] not in check and [i,j] not in check:
            check.append([i,j])
            if d<compare[0]:
                c+=1
                if c>2:
                    compare[2]=compare[1]
                    for k in range(0,8):
                        result[2][k]=result[1][k]
                if c>1:
                    compare[1]=compare[0]
                    for k in range(0,8):
                        result[1][k]=result[0][k]
                if c>0:
                    compare[0]=d
                    result[0][0]=i+1
                    result[0][1]=j+1
                    for k in range(1,4):
                        result[0][k+1]=total[i][k]
                        result[0][k+4]=total[j][k]
            elif compare[0]<=d<compare[1] :
                compare[2]=compare[1]
                for k in range(0,8):
                    result[2][k]=result[1][k]

                compare[1]=d
                result[1][0]=i+1
                result[1][1]=j+1
                for k in range(1,4):
                    result[1][k+1]=total[i][k]
                    result[1][k+4]=total[j][k]
                
            elif compare[1]<=d<compare[2] :
                check[1]=d
                compare[2]=d
                result[2][0]=i+1
                result[2][1]=j+1
                for k in range(1,4):
                    result[2][k+1]=total[i][k]
                    result[2][k+4]=total[j][k]
for i in range(3):
    for j in range(8):
        if j!=7:
            print(result[i][j],end=" ")
        else:
            print(result[i][j])
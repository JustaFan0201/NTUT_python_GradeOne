def show(total):
    for j in range(16):
        if j%4==3:
            print(total[j])
        else:
            print(total[j],end=" ")
def sol(total,i,sum):
    for j in range(4):
        if total[4*i+j]=="0":
            total[4*i+j]=str(sum)
            return total
def sol2(total,i,sum):
    for j in range(4):
        if total[i+4*j]=="0":
            total[i+4*j]=str(sum)
            return total
def sol3(total,i,sum):
    for j in range(2):
        if total[8*i+j]=="0":
            total[8*i+j]=str(sum)
            return total
    for j in range(2):
        if total[8*i+4+j] =="0":
            total[8*i+4+j]=str(sum)
            return total
def sol4(total,i,sum):
    for j in range(2):
        if total[8*i+2+j] =="0":
            total[8*i+2+j] = str(sum)
            return total
    for j in range(2):
        if total[8*i+6+j] =="0":
            total[8*i+6+j] = str(sum)
            return total
total=[]
lib=["1","2","3","4"]
count=0
fail=0
for i in range(4):
    temp=input().split(" ")
    total+=temp
    temp.clear()
i=0
sum=10
while(i<4):
    for j in range(4):
        if total[4*i+j] in lib:
            sum-=int(total[4*i+j])
            count+=1
    if count==3:
        total=sol(total,i,sum)
        fail=1
    sum=10
    count=0

    for j in range(4):
        if total[i+4*j] in lib:
            sum-=int(total[i+4*j])
            count+=1
    if count==3:
        total=sol2(total,i,sum)
        fail=1
    sum=10
    count=0

    if i<2:
        for j in range(2):
            if total[8*i+j] in lib:
                sum-=int(total[8*i+j])
                count+=1
        for j in range(2):
            if total[8*i+4+j] in lib:
                sum-=int(total[8*i+4+j])
                count+=1
        if count==3:
            total=sol3(total,i,sum)
            fail=1
        sum=10
        count=0

        for j in range(2):
            if total[8*i+2+j] in lib:
                sum-=int(total[8*i+2+j])
                count+=1
        for j in range(2):
            if total[8*i+6+j] in lib:
                sum-=int(total[8*i+6+j])
                count+=1
        if count==3:
            total=sol4(total,i,sum)
            fail=1
        sum=10
        count=0

    if fail==1:
        i=0
        fail=0
    else:
        i+=1
show(total)
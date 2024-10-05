import math
def perRank(people):
    perResult=[]
    perRank=0
    i,j=1,1
    num=3
    if people<=2:
        num=people
    while(len(perResult)<num):
        perRank=math.ceil(j/100*people)
        if perRank>=i:
            perResult+=[str(j)+"%"]
            i+=1
        j+=1
    return perResult
def totalRank(data:dict,className,StudentYearName,ClassYear,ClassNumForStudent,GiveupYearPeople):
    result={}
    point={}
    people=0
    giveup={}
    for i in data.keys():
        if i[4:7]==ClassYear:
            classdata=dict(data[i])
            for j,studentGrade in classdata.items():
                if j[3:6]==className and j[0:3]==StudentYearName:
                    if studentGrade=="w":
                        if j not in giveup:
                            people+=1
                            giveup[j]=1
                        else:
                            giveup[j]+=1
                    else:
                        if j not in result:
                            giveup[j]=0
                            people+=1
                            result[j]=studentGrade*int(i[3])
                            point[j]=int(i[3])
                        else:
                            result[j]+=studentGrade*int(i[3])
                            point[j]+=int(i[3])
    if len(result)==0:
        return 0
    for i in result.keys():
        result[i]=math.floor(result[i]/point[i])
    result=dict(sorted(result.items(),key=lambda x:x,reverse=0))
    result=dict(sorted(result.items(),key=lambda x:x[1],reverse=1))
    perResult=perRank(people)
    print(className,StudentYearName,ClassYear)
    c=0
    for i in result.keys():
        if c>2:
            break
        print(i,result[i],perResult[c],str(math.floor(100*(float(GiveupYearPeople[ClassYear][i])/float(ClassNumForStudent[ClassYear][i]))))+"%")
        c+=1

    return 0

def totalclass(data:dict,ClassYearName,ClassYear,choose):
    result={}
    people=0
    giveup=0
    TotalScore=0
    classNum=0
    high=[]
    low=""
    for i in data.keys():
        if i[0:4]==ClassYearName and i[4:7]==ClassYear:
            classNum+=1
            classdata=dict(data[i])
            for j,studentGrade in classdata.items():
                if studentGrade=="w":
                    giveup+=1
                else:
                    if j not in result:
                        people+=1
                        result[j]=studentGrade
                    else:
                        result[j]+=studentGrade
                    TotalScore+=studentGrade
    if classNum==0:
        return {}
    print(ClassYearName,ClassYear)
    result=dict(sorted(result.items(),key=lambda x:(x[1],x),reverse=0))
    for i in result.keys():
        low=i
        break
    result=dict(sorted(result.items(),key=lambda x:x,reverse=0))
    result=dict(sorted(result.items(),key=lambda x:x[1],reverse=1))
    c=0
    for i in result.keys():   
        if c>1:
            break
        high+=[i]
        c+=1

    print(result[high[0]],TotalScore//people,result[low],str((math.floor((float(giveup))/float(people+giveup)*100)))+"%")
    perResult=perRank(people+giveup)

    c=0
    for i in result.keys():
        if c>2:
            break
        print(i,result[i],perResult[c])
        c+=1
    if ClassYearName==choose:
        thisyear={high[0]:result[high[0]],high[1]:result[high[1]]}
        return thisyear
    else:
        return {}


classnum=int(input())
data={}
specail=["101","201"]
className=[]
StudentYearName=[]
ClassYearName=[]
ClassYear=[]
ClassNumForStudent={}
GiveupYearPeople={}
yearRank={}
studentNum={}
for i in range(classnum):
    classdata=input().split(" ")
    classinfo=classdata[0]+classdata[1]
    data[classinfo]={}
    if classdata[0] not in ClassYearName:
        ClassYearName+=[classdata[0]]
    if classdata[1][0:3] not in ClassYear:
        ClassYear+=[classdata[1][0:3]]

    if classdata[1][0:3] not in ClassNumForStudent:
        ClassNumForStudent[classdata[1][0:3]]={}
    if classdata[1][0:3] not in GiveupYearPeople:
        GiveupYearPeople[classdata[1][0:3]]={}
    for j in range(int(classdata[2])):
        info=input().split(" ")

        Temp=ClassNumForStudent[classdata[1][0:3]]
        TempForLosser=GiveupYearPeople[classdata[1][0:3]]
        if info[1]=="w":
            if info[0] not in TempForLosser:
                GiveupYearPeople[classdata[1][0:3]][info[0]]=1
            else:
                GiveupYearPeople[classdata[1][0:3]][info[0]]+=1
        else:
            if info[0] not in TempForLosser:
                GiveupYearPeople[classdata[1][0:3]][info[0]]=0
        if info[0] not in Temp:
            ClassNumForStudent[classdata[1][0:3]][info[0]]=1
        else:
            ClassNumForStudent[classdata[1][0:3]][info[0]]+=1

        if info[0][3:6] not in className:
            className+=[info[0][3:6]]
        if info[0][0:3] not in StudentYearName:
            StudentYearName+=[info[0][0:3]]

        if info[0][3:6] not in studentNum:
            studentNum[info[0][3:6]]={}
        studentNum[info[0][3:6]][info[0][6:8]]=info[0][6:8]
        
        if info[1]=="w":
            studentinfo,score=info
        elif classinfo[0:3] in specail:
            studentinfo,score1,score2=info
            score=math.ceil((0.7*int(score1)+0.3*int(score2)))
        else:
            studentinfo,score=info
            score=int(score)
        data[classinfo][studentinfo]=score
choose=input()
className=sorted(className,key=lambda x:x)
StudentYearName=sorted(StudentYearName,key=lambda x:x)
ClassYearName=sorted(ClassYearName,key=lambda x:x)
ClassYear=sorted(ClassYear,key=lambda x:x)
for i in className:
    for j in StudentYearName: 
        for k in ClassYear:
            totalRank(data,i,j,k,ClassNumForStudent,GiveupYearPeople)
for i in ClassYearName:
    for j in ClassYear:
        temp=totalclass(data,i,j,choose)
        for k,value in temp.items():
            if k not in yearRank:
                yearRank[k]=value
            else:
                pass
yearRank=dict(sorted(yearRank.items(),key=lambda x:x,reverse=0))
yearRank=dict(sorted(yearRank.items(),key=lambda x:x[1],reverse=1))
c=0
for i in yearRank.keys():
    if c>1:
        break
    else:
        print(i,end=" ")
    c+=1
studentNum=dict(sorted(studentNum.items(),key=lambda x:len(x[1]),reverse=1))
c=0
for i in studentNum.keys():
    if c==1:
        print(i)
        break
    else:
        print(i,end=" ")
    c+=1

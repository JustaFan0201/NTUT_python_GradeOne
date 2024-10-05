def push(stack,data,top):
    stack[top+1]=data
    return top+1,stack
def pop(stack,top):
    stack[top]=0
    return top-1,stack
def sol(allstr):
    stack=[0 for i in range(30)]
    left=["(","{","["]
    right=[")","}","]"]
    top=-1
    for i in range(len(allstr)):
        if allstr[i] in left:
            top,stack=push(stack,allstr[i],top)
        elif allstr[i] in right:
            temp=stack[top]
            if allstr[i]==")" and stack[top]=="(":
                pass
            elif allstr[i]=="]" and stack[top]=="[":
                pass
            elif allstr[i]=="}" and stack[top]=="{":
                pass
            else:
                return "fail"
            top,stack=pop(stack,top)
    if stack[0]==0:
        return "pass"
    else:
        return "fail"

num=int(input())
deep=int(input())
nowdeep=0

left=["(","{","["]
right=[")","}","]"]
allstr=[]
temp_all=""
top=-1
temp_deepword=""
alldeepword=[]
for i in range(num):
    str_temp=input()
    for j in range(len(str_temp)):
        if str_temp[j] in left:
            nowdeep+=1
        elif str_temp[j] in right:
            nowdeep-=1
        if str_temp[j] in left or str_temp[j] in right:
            temp_all+=str_temp[j]
        if nowdeep==deep and str_temp[j]not in left and str_temp[j] not in right:
            temp_deepword+=str_temp[j]
    temp_all=sol(temp_all)
    allstr.append(temp_all)
    alldeepword.append(temp_deepword)
    temp_all=""
    temp_deepword=""
for i in range(num):
    if len(alldeepword[i])==0:
        alldeepword[i]="EMPTY"
    if allstr[i]=='pass':
        print(allstr[i],end=", ")
        print(alldeepword[i])
    else:
        print(allstr[i])
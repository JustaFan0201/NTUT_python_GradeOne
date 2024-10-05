def find_shortest_path(graph:dict, current:str, end:str, path=[],result=[]):
    path = path + [current]
    if current == end:
        return path
    for friend in graph[current]:
        if friend not in path:
            new_path = find_shortest_path(graph, friend, end, path,result)
            if new_path:
                if new_path not in [result]:
                    result+=[new_path]
    return result
tempData=input().split(" ")
num,start,end=tempData
rest=input().split(" ")
save={}
c=0
result=[]
passroad=[]
while(c<int(num)):
    temp=input().split(" ")
    if temp[0]=="-1":
        break
    else:
        p1,p2=temp
    if p1 not in save:
        save[p1]={}
    if p2 not in save:
        save[p2]={}
    save[p1][p2]=p2
    save[p2][p1]=p1
    c+=1
path = find_shortest_path(save, start, end)
for i in range(len(path)):
    if i==0:
        short=path[i]
    elif len(path[i])<len(short):
        short=path[i]
for i in range(len(rest)):
    for j in range(len(short)):
        if rest[i]==short[j] and rest[i] not in passroad:
            passroad+=rest[i]
if path:
    print(" ".join(passroad))
    print(" ".join(short))
else:
    print("NO")
import copy
def find_shortest_path(graph:dict, current:str, path=[],result=[]):
    if current == '0' or current in path:
        return path
    path+=[current]
    for friend in graph[current]:
        new_path= find_shortest_path(graph, friend,copy.copy(path),result)
        if new_path not in [result]:
            result+=[new_path]
    return result
tempData=[x for x in input().split(" ") if x!=""]
num,start=tempData
save={}
c=0
totalGold={}
while(c<int(num)):
    temp=[x for x in input().split(" ") if x!=""]
    main,gold,road1,road2=temp
    if main not in save:
        save[main]={}
    save[main][road1]=road1
    save[main][road2]=road2
    totalGold[main]=int(gold)
    c+=1
path = find_shortest_path(save, start)
for i in range(len(path)):
    temp=0
    for j in range (len(path[i])):
        temp+=totalGold[path[i][j]]
    if i==0:
        biggest=temp
    elif temp>biggest:
        biggest=temp
print(biggest)
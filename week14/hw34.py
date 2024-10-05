def find_path(graph, current, end, path=[],total=0):
    path = path + [current]
    if current == end:
        return path,path,total
    longest = None
    shortest=None
    result=None
    for friend in graph[current]:
        if friend not in path:
            new_path,new_path,new_total = find_path(graph, friend, end, path,total+graph[current][friend])
            if new_path:
                if longest is None or len(new_path) > len(longest):
                    longest = new_path
                    result= new_total
                if shortest is None or len(new_path) < len(shortest):
                    shortest = new_path
                    result= new_total
    return shortest,longest,result

num=input() 
save={}
Data=[]
c=0
d=0
while(1):
    temp=input().split(" ")
    if temp[0]=="-1":
        break
    else:
        p1,p2,familiar=temp
    Data.append([p1,p2,familiar])
    if p1 not in save:
        save[p1]={}
    if p2 not in save:
        save[p2]={}
    save[p1][p2]=int(familiar)
    c+=1
while(1):
    if d==len(Data):
        break
    p1=Data[d][0]
    p2=Data[d][1]
    if p1 in save[p2] and p2 in save[p1]:
        if save[p1][p2]>save[p2][p1]:
            save[p1][p2]=save[p2][p1]
    d+=1
shortest_path,longest_path,total = find_path(save, "A", "B")
layers = len(shortest_path) - 1
print(layers)
print(" ".join(shortest_path))
print(total)
print(" ".join(longest_path))

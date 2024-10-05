size=int(input())
rotate=input()
list_size=[]
new_list=[]
list_size.append(0)
new_list.append(0)
for i in range (1,size*size+1):
    list_size.append(i)
for i in range (0,len(rotate)):
    if rotate[i]=='L':
        for i in range(1,size+1):
            for j in range (1,size+1):
                new_list.append(list_size[j*size-i+1])
        for i in range (1,size*size+1):
            list_size[i]=new_list[i]  
        new_list.clear()
        new_list.append(0)
    elif rotate[i]=='R':
        for i in range (size,0,-1):
            for j in range (size,0,-1):
                new_list.append(list_size[j*size-i+1])
        for i in range (1,size*size+1):
            list_size[i]=new_list[i]
        new_list.clear()
        new_list.append(0)
for i in range (1,size*size+1):
    print(list_size[i],end='')
    if i%size!=0:
        print(' ',end='')
    else:
        print(end='\n')
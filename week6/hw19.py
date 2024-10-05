def triangle(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end='')
        for j in range(i,1,-1):
            print(j-1,end='')
        print('')
def right_triangle(num):
    for i in range(1,num+1):
        for j in range(num-i,0,-1):
            print('_',end='')
        for j in range(1,i+1):
            print(j,end='')
        for j in range(i,1,-1):
            print(j-1,end='')
        for j in range(num-i,0,-1):
            print('_',end='')
        print('')
def inverse_right_triangle(num):
    for i in range(1,num+1):
        for j in range(1,i):
            print('_',end='')
        for j in range(1,num+2-i):
            print(j,end='')
        for j in range(num-i,0,-1):
            print(j,end='')
        for j in range(1,i):
            print('_',end='')
        print('')

choose=int(input())
num=int(input())
if choose==1:
    triangle(num)
elif choose==2:
    right_triangle(num)
elif choose==3:
    inverse_right_triangle(num)

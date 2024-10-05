def triangle(num):
    for i in range(1,num+1):
        for j in range(num-i,0,-1):
            print('#',end='')
        for j in range(0,2*i-1):
            print('*',end='')
        for j in range(num-i,0,-1):
            print('#',end='')
        print('')
def inverse_triangle(num):
    for i in range(1,num+1):
        for j in range(1,i):
            print('#',end='')
        for j in range(2*num-i,i-1,-1):
            print('*',end='')
        for j in range(1,i):
            print('#',end='')
        print('')
def diamond(num):
    count=int((num+1)/2)
    for i in range(1,count+1):
        for j in range(count-i,0,-1):
            print(' ',end='')
        for j in range(0,2*i-1):
            print('*',end='')
        print('')
    for i in range(1,count):
        for j in range(0,i):
            print(' ',end='')
        for j in range(num-i-1,i-1,-1):
            print('*',end='')
        print('')
def fish(num):
    count=int((num+1)/2)
    for i in range(1,count+1):
        for j in range(count-i,0,-1):
            print(' ',end='')
        for j in range(0,2*i-1):
            print('*',end='')
        for j in range(num-2*i+1,0,-1):
            print(' ',end='')
        for j in range(0,i-1):
            print('-',end='')
        print('')
    for i in range(1,count):
        for j in range(0,i):
            print(' ',end='')
        for j in range(num-i-1,i-1,-1):
            print('*',end='')
        for j in range(0,2*i):
            print(' ',end='')
        for j in range(num-2*i-1,0,-2):
            print('-',end='')
        print('')
choose=int(input())
num=int(input())
if num%2==0 or num<=2 or num>=50:
    print('error')
elif choose==1:
    triangle(num)
elif choose==2:
    inverse_triangle(num)
elif choose==3:
    diamond(num)
elif choose==4:
    fish(num)
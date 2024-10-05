name =(input())
num =int(input())
chinese =int(input())
cs =int(input())
pd =int(input())

Average=(chinese+cs+pd)//3
Total=chinese+cs+pd

output="""
Name:{}
ID:{}
Average:{}
Total:{}
""".format(name, num, Average,Total)

print(output)

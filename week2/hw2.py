import math
a=int(input())
b=int(input())
c=int(input())

one = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
two = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)

print("%.1f" %one)
print("%.1f" %two)
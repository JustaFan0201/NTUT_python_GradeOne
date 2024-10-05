import math
from decimal import Decimal
h=Decimal(input())
w=Decimal(input())
bmi=Decimal(w/h/h)
bmi=(math.floor(bmi*1000)/1000.0)

if str(bmi*1000)[len(str(bmi*1000))-1]==5:
    beta_bmi=(math.floor(bmi*100)/100.0)
    if beta_bmi*100%2==0:
        bmi=(math.floor(bmi*100)/100.0)
    else:
        bmi=(math.ceil(bmi*100)/100.0)
else:
    bmi=round(bmi,2)
print("%.2f"%bmi)

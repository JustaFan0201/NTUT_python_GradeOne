import math
type1=input()
type2=input()
type3=input()
type1 = type1.split(',')
type2 = type2.split(',')
type3 = type3.split(',')
str1=[]
if int(type1[0])<=10:
    price1=380*float(type1[0])
elif int(type1[0])<=20:
    price1=380*float(type1[0])*float(type1[1])/100.0
elif int(type1[0])<=30:
    price1=380*float(type1[0])*float(type1[2])/100.0
else:
    price1=380*float(type1[0])*float(type1[3])/100.0

if int(type2[0])<=10:
    price2=1200*float(type2[0])
elif int(type2[0])<=20:
    price2=1200*float(type2[0])*float(type2[1])/100.0
elif int(type2[0])<=30:
    price2=1200*float(type2[0])*float(type2[2])/100.0
else:
    price2=1200*float(type2[0])*float(type2[3])/100.0

if int(type3[0])<=10:
    price3=180*float(type3[0])
elif int(type3[0])<=20:
    price3=180*float(type3[0])*float(type3[1])/100.0
elif int(type3[0])<=30:
    price3=180*float(type3[0])*float(type3[2])/100.0
else:
    price3=180*float(type3[0])*float(type3[3])/100.0

price1=math.ceil(price1)
price2=math.ceil(price2)
price3=math.ceil(price3)

if price1==price2==price3:
    print("A,"+str(price1),"B,"+str(price2),"C,"+str(price3))
elif price1==price2 and price1>price3:
    print("A,"+str(price1),"B,"+str(price2),"C,"+str(price3))
elif price1==price3 and price1>price2:
    print("A,"+str(price1),"C,"+str(price3),"B,"+str(price2))
elif price2==price3 and price2>price1:
    print("B,"+str(price2),"C,"+str(price3),"A,"+str(price1))
else:
    if max(price1,price2,price3)==price1:
        print("A,"+str(max(price1,price2,price3)))
    elif max(price1,price2,price3)==price2:
        print("B,"+str(max(price1,price2,price3)))
    else:
        print("C,"+str(max(price1,price2,price3)))
    if price2>price1>price3 or price2<price1<price3:
        print("A,"+str(price1))
    elif price1>price2>price3 or price1<price2<price3:
        print("B,"+str(price2))
    else:
        print("C,"+str(price3))
    if min(price1,price2,price3)==price1:
        print("A,"+str(min(price1,price2,price3)))
    elif min(price1,price2,price3)==price2:
        print("B,"+str(min(price1,price2,price3)))
    else:
        print("C,"+str(min(price1,price2,price3)))

print(price1+price2+price3)
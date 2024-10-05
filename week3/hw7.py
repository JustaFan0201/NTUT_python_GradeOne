in_voice=int(input())
out_voice=int(input())
phone=int(input())
in_msg=int(input())
out_msg=int(input())
internet=int(input())
flag_183=0
flag_383=0
flag_983=0
flag_1283=0
type_183=0.08*in_voice+0.139*out_voice+0.135*phone+1.128*in_msg+1.483*out_msg
type_383=0.07*in_voice+0.130*out_voice+0.121*phone+1.128*in_msg+1.483*out_msg
type_983=0.06*in_voice+0.108*out_voice+0.101*phone+1.128*in_msg+1.483*out_msg
type_1283=0.05*in_voice+0.1*out_voice+0.09*phone+1.128*in_msg+1.483*out_msg

if internet>1:
    type_183=type_183+(internet-1)*250
if internet>3:
    type_383=type_383+(internet-3)*200
if internet>5:
    type_983=type_983+(internet-5)*150

if type_183<=183:
    d_183=183-type_183
    flag_183=1
else:
    d_183=type_183-183
if type_383<=383:
    d_383=383-type_383
    flag_383=1
else:
    d_383=type_383-383
if type_983<=983:
    d_983=983-type_983
    flag_983=1
else:
    d_983=type_983-983
if type_1283<=1283:
    d_1283=1283-type_1283
    flag_1283=1
else:
    d_1283=type_1283-1283

ans=min([d_183,d_383,d_983,d_1283])
if ans==d_183:
    if flag_183==1:
        print('183')
        print('183')
    else:
        print('%.0f'%type_183)
        print('183')
if ans==d_383:
    if flag_383==1:
        print('383')
        print('383')
    else:
        print('%.0f'%type_383)
        print('383')
if ans==d_983:
    if flag_983==1:
        print('983')
        print('983')
    else:
        print('%.0f'%type_983)
        print('983')
if ans==d_1283:
    if flag_1283==1:
        print('1283')
        print('1283')
    else:
        print('%.0f'%type_1283)
        print('1283')
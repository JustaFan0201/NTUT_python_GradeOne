A=input()
B=input()
WORD1=input()
WORD2=input()
sub=abs(len(WORD2)-len(WORD1))

C=A+" "+B
print(C)
D=C.split(" ")
D_true=""
C_len=""
D_len=""

D_reverse=""

for i in range(len(D)):
    C_len=C_len+D[i]
    if D[i].upper()==WORD1.upper():
        D[i]=WORD2
        D_reverse=D_reverse+"".join(reversed(D[i]))+" "
    else:
        D_reverse=D_reverse+D[i]+" "
    if i!=len(D)-1:
        D_true=D_true+D[i]+" "
    else:
        D_true=D_true+D[i]
    D_len=D_len+D[i]
D_reverse.strip()
print(D_true)
print(str(len(C_len))+" "+str(len(D_len)))
print(D_reverse)
C_reverse=C[::sub]
C_reverse=C_reverse.replace("  "," ")
print(C_reverse)
# L1=["X:-1","Y:2","X:-4","B:1","X:5",]
# X1=0
# Y1=0
# B1=0
# for i in L1:
#     if "X" in i:
#         print(i[2:])
#         X1=X1+int(i[2:])
#     elif "Y" in i:
#         print(i[2:])
#         Y1 = Y1 + int(i[2:])
#     elif "B" in i:
#         B1=B1 + int(i[2:])
#
# L2=[]
# if(X1!=0):
#     X1="X1:"+str(X1)
#     L2.append(X1)
#
# if(Y1!=0):
#     Y1="Y1:"+str(Y1)
#     L2.append(Y1)
#
# if(B1!=0):
#     B1="B1:"+str(B1)
#     L2.append(B1)
#
#
# print(sorted(L2))
#




import re

string1="<div></div><div><Test>T</Test>"
tag=re.findall("<.*?>?>",string1)
rtag=[]

for i in tag:
    if "/" in i:
        rtag.append(i)
        tag.remove(i)
print(tag,"\n", rtag)

for i in tag:
    i= str(i).replace("<","</")
    if i in rtag:
        rtag.remove(i)
    else:
        print("no clsoe tag",i)
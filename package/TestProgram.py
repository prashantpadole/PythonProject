List1=[1,2,3,4,5,6]
Tuple1=(1,2,3,4,5,6)

print(List1*2)
print(Tuple1*2)

print(List1[0])
print(Tuple1[0])

List1=[100,300,400]
Tuple1=(100,200) #valid  because reinitialise Tuple
#Tuple1[0]=(100) # invalid assigning new value is not valid

print(List1)
print(Tuple1)


for i in List1:
    count = 0
    while(count<4):
        print("List values are {} ".format(i))
        count+=1

for i in Tuple1:
    count = 0
    while(count<5):
        print("Tuple values are {}".format(i))
        count+=1

# String opeartion
TestString1=" I stay in Canada"
TestString2="Name of the city is Montreal "

completeString=TestString1+" and "+TestString2
print(completeString)
print(TestString2*2)

#convert string into list
SList=list(TestString2)
print(SList)

print(TestString2.swapcase())
print(TestString2.split(' '))

splitString1=TestString1.split(' ')
print(sorted(splitString1))  ## sorted
List1.sort(reverse=True) # sort using reverse order
print(List1)

newString1=' '.join(splitString1)
print(newString1)

a=100
b=2.5
c=a/b
print("my name is Prashant",a,TestString2,c)

print(TestString2[1:10]) #string portion
print((TestString1[::-1])) # reverse string
print(TestString1.strip(' ')," and" , TestString2.strip())
print(set(TestString2))

##### Dictionary
Dict1={}
Dict1={1:"Test",2:'Blue',"West":200}
print(Dict1)

for i,seq in enumerate(Dict1.keys()):
    print(i," ",seq,"\n")


for i in Dict1.values():
    print(i,"\n")

for i in Dict1.items():
    print(i,"\n")

print(Dict1.get(1))
Dict2=Dict1.copy()
Dict1[0]="New"
print(Dict2,"\n",Dict1)

import copy
Dict2=copy.deepcopy(Dict1)
Dict1[10]="NewTest"
print(Dict2,"\n",Dict1)
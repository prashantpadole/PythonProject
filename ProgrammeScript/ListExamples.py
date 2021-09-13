# from typing import Set


# List1=[1,2,3,4,5,6,9,12,13]

# for i in List1:
#     print(i)
#     print("\n")

# print("Enumerator use in List")####
# ind=1
# for ind,value in enumerate(List1):
#     print(str(ind)+" "+str(value))
#     print("\n")

# print("converting list into Tuple using tuple function")

# weekdays =["Sun","Mon","Tue","Wed","Thur","Fri","Sat","Tue"]

# ListToTuple = tuple(weekdays)
# print(ListToTuple)

# print("converting list into Set using tuple function")

# ListToSet = set(weekdays)
# print(ListToSet)

# print("count occurance of element")

# count=0
# print(weekdays.count("Tue"))
# for i in weekdays:
#     if i=="Tue":
#         count= count + 1
    
# print("count of element is ",count)

# if "Tue" in weekdays:
#     print("element is preesnt in list")

# Set1={1,2,3,4,5,6}
# print(Set)
# print(type(Set1))
# print(len(Set1))

# if 3 in Set1:
#     print("element present in Set")

# if 10 not in Set1:

#     print("elemtn not in set")

# print("Add elements in Set")


# Set1.add(12)
# Set1.add(15)

# print(Set1)
# Set1.remove(12)

# print(Set1)

# print("print sum of 1 to 100")
# print(sum(range(1,100)))


# ##############

# print("calculate average of number \n")

# Num= int(input("enter number of element to be inserted \n"))

# ListNum=[]

# for i in range(0,Num):
#     elem = int(input("enter number "+str(i+1)))
#     ListNum.append(elem)
# Avg= sum(ListNum)/Num
# print(ListNum)
# print(Avg)




# ###############

# print("Reverse the number \n")

# Num1= int(input("Enter the number to be reverse \n"))
# ReverseNum=0

# while(Num1>0):
#     digit=Num1%10
#     ReverseNum=ReverseNum*10+digit
#     Num1=Num1//10

# print(ReverseNum)


# ########

# print("sum of digi in number \n")

# Num1= int(input("Enter Number for calculation \n"))

# TotalSum=0

# while(Num1>0):
#     digit=Num1%10
#     TotalSum=digit+TotalSum
#     Num1=Num1//10

# print(TotalSum)


# ########
# print("###########Palindrom Number######")

# OriNum=int(input("Enter the String"))
# ReverseNum=0

# while(OriNum>0):
#     digit=OriNum%10
#     ReverseNum=ReverseNum*10+digit
#     OriNum=OriNum//10

# if OriNum== ReverseNum:
#     print("Number is Palindrome Number")

# else:
#     print("Number is not palindrome")


# ##############

# print("####no of digit in number######")

# Num1= int(input("Enter the number for calculation \n"))

# noDigit=0


# while(Num1>0):
#     digit=Num1%10
#     noDigit=noDigit+1
#     Num1=Num1//10

# print("No of Digit in Number is ",str(noDigit))



#################

# print("print table of given number")

# Num1=int(input("Enter number for table"))

# for ind in range(1,11):
#     print(ind*Num1)
#     print("\n")


##############



# print("prime Number test \n")

# Num1=int(input("Enter Number to be evaluated \n"))
# prime=""

# if(Num1==1):
#     prime="false"
# else:
#     for i in range(2,Num1-1):
#         if(Num1%i==0):
#             prime="false"

# if(prime=="false"):
#     print("Number "+str(Num1)+" is not prime Number")

# else:
#     print("Number "+str(Num1)+" is  prime Number")



##################

print("Amstrong Number Test \n")

Num1=int(input("Enter number to be evaluated \n"))
OriNum=Num1
Sum=0
while(Num1>0):
    digit=Num1%10
    Sum=Sum+(digit**3)
    Num1=Num1//10

print("Sum of number is "+str(Sum))

if(Sum==OriNum):
    print("Number "+str(OriNum)+" is Armstrong Number ")
else:
    print("Number "+str(OriNum)+" is not an Armstrong Number ")

from utility import prime as iprime
import utility.Palindrom as ipalindrom


userChoice=int(input("Enter Your choice - 1. for Prime , 2. for palindrom Test \n"))

if(userChoice==1):
    #### Prime Number Test
    fNum=int(input("Enter number to check prime number: \n"))
    pNum=iprime.primeType(fNum).primeNum()

elif(userChoice==2):
    ### Palindrom Number Test
    pNum=int(input("Enter number to check if it is Palindrom \n"))
    ipalindrom.palindromType(pNum).palindromNum()

else:
    print("Invalid choice , Please enter again")

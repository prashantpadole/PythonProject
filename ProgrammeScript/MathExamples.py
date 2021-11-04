class Arithmatic:

    def __init__(self,Number):
        self.Number= Number
        print("number is "+str(Number))

    def armstrong(self):
        print("Amstrong Number Test \n"+str(self.Number))
        #Number=153
        ArmNum=self.Number

        Sum=0
        while(ArmNum>0):
            digit=ArmNum%10
            Sum=Sum+(digit**3)
            ArmNum=ArmNum//10

        print("Sum of number is "+str(Sum))

        if(Sum==self.Number):
            print("Number "+str(self.Number)+" is Armstrong Number ")
        else:
            print("Number "+str(self.Number)+" is not an Armstrong Number ")

    def prime(self):
        print("prime Number test \n"+str(self.Number))
        prime=""
        primeNum=self.Number
        if(primeNum==1):
             prime="false"
        else:
            for i in range(2,primeNum-1):
                if(primeNum%i==0):
                     prime="false"
        if(prime=="false"):
            print("Number "+str(self.Number)+" is not prime Number")
        else:
            print("Number "+str(self.Number)+" is  prime Number")




maths = Arithmatic(int(input("Enter Number to be evaluated as Test \n")))
maths.armstrong()
maths.prime()



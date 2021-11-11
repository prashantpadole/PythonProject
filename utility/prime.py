
class primeType:

    def __init__(self,num1):
        self.num1=num1

    def primeNum(self):

        flagPrime='Yes'
        tmp=0


        for i in range(2,(self.num1//2)+1):

            tmp=self.num1%i
            if(tmp==0):
                flagPrime='No'


        if(flagPrime=='No'):
            print(f'{self.num1} is not a prime number')
        else:
            print(f'{self.num1} is a prime number')













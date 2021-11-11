class palindromType:

    def __init__(self,num1):

        self.num1=num1

    def palindromNum(self):
        OriginalNum=self.num1
        ReverseNum=0

        while(OriginalNum>0):
            digit=OriginalNum%10
            OriginalNum=OriginalNum//10
            ReverseNum=ReverseNum*10+digit
            #print(f'digit is {digit} , OriginalNum is {OriginalNum} and ReverseNum is {ReverseNum}')

        if(self.num1==ReverseNum):
            print(f'{self.num1} is a palindrom number')
        else:
            print(f'{self.num1} is not a palindrom number')

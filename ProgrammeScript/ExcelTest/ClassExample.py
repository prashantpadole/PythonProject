class Addition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        # .operator with format
        print("first number is {}, second number is {}  and addition is {}".format(self.x,self.y,self.sum))
        # no comma no dot operato
        print("first number is %d,second number is %s and addition is %f" %(self.x,self.y,self.sum))
        #seperate all variable by ,
        print("first number is",self.x, "second number is ",self.y ,"and addition is ",self.sum)
        print("Pass",self.sum)

    def calculate(self):
        self.sum= self.x+self.y


add=Addition(100,200)
add.calculate()
add.display()
'''
class Person(object):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        self.sal=salary

    def getName(self):
        print(f'my name is {self.name}')




class Employee(Person):

    def __init__(self,name,age,salary):
        self.age=age
        Person.__init__(self,name,salary)

    def getAge(self):
        print("Age of Employee is {}".format(self.age))

    def getName(self):
        print("my name is--- %s " %(self.name))
        Person.getName(self)


emp=Employee("Prashant",20,200)
emp.getAge()
emp.getName()
# emp.__salary  # private variable
print(emp.sal)

Single Level inheritance'''
import json

''' Multiple Inheritance 
class Girraf(object):

    def __init__(self,name,color,height):
        self.name=name
        self.color=color
        self.height=height


    def property(self):
        print(f'Girraf Animal Name is {self.name}')
        print("Girraf Animal has {} color".format(self.color))
        print("Girraf Animal has medium %s" %(self.height))

class Horse(object):

    def __init__(self, name, color, height):
        self.name = name
        self.color = color
        self.height = height


    def property(self):
        print(f'Horse Animal Name is {self.name}')
        print("Horse Animal has {} color".format(self.color))
        print("Horse Animal has medium %s" % (self.height))


class Zebra(Girraf,Horse):
    def __init__(self,name,color,height):
        self.name=name
        self.color=color
        self.height=height
        Girraf.__init__(self,name,color,height)
        Horse.__init__(self, name,color, height)

    def property(self):
        print(f'Animal Name is {self.name}')
        print("Animal has {} color".format(self.color))
        print("Animal has medium %s" %(self.height))

    def HorseProperty(self):
        Horse.property(self)

    def GirrafProperty(self):
        Girraf.property(self)





animal=Zebra('Zebra','W&B','Medium')

animal.property()
animal.HorseProperty()

'''
import json

js={"Name":"Prashant",
    "Age":"25",
    "Employee":"Yes"}

### serialization : json to byte of data
# jsfile=open("outFile.json","w")
# json.dump(js,jsfile)
#
# print("deserlization")
# with open("outFile.json","r") as jsReadFile:
#     data = json.load(jsReadFile)
# print(data)
#
#
# #######
#
# element=WebDriver(driver,10).untill(EC.presence_of_element_located(By.id,"test"))
#
# element=WebDriverWait(driver,10).untill(EC.presentof_elementlocate(By.id,"Name"))

list1=["A","B","C","D","H"]
Test=' '.join(alph for alph in list1)
print((Test))
Test2="Example"
print(Test2)
print(Test+",".join(Test2))
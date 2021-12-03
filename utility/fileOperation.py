import os


class fileOperation:
    def __init__(self,filename):
        self.filename=filename
        print("filename is %s" % str(self.filename))

    def OpenFile(self):
        fileOpen=open(str(self.filename),"w+")
        print(fileOpen.name)
        print(fileOpen.mode)


    def ReadFile(self):
        fileOpen = open(self.filename, "r+")
        fileRead=fileOpen.read()
        print(fileRead)



    def WriteFile(self):
        fileOpen = open(self.filename, "w+")
        fileContent='''This is my file , 
                       and don't touch it
                       I am writing sample text for testing'''
        print(fileOpen.tell())
        fileOpen.seek(5, 0)
        fileOpen.write(fileContent)
        print(fileOpen.tell())
        fileOpen.closed

    def osFileOpt(self):
        try:
            os.rename(self.filename,r'C:\MSDE\PythonProject\TestData\NewFile.txt')
        except FileExistsError:
            os.remove(r'C:\MSDE\PythonProject\TestData\NewFile.txt')
            os.rename(self.filename, r'C:\MSDE\PythonProject\TestData\NewFile.txt')

        try:
            os.remove("NewFile.txt")
        except FileNotFoundError:
            os.remove(r'C:\MSDE\PythonProject\TestDat\NewFile.txt')
        except FileNotFoundError:
            os.remove(r'C:\MSDE\PythonProject\TestData\NewFile.txt')
        else:
            print("No error Encountered \n")
        finally:
            print("Finally executed")

        print("Done")






filename=r'C:\MSDE\PythonProject\TestData\TestDocument.txt'
fileOp=fileOperation(filename)
fileOp.OpenFile()
fileOp.WriteFile()
fileOp.ReadFile()
# fileOp.osFileOpt()


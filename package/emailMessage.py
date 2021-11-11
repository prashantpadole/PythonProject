import configparser
import utility.sendEmailAttachment as se

config=r'C:\MSDE\PythonProject\ProgrammeScript\config.cfg'
parser=configparser.ConfigParser()
parser.read(config)

fromaddr=parser.get('email','fromaddr')
toaddr=parser.get('email','toaddr')
body=parser.get('email','body')
subject=parser.get('email','subject')

semail=se.sendEmailMessage(fromaddr,toaddr,body,subject) # create object of file se and call class"
semail.emailMessage()
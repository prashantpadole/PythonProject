import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os.path
import getpass

class sendEmailMessage:
    def __init__(self,fromaddr,toaddr,body,subject):
        self.fromaddr=fromaddr
        self.toaddr=toaddr
        self.body=body
        self.subject=subject

    def emailMessage(self):
        msg=MIMEMultipart()
        msg['Subject']=self.subject
        msg['From']=self.fromaddr
        #msg.set_type('text/html')
        #msg.set_content(self.body)

        file_name=r'C:\MSDE\PythonProject\ProgrammeScript\sendEmail\TestData\MyExcelSheet.xlsx'
        fName=os.path.basename(file_name)

        part=MIMEBase('application','octet-stream')
        part.set_payload(open(file_name,'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment',filename=fName)
        msg.attach(part)
    #     return msg
        print("start")
    #    password = getpass.getpass(prompt="Enter Your Password")
        print("end")
    # def sendMessage(self):
        server =smtplib.SMTP('smtp.gmail.com')
        server.connect('smtp.gmail.com')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('padole.prashant1.com','TestPassword')
        server.sendmail(self.fromaddr,self.toaddr,msg.as_string())
        print("email has been sent")
        server.quit()








import smtplib
from email.mime.text import MIMEText
import random
import pdfkit
import wkhtmltopdf

# This is a class that is used to carry out different types of tasks, including email verification and download webpage.

class Function_D():
    def __init__(self):
        pass

    def send_email(self,sender,receiver,psd,subject,content):
        """
        This can only be used as sina email
        """
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        try:
            s = smtplib.SMTP_SSL('smtp.sina.cn')
            s.login(sender,psd)
            s.sendmail(sender,receiver,msg.as_string())
            print('Email Sent')
        except smtplib.SMTPException:
            print('Fail To Send')
            return content[-7:]

    def gen_ran_num(self):
        ranstr = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',6)
        ranstr = ''.join(ranstr)
        return ranstr

    def download_webpage(self):
        pdfkit.from_file('timetable.html','out.pdf'))

a = Function_D()
"""
sender = 'davidxiong@sina.cn'
receiver = 'airsealand@163.com'
psd = 'david0811'
subject = 'Dawei Xiong CSIA Test'
content = 'This is your six digit verification code:  ' + a.gen_ran_num()
verification_code = content[-7:]
print(content)
#print(verification_code)
a.send_email(sender,receiver,psd,subject,content)
"""
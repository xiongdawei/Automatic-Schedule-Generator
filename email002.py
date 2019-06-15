import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.qq.com"
mail_user = "663440751@qq.com"
mail_pass = 'ibdpcsia2020'


sender = '663440751@qq.com'
receivers = ['davidxiong@sina.cn']

message = MIMEText('Python Test', 'plain', 'utf-8')
message['From'] = Header("Python Test", 'utf-8')
message['To'] = Header("Python", 'utf-8')

try:
    subject = 'Python SMTP Email Test'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Email Sent"
except smtplib.SMTPException :
    print "Error: Fail To Send The Email"
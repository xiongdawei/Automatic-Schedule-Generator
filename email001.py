import smtplib
from email.mime.text import MIMEText
from email.header import Header
from django.core.mail import send_mail

sender = 'davidxiong@sina.cn'
receivers = 'airsealand@163.com'

email_title = 'Test'
email_body = 'Python Email Test'
email = ''







"""
receivers = 'davidxiong@sina.cn'
sender = 'airsealand@163.com'

message = MIMEText('Test','plain','utf-8')
message['From'] = Header('Test001','utf-8')
message['To'] = Header('Test002','utf-8')

subject = 'Python SMTP email test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpobj = smtplib.SMTP('smtp.sina.cn')
    smtpobj.sendmail(sender,receivers,message.as_string())
    print('Sent the email succesfully')
except smtplib.SMTPException:
    print('Error: Cannot send the email')
"""
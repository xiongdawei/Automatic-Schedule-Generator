import smtplib
from email.mime.text import MIMEText

msg_from = 'davidxiong@sina.cn'
passwd = 'david0811'
msg_to = 'airsealand@163.com'

subject = "Python Test"
content = "This is the test"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.sina.cn")
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print "Email Sent"
except smtplib.SMTPException:
    print "Fail To Send"


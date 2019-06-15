import smtplib
from email.mime.text import MIMEText

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


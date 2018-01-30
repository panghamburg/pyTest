import smtplib
from email.header import Header
from email.mime.text import MIMEText

sendhost = 'smtpdm.aliyun.com'
sendmail = 'support@exmail.lightbeijing.com'
sendport = 465
sendpassword = 'Lbjadmin2016'

tomail = ['2234363442@qq.com']
html_content = '''
<h1>测试邮件</h1>
<p>测试邮件内容</p>
<p>换行内容</p>
'''
message = MIMEText(html_content, 'html', 'utf-8')
message['From'] = Header('lbj', 'utf-8')
message['To'] = Header(tomail[0], 'utf-8')
subject = 'SMTP TEST'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(sendhost, sendport)
    smtpObj.login(sendmail, sendpassword)
    smtpObj.sendmail(sendmail, tomail, message.as_string())
    smtpObj.quit()
    print('已发送')
except smtplib.SMTPException as e:
    print(e)

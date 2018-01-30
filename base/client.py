import socket
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 9999
# s.connect((host, port))
# msg = s.recv(1024)
# s.close()
# print(msg.decode('utf-8'))

#设置邮箱
sendhost = 'smtpdm.aliyun.com'
sendmail = 'support@exmail.lightbeijing.com'
# sendlogname = 'support@exmail.lightbeijing.com'
sendpas = 'Lbjadmin2016'
# sendport = 465
# sendmail = 'from@loc.com'
tomail = ['2234363442@qq.com']
html_c = '''
<h1>测试邮件</h1>
<p>测试邮件内容</p>
<p>换行内容</p>
'''
message = MIMEText(html_c, 'html', 'utf-8')
message['From'] = Header('The me', 'utf-8')
message['To'] = Header(tomail[0], 'utf-8')

subject = 'SMTP 测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(sendhost, sendport)
    smtpObj.login(sendlogname, sendpas)
    smtpObj.sendmail(sendmail, tomail, message.as_string())
    print('发送ok')
except smtplib.SMTPException as e:
    print(e)

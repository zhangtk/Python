# -*- coding="utf-8" -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱的服务器
smtpserver = "smtp.163.com"
#发送邮箱的用户名及密码
user = "xxxxxxxx"
pwd = "xxxxx"
#发送用户
sender = "xxxxxxx@163.com"
#接受用户
recevier = "xxxxxxx@qq.com"
#主题
subject = "TestedReSult"
#内容
msg = MIMEText('请知悉！','plain','utf-8')

msg['Subject'] = Header(subject,'utf-8')
msg['From'] = 'cainiao<xxxxxxxx@163.com>'
msg['To'] = 'xxxxxxx@qq.com'


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,pwd)
smtp.sendmail(sender,recevier,msg.as_string())
smtp.quit()
print("邮件发送成功！")
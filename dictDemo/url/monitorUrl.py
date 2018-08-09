#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib,sys,urllib,json,smtplib
from email.mime.text import MIMEText
mailto_list=['liudong@researchina.cn']
mail_host="smtp.exmail.qq.com"
mail_user="liudong@researchina.cn"
mail_pass="邮箱密码"
mail_postfix="researchina.cn"
def send_mail(to_list,sub,content):
     me="hello"+"<"+mail_user+"@"+mail_postfix+">"
     msg = MIMEText(content,_subtype='plain')
     msg['Subject'] = sub
     msg['From'] = me
     msg['To'] = ";".join(to_list)
     try:
         server = smtplib.SMTP(mail_host,25)
         server.set_debuglevel(1)
         server.login(mail_user,mail_pass)
         server.sendmail(me, to_list, msg.as_string())
         server.close()
     except :
         return False
url = "http://storm.yqing.cn/api/v1/cluster/summary"
wp = urllib.urlopen(url).read()
#content = wp.read()
#print(wp)
a = json.loads(wp)
b = (a["supervisors"])
 #print(b)
if b < 3:
    send_mail(mailto_list,'Storm UI','Please check immediately error')
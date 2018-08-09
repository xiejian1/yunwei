#-*- encoding: utf-8 -*-


import linecache,sys,time,datetime,os
import urllib,sys,urllib,json,smtplib
from email.mime.text import MIMEText

mailto_list=['liudong@philisense.com']
mail_host="smtp.philisense.com"
mail_user="liudong@philisense.com"
mail_pass="邮箱密码"
mail_postfix="philisense.com"
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

for root,dirs,files in os.walk(r'/home/work/app/jppt/log/new_log'):
    for file in files:
        with open(root+"/"+file, 'r') as f:
            lines = f.readlines()
            last_line = lines[-1]
            a = last_line.strip()
            try:
                timeArray = time.strptime(a,"%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray))
            except Exception as ex:
                send_mail(mailto_list,'jppt','file = '+ file + '\n' + '\n' + a)
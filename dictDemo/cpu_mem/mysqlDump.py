#!/usr/bin/env python
# author: liudong
# -*- coding: utf-8 -*-
# filename: db_bak.py
import os
import time
import string

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
#######################################以上是邮箱配置##########################################
''' defined variable '''
databases=['zabbix']    #定义要备份的数据库名
sql_user='zabbix'       #数据库登陆用户
sql_pwd=['zabbix']      #数据库登陆密码
''' Defining the remote backup variables '''
jv_test01_ip="192.168.199.193"      #备份服务器ip
jv_test01_user="work"       #账户
jv_test01_port='19741'      #端口
jv_test01_dir="/home/work/"         #要备份到的服务器路径
''' Create the backup file directory '''
mkdir_dir="/home/work/"+time.strftime('%Y%m%d')+"/"       #在/home/work/目录下用当天时间的格式创建目录
if not os.path.exists(mkdir_dir):       #判断如果没有当天时间目录
    os.mkdir(mkdir_dir)     #创建
print ('Successfully created directory', mkdir_dir)       #打印创建成功
''' Start backup of database to the specified directory '''
for database_name in databases:     #循环zabbix数据库
    os.chdir(mkdir_dir)         #改变当前工作目录到指定的路径
today_sql=mkdir_dir+database_name+'_'+time.strftime('%Y%m%d')+'.sql' #定义数据库文件名变量
sql_comm="mysqldump -u %s -p'%s' %s > %s"%(sql_user,sql_pwd[0],database_name,today_sql) #定义备份数据库变量
if os.system(sql_comm) == 0:    #如果上一条执行结果等于0，表示成功
    print (database_name,'is backup successfully!')   #打印成功信息
else:       #否则
    send_mail(mailto_list,'db_bak','The in db_bak error !!')    #发送邮件，提示未备份成功信息
time.sleep(3)   #停顿3秒
scp_comm="scp -P%s %s %s@%s:%s "% (jv_test01_port,today_sql,jv_test01_user,jv_test01_ip,jv_test01_dir)#把备份的数据库文件拷贝到指定的服务器的备份目录
if os.system(scp_comm) == 0:    ##如果上一条执行结果等于0，表示成功
    print (today_sql,'This file backup to jv_test01 success!' )   #打印成功信息
else:       #否则
    send_mail(mailto_list,'db_bak','The in scp  error !!')   #发送邮件，提示未远程备份成功信息
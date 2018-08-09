#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib,sys,urllib3,json,smtplib
from email.mime.text import MIMEText

mailto_list=['邮箱']
mail_host="smtp.philisense.com"
mail_user="邮箱"
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
#把 接口：参数，以（key ：value）写成字典的方式
api_host ={"http://back.oursdata.com/jppt/jp-index-data/hours-data":{"appid":"1,2,3,4",
        "indexType":"node_activeness_count",
        "dateType":"month",
        "startDate":"2016/6/25",
        "endDate":"2016/12/21"},
        "http://back.oursdata.com/jppt/jp-index-data/avg-day":{"appid":"1, 2, 3, 4, 5",
        "indexType":"active_avg",
        "dateType":"week",
        "_csrf":"Q2lwdWd0ekQaXkgANEEDMy89RVgORzsLJAs4MgVMKBYiOy8aBgZMCA=="}
        }
#给函数定义两个参数
def interfaceTest(api_url,parameter):
    params = urllib.urlencode(parameter)
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
    req = urllib3.Request(url=api_url, data=params, headers=headers)
    response = urllib3.urlopen(req)
    a = json.loads(response.read())
    if a["err"] == "ok":
        if len(a["data"]) == 0:
            send_mail(mailto_list,'data',k + '\n' 'The data is None!!!')
    else:
        send_mail(mailto_list, 'err','"err" not equal to "ok"')

if __name__ == "__main__":
    for (k,v) in api_host.items():
        interfaceTest(k,v)   #给函数传参
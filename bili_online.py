#coding=utf-8

import asyncio
import aiohttp
import xml.dom.minidom
import random
import json
import json
import re
import webbrowser
import os
import datetime
import requests
import time

import sys
import requests
import smtplib
from email.mime.text import MIMEText

#http://space.bilibili.com/ajax/live/getLive?mid=1593666
#587832
#{"status":true,"data":"36963"}
#http://live.bilibili.com/bili/isliving/1593666
#is not ({"code":0,"msg":"","data":""});

def sendmail(live):
    ##发邮件
    mailto_list=["185128167@qq.com"]    #收件箱
    mail_host="smtp.qq.com"         #发件箱服务器, 163的是smtp.163.com, 126的是smtp.126.com, qq的是smtp.qq.com
    mail_user="860665461"                 #发件箱用户名, 例如test@163.com, 则用户名是test
    mail_pass="dlogpgglpchwbdci"           #发件箱密码, 就是上面填的test@163.com的密码
    mail_postfix="qq.com"           #这个改为跟发件箱一样的后缀
    sub= live+'了。。。'
    content = "http://live.bilibili.com/138"
    me=live+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)
    
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, mailto_list, msg.as_string())
        server.close()
        print ("send_mail成功")
        return True
    except:
        print ("False")
        return False 
    print('发邮件')

nowOnline = 0
while(1):
    try:   
        r = requests.get('http://live.bilibili.com/bili/isliving/1593666').text
        print(r)
        if "online" in r:
            print('online')
            if nowOnline == 0:
                nowOnline = 1
                sendmail('live')
                #webbrowser.open('http://live.bilibili.com/138')
            else:
                print('不发邮件')
        else:
            if nowOnline == 1:
                sendmail('nolive')
            nowOnline = 0
            print('不在直播')
        time.sleep(60*5)#300000 5分钟一次

        
    except:
        print("False")
        time.sleep(60/4)
#res = re.search(r'true', r)
#if res:
#    print(res)

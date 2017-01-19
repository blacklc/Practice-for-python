#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月23日

@author: lichen
'''
import poplib
import smtplib
#import email.mime.text.MIMEText
from email.mime.text import MIMEText  


uname='akdkss1230@163.com'
pwd='lc199248'
mail_server='pop.163.com'
mail_host='smtp.163.com'
#mail_postfix='163.com' #发件箱后缀

#将邮箱中的邮件全部下载到本地
def download_AllMail():
    p=poplib.POP3(mail_server)
    p.user(uname)
    p.pass_(pwd)
    for msg_id in p.list()[1]:
        print msg_id
        mailfile=open('/Users/lichen/Desktop/%s.eml' %msg_id,'w')
        mailfile.write('/n'.join(p.retr(msg_id)[1]))
        mailfile.close()
        p.quit()

#实时收取最新邮件
def download_NewMail():
    while 1:
        p=poplib.POP3(mail_server)
        p.user(uname)
        p.pass_(pwd)
        idlist=p.list()[1]
        msg_id=idlist[-1]
        print msg_id
        mailfile=open('/Users/lichen/Desktop/%s.eml' %msg_id,'w')
        mailfile.write('/n'.join(p.retr(msg_id)[1]))
        mailfile.close()
        p.quit()

def send_mail(to_addrlist,sub,content):
    msg=MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject']=sub #确定邮件主题
    msg['From']=uname #确定发信人
    msg['To']=';'.join(to_addrlist) #确定收信人
    try:
        sm=smtplib.SMTP() #创建实例
        sm.set_debuglevel(1) #打开调试模式
        #sm.starttls(keyfile, certfile) #启动ssl
        sm.connect(mail_host) #连接发件服务器
        sm.login(uname,pwd) #登陆服务器
        sm.sendmail(uname,to_addrlist,msg.as_string())
        sm.close()
        return True
    except Exception,e:
        print str(e)
        return False

def main():
    to_list=['575784862@qq.com']
    sub='需要联系你'
    content='你好，我是你的同事，想联系你'
    if send_mail(to_list,sub, content):
        print "send sucessful"
    else:
        print 'send False'

main()
        
    











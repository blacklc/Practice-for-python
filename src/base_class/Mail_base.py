#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月12日

@author: lichen
'''

import poplib
import smtplib
from email.mime.text import MIMEText 

class mailbase(object):
    '''
    邮件常用操作类
    基于pop3协议
    '''

    __slots__=('__path','__uname','__passwd','__mail_server','__mail_host')
    
    def __init__(self):
        self.__uname=''
        self.__passwd=''
        self.__mail_server=''
        self.__mail_host=''

    def get_uname(self):
        return self.__uname


    def get_passwd(self):
        return self.__passwd


    def get_mail_server(self):
        return self.__mail_server


    def get_mail_host(self):
        return self.__mail_host


    def set_uname(self, value):
        self.__uname = value


    def set_passwd(self, value):
        self.__passwd = value


    def set_mail_server(self, value):
        self.__mail_server = value


    def set_mail_host(self, value):
        self.__mail_host = value

    uname = property(get_uname, set_uname, None, None)
    passwd = property(get_passwd, set_passwd, None, None)
    mail_server = property(get_mail_server, set_mail_server, None, None)
    mail_host = property(get_mail_host, set_mail_host, None, None)
    
    def download_AllMail(self,mailfile_path):
        '''
        将邮箱中的邮件全部下载到本地
        '''
        p=poplib.POP3(self.mail_server)
        p.user(self.__uname)
        p.pass_(self.__passwd)
        for msg_id in p.list()[1]:
            print msg_id
            mailfile=open('%s/%s.eml' %(mailfile_path,msg_id),'w')
            mailfile.write('/n'.join(p.retr(msg_id)[1]))
            mailfile.close()
            p.quit()
    
    def download_NewMail(self,mailfile_path):
        '''
        实时收取最新邮件
        '''
        while 1:
            p=poplib.POP3(self.__mail_server)
            p.user(self.__uname)
            p.pass_(self.__passwd)
            idlist=p.list()[1]
            msg_id=idlist[-1]
            print msg_id
            mailfile=open('%s/%s.eml' %(mailfile_path,msg_id),'w')
            mailfile.write('/n'.join(p.retr(msg_id)[1]))
            mailfile.close()
            p.quit()
            
    def send_mail(self,to_addrlist,sub,content):
        '''
        发送邮件
        '''
        msg=MIMEText(content,_subtype='plain',_charset='gb2312')
        msg['Subject']=sub  #确定邮件主题
        msg['From']=self.__uname #确定发信人
        msg['To']=';'.join(to_addrlist) #确定收信人
        try:
            sm=smtplib.SMTP() #创建实例
            sm.set_debuglevel(1) #打开调试模式
            #sm.starttls(keyfile, certfile) #启动ssl
            sm.connect(self.__mail_host) #连接发件服务器
            sm.login(self.__uname,self.__passwd) #登陆服务器
            sm.sendmail(self.__uname,to_addrlist.msg.as_string())
            sm.close()
            return True
        except Exception,e:
            print str(e)
            return False

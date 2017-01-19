#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月8日

@author: lichen
'''

import subprocess
import ConfigParser
import Queue
import time
import threading
import base_class.Thread_base as threadbase

def readConfig(configfile):
    '''
    读取配置文件，并返回服务器地址列表和操作指令列表
    '''
    ips=[]
    cmds={}
    config=ConfigParser.ConfigParser()
    config.read(configfile)
    machines=config.items("MACHINES")
    commands=config.items("COMMANDS")
    for ip in machines:
        ips.append(ip[1])
    for commandcontent in commands:
        cmds[commandcontent[0]]=commandcontent[1]  #加载过程中会自动将配置文件中的字符串小写化
    return ips,cmds

def launcher(queue,cmd_type,cmd_content):
    '''
    线程调用方法
    '''
    ip=queue.get()
    print "thread %s is running cmd:%s on %s" %(threading.current_thread().name,cmd_type,ip)
    subprocess.call("ssh %s %s" %(ip,cmd_content),shell=True)
    #向队列发送工作完成信号，必须要有
    queue.task_done()
    
start_time=time.time()
q=Queue.Queue()
ips,cmds=readConfig("resources/config.ini")
#创建自定义线程对象
t=threadbase.thread_base()
#确定线程并发数
if len(ips)<10:
    t.thread_num=len(ips)
else:
    t.thread_num=10
t.thread_target=launcher
#创建线程池
for cmd_type in cmds:
    t.thread_args=(q,cmd_type,cmds[cmd_type])    
    t.create_thread_pool()    
print "now,Main Thread waiting"
for ip in ips:
    q.put(ip)
#等待队列为空以后再执行后续代码，必须要有
q.join()
end_time=time.time()
print "Task completed in %s seconds" %(end_time-start_time)




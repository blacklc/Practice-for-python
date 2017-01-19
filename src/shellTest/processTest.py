#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年7月26日

@author: lichen
'''

import sys
import os
import time
import subprocess
from threading import Timer

def multi(*args):
    """
    支持输入多条shell命令
    """
    for cmd in args:
        p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        out=p.stdout.read()
        print out
multi("df -h","ls -l /")

#与标准输入进行通信
p=subprocess.Popen("wc -c",shell=True,stdin=subprocess.PIPE)
p.communicate("lichen")

#shell管道的实现
p1=subprocess.Popen("netstat -an",shell=True,stdout=subprocess.PIPE)
p2=subprocess.Popen("grep 80",shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
print p2.stdout.read()

def daemonize(stdin="/dev/null",stdout="/dev/null",stderr="/dev/null"):
    """
    将当前进程转化为守护进程
    """
    try:
        pid=os.fork()
        #判断是否是父进程
        if pid>0:
            #如果是父进程，则关闭父进程
            sys.exit(0)
    except OSError,err:
        sys.stderr.write("fork father process failed: %s" %err)
    #创建守护进程
    os.chdir("/") #使守护进程不影响目录挂载卸载操作
    os.umask(0) #为守护进程分配系统权限
    os.setsid() #使守护进程建立一个新会话、建立一个新进程组并且脱离终端控制
    #整理标准输入、输出和错误流
    si=file(stdin,"r")
    so=file(stdout,"a+")
    se=file(stderr,"a+",0)
    #重定向标准输入、输出和错误流到指定文件中
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(),sys.stderr.fileno())

daemonize("/Users/lichen/Desktop/stdin.log","/Users/lichen/Desktop/stdout.log", "/Users/lichen/Desktop/stderr.log") 
def hello():
    print "hello world"
#设置定时线程任务
t=Timer(5,hello)
t.start()
delay=5
for i in range(delay):
    print delay
    delay=delay-1
    time.sleep(1) 
    
time.sleep(3)


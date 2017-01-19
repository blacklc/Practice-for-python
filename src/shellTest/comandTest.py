#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月12日

@author: lichen
'''

import time
import subprocess


def disk_report(command):
    p=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
    return p.stdout.readlines() #将命令输出的每行内容组成一个list作为返回值

#执行任意命令
subprocess.call('ls -l /',shell=True)

print '\n'+'this is the system info:'
print 'uname:'
subprocess.call('uname -a',shell=True)
print ''
print 'storge:'
subprocess.call('df -h',shell=True)
print ''

print type(time.strftime("%Y-%m-%d"))




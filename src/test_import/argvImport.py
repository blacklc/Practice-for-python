#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
__author__='lichen'

import sys

def readargv():
    argvlist=sys.argv
    length=len(argvlist)
    for i in range(length):
        if length==1:
            print 'already read the first argv,and the first argv is \"',argvlist[0],'\"and not input argv.'
        elif i==0:
            print 'already read the first argv,and the first argv is',argvlist[0]
        else:
            print 'already read the %d argv,and the %d argv is' %(i,i),argvlist[i] 

#可以用此判断来测试某一个模块文件中的功能函数。其原理就是在单独运行某一个模块文件的时候，系统会自动把变量__name__的值赋成__main__
if __name__=='__main__':
    print 'only run import'
    readargv()
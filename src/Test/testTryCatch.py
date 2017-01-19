#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#使用logging模块将程序错误信息记录到日志中
import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def trycatchfinally():
    try:
        print '\n'+'\n'+'start try&catch'
        bar('0')
    except StandardError,e:
        print 'error is \"',e,'\"'
        #logging.exception(e)
        #将错误输出到指定文件中。注意，必须要有“level”参数，否则无法输出到文件中。
        logging.basicConfig(level=logging.DEBUG,  
                            filename='/Users/lichen/Desktop/python/tmp.log',
                            filemode='w',
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        logging.info(e)
    #finally:
        #print 'finally...........'

trycatchfinally()
print 'END'
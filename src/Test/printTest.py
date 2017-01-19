#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#print('中文').encode('utf-8')
print('中文')

name=raw_input("please input your name:")
print('the name your input is '+name+'\n')

length=len(name)
print'the name\'s length=',length

#可用print的格式化输出解决输出中多余空格的问题
print('name is %s and the length=%d'+'\n') %(name,length)

print "****************************************************************"
print "                      DaliyCheck Report                         "
print "****************************************************************"
print "***************"
print "*     EHR     *"
print "***************"
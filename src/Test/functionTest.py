#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''

def infoprint(info):
    print info
    
infoprint('test')
infoprint(123)

#函数可以有多个返回值
def addnumber(x,y):
    x=x+1
    y=y+1
    return x,y

a,b=addnumber(1,2)
infoprint(a)
infoprint(b)

#可变参数在函数调用时自动组装为一个tuple
def addnumber2(*list1):
    #初始化list
    list2=[]
    for i in range(5):
        list2.append(i)
    print type(list1)
    
addnumber2()
    
#关键字参数在函数内部自动组装为一个dict
def user(name,age,**information):
    print 'name:%s,age=%d' %(name,age),
    print 'information:',information,'\n'
infor={'male':'female'}
user('test',10,**infor)


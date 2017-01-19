#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
import types
import test_import.testClass
#判断变量的类型
print '\n'+'123\'s type is',type(123)
#判断两个变量的类型是否相同
if type(123)==type('abc'):
    print '相同'
else:
    print '不相同'
#判断是否为某一基本类型
if type(123)==types.IntType:
    print '是int'
else:
    print '不是int'
#判断是否为一特定类
ttt=test_import.testClass.test1()
uuu=test_import.testClass.son1()
#isinstance返回的是bool类型
print type(isinstance(ttt,test_import.testClass.test1))
if isinstance(ttt,test_import.testClass.test1):
    print 'ttt is class test1'
#获取一个对象的所属的类的所有属性和类方法
classlist1=dir(ttt)
print classlist1
#class1.aaa=99
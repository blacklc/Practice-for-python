#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''

import test_import.testClass

#建立对象的时候要在类名后加上括号，不管有没有初始参数
class1=test_import.testClass.test1()
class1.set_name('lichen')
class1.set_number(1)
#调用时需要加上()
class1._printinfo()
son2=test_import.testClass.son1()
son2.set_number(1)
son2.set_name('lichen2')
print 'before add number,number is',
son2._printinfo()
son2.add_number(5)
print 'after add number,number is',
son2._printinfo()

#输出指定对象的所有属性和方法
print '\n',dir(class1)
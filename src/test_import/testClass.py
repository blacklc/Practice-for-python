#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#面向对象
class test1(object):
    #限制类中的属性。只有在括号里出现的属性才能被建立使用。注意，此项不对子类管用。子类中需要再限制。
    __slots__=('__name','__number')
    def __init__(self):
        self.__name=''
        self.__number=0
    #私有变量：在变量前加上两个下滑线即可。同样，私有变量的赋值和使用只能用类方法来调。
    def set_name(self,name):
        self.__name=name
    def set_number(self,number):
        self.__number=number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    #所有的类方法的第一个参数必须为self
    def _printinfo(self):
        print 'name=',self.get_name(),'number=',self.get_number()
        
#继承了test类
class son1(test1):
    def add_number(self,number):
        #self.__number=self.__number+number
        #a=self.get_number
        #子类调用父类的私有变量需要使用父类的方法
        self.set_number(self.get_number()+number)
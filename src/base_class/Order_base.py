#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月12日

@author: lichen
'''

class orderbase(object):
    '''
    classdocs
    '''

    '''
    def __init__(self, params):
    
    '''
    
    def zdypx(self,x,y):
        '''
        自定义排序
        针对字母排序忽略大小写,原理为全部都转换成大写或者小写即可
        '''
        if 'A'<x<'z' and 'A'<y<'z':
            x=x.upper()
            y=y.upper()
        if x<y:
            return -1
        elif x==y:
            return 0
        else:
            return 1
        
        
        
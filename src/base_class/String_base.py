#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月12日

@author: lichen
'''

class string_base(object):
    '''
    字符串常用方法类
    '''

    '''
    def __init__(self, params):

    '''
        
    def cutline(self,strs):
        '''
        已空格为分隔符️切割多行文本,返回值为每行的每一个单词的map
        ''' 
        cutlinelist=strs.splitlines()
        linewordlist=[]
        report={}
        for i,line in enumerate(cutlinelist):
            for linewords in line.split():
                linewordlist.append(linewords)
            report[i+1]=linewordlist
            linewordlist=[]
        return report
                
                
                
                
                
                
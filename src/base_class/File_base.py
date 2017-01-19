#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月18日

@author: lichen
'''

class filebase(object):
    '''
    自定义底层文件类
    '''

    __slots__=('__path')
    
    def __init__(self):
        '''
        初始化属性
        '''
        self.__path=''
    
    def set_path(self,path):
        self.__path=path
        
    def get_path(self):
        return self.__path
    
    def readallfile(self,readbit=0):
        f=open(self.get_path(),'r')
        print '文件内容为'
        if readbit==0:
            print f.read()
        else:
            print f.read(readbit)
    
    def readlinefile(self,linesize=0):
        f=open(self.get_path(),'r')
        print '文件的一行内容为'
        if linesize==0:
            print f.readline()
        else:
            print f.readline(linesize)
            
    def readlinesfile(self,sizeint=0):
        f=open(self.get_path(),'r')
        #print '文件中的所有行内容为'
        if sizeint==0:
            #print f.readlines()
            return f.readlines()
        else:
            print f.readlines(sizeint)
            return f.readlines(sizeint)
        
    def addcontent(self,addtext):
        try:
            f=open(self.get_path(),'a')
            f.write(addtext+'\n')
        finally:
            f.close()
        
        
        
        
        
        
        
        
        
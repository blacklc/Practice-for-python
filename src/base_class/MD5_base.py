#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月30日

@author: lichen
'''
import hashlib

class MD5base(object):
    '''
    MD5校验基础类
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
    
    def create_checksum(self,path):
        f=open(path)
        checksum=hashlib.md5()
        while True:
            fbuffer=f.read()
            if not fbuffer:break    #如果读取文件的内容为空，则跳出循环
            checksum.update(fbuffer)
        f.close()
        checksum=checksum.digest()
        return checksum
        
        
        
        
        
        
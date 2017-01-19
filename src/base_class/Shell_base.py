#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月12日

@author: lichen
'''

import subprocess

class shellbase(object):
    '''
    shell命令相关操作
    '''
    
    __slots__=('__command','__param')

    def __init__(self):
        self.__command=''
        self.__param=''

    def get_command(self):
        return self.__command


    def get_param(self):
        return self.__param


    def set_command(self, value):
        self.__command = value


    def set_param(self, value):
        self.__param = value

    command = property(get_command, set_command, None, None)
    param = property(get_param, set_param, None, None)
    
    def command_report(self):
        '''
        打印任意命令的返回值
        '''
        p=subprocess.Popen([self.__command,self.__param],shell=True,stdout=subprocess.PIPE)
        return p.stdout.readlines() #将命令输出的每行内容组成一个list作为返回值
    
        
        
        
        
    
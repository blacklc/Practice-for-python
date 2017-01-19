#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月16日

@author: lichen
'''

import threading

class thread_base(object):
    '''
    进程与线程相关基础方法
    '''

    __slots__=('__thread_target','__thread_num','__thread_args')

    def __init__(self):
        self.__thread_target=None
        self.__thread_num=None
        self.__thread_args=()

    def get_thread_target(self):
        return self.__thread_target


    def get_thread_num(self):
        return self.__thread_num


    def get_thread_args(self):
        return self.__thread_args


    def set_thread_target(self, value):
        self.__thread_target = value


    def set_thread_num(self, value):
        self.__thread_num = value


    def set_thread_args(self, value):
        self.__thread_args = value

    thread_target = property(get_thread_target, set_thread_target, None, None)
    thread_num = property(get_thread_num, set_thread_num, None, None)
    thread_args = property(get_thread_args, set_thread_args, None, None) 
        
    def create_thread_pool(self):
        '''
        创建线程池
        '''
        for i in range(self.__thread_num):
            thread_worker=threading.Thread(target=self.__thread_target,name="thread%d" %i,args=self.__thread_args)
            thread_worker.setDaemon(True)
            thread_worker.start()    

        
        
        
        
        
        
        
        
        

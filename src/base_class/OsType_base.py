#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月6日

@author: lichen
'''

import platform

class osType_base(object):
    '''
    检测操作系统信息
    '''
    
    #如果没有调用属性不存在，则会自动调用__getarr__方法
    def __getattr__(self,attr):
        if attr=="osx":
            return "osx"   
        elif attr=="rhel":
            return "redhat"
        elif attr=="ubu":
            return "ubuntu"
        elif attr=="sun":
            return "SunOS"
        elif attr=="centos":
            return "Centos"
        elif attr=="unknown_linux":
            return "unknown_linux"
        elif attr=="unknown":
            return "unknown"
        else:
            raise AttributeError,attr
        
    def linuxType(self):
        if platform.dist()[0]=="redhat":
            return self.rhel
        elif "buntu" in platform.uname()[4]:
            return self.ubu
        elif platform.dist()[0]=="centos":
            return self.centos
        else:
            return self.unknown_linux
    
    def queryOS(self):
        if platform.system()=="Darwin":
            return self.osx
        elif platform.system()=="Linux":
            return self.linuxType()
        elif platform.system()=="SunOS":
            return self.sun
        else:
            return self.unknown
    
    
    
    
    
    
    
    
        
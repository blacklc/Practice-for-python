#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月13日

@author: lichen
'''

import tarfile
import OS_operation_base.os_operation_base.reportAllFiles as reportAllFiles

class tar_base(object):
    '''
    归档常用操作类
    '''

    __slots__=('__filefullpath','__dirfullpath','__tartype','__tarfilefullpath')
    
    def __init__(self):
        self.__filefullpath=''
        self.__dirfullpath=''
        self.__tartype=''
        self.__tarfilefullpath=''
    
        
    def tarfile(self):
        '''
        归档单一文件
        '''
        tar=tarfile.open('%s.tar' %self.__filefullpath,'w',self.__tartype)
        tar.add(self.__filefullpath)
        tar.close()
        
    def tardir(self):
        '''
        归档某一目录
        '''
        tardir=tarfile.open('%s.tar' %self.__dirfullpath,'w',self.__tartype)
        allfiles=reportAllFiles
        for file1 in allfiles:
            tardir.add(file1)
        tardir.close()
    
    def tarlist(self):
        '''
        遍历某一归档文件,返回归档中的所有文件的全路径
        '''
        report=[]
        tarcontent=tarfile.open(self.__tarfilefullpath,"r")
        tarlist=tarcontent.getnames()
        for tarchlidfile in tarlist:
            tarchlidfile_fullpath="/"
            tarchlidfile_fullpath+=tarchlidfile
            report.append(tarchlidfile_fullpath)
        return report
        
        
        
        
        
        
        
        
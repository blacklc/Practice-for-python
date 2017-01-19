#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月12日

@author: lichen
'''

import os
import shutil
import time
import copy_reg
import types
import subprocess
import base_class.MD5_base as md5
from genericpath import getsize
from fnmatch import fnmatch
from multiprocessing import Pool
from random import uniform


def _pickle_method(m):
    '''
    用copy_reg将当前类注册为可序列化，以便进程池调用
    '''
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)

class os_operation_base(object):
    '''
    操作系统常用操作基础类
    '''

    '''
    def __init__(self, params):

    '''
        
    def reportAllFiles(self,path):
        '''
        遍历一个目录及其子目录下的所有文件(不包括文件夹) 
        '''
        files=[]
        for dirpath,dirnames,filenames in os.walk(path): #os.walk()返回的是一个生成器
            for file_name in filenames:
                file_fullpath=os.path.join(dirpath,file_name)
                files.append(file_fullpath)
        return files
    
    
    def returnAllDir(self,path):
        '''
        遍历一个目录及其子目录下的所有文件夹 
        '''
        Dir=[]
        for dirpath,dirnames,filenames in os.walk(path): #os.walk()返回的是一个生成器
            for dir_name in dirnames:
                dir_fullpath=os.path.join(dirpath,dir_name)
                Dir.append(dir_fullpath)
        return Dir 
    
    def compareByMD5(self,file1_fullpath,file2_fullpath):
        '''
        基于MD5的文件比对 
        '''
        file1=md5.MD5base()
        file2=md5.MD5base()
        file1.set_path(file1_fullpath)
        file2.set_path(file2_fullpath)
        if file1.create_checksum(file1.get_path())==file2.create_checksum(file2.get_path()):
            return True
        else:
            return False
    
    def GetfileSize(self,strPath):
        """
        获取指定文件大小
        """  
        if not os.path.exists(strPath):  
            """
            判断路径是否存在
            """
            return 0
  
        if os.path.isfile(strPath):  
            """
            判断是否是文件
            """
            return os.path.getsize(strPath)
    return 0  
    
    def get_dirSize(self,strPath):
        """
        获取指定目录大小
        """      
        nTotalSize = 0
        for strRoot, lsDir, lsFiles in os.walk(strPath):  
            #get child directory size  
            for strDir in lsDir:  
                nTotalSize = nTotalSize + self.GetfileSize(os.path.join(strRoot, strDir))
                #for child file size  
            for strFile in lsFiles:  
                nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strFile))
        return nTotalSize
        
    def findDupes(self,path):
        '''
        查找重复文件
        '''
        f=self.reportAllFiles(path)
        md5_file=md5.MD5base()
        dup=[]
        record={}
        for files1 in f:
            r_key=(getsize(files1),md5_file.create_checksum(files1))
            if r_key in record:
                dup.append(files1)
            else:
                record[r_key]=files1
        return dup   
    
    def deleteDupes(self,path):
        '''
        删除重复文件
        '''
        dupes=self.findDupes(path)
        for dupfile in dupes:
            try:
                status=os.remove(dupfile)
            except Exception,err:
                print err
            finally:
                return status    
        
    def interatcive(self,file_fullpath):
        '''
        删除文件(有用户确认)
        '''
        input=raw_input('你确定要删除 %s [N]/Y' %file_fullpath)
        if input.upper()=='Y':
            try:
                status=os.remove(file_fullpath)
            except Exception,err:
                print err
            finally:
                return status
        else:
            return -1
        
    def findfileByfilename(self,filename,dir_fullpath):
        '''
        依据文件名查找文件(文件名可为部分内容)
        '''
        report=[]
        f=self.reportAllFiles(dir_fullpath)    
        for files1 in f:
            if fnmatch(files1, filename):
                report.append(files1)
        return report
        
    def renamefilesbysuffix(self,dir_fullpath,old_suffix,new_suffix):   
        '''
        依据文件后缀名重命名文件
        '''
        f=self.reportAllFiles(dir_fullpath) 
        for files1 in f:
            if fnmatch(files1, '*.%s' %old_suffix):
                shutil.move(files1,'%s.%s' %(files1,new_suffix))
        
    def query_alive(self,machine_queue,alive_machineQueue):
        '''
        心跳检测主方法(并返回各主机丢包率)，需要配合run_multiprocess使用(基于ping,多进程)
        '''
        time.sleep(uniform(0, 2))
        ping_count=5
        while not machine_queue.empty():
            ip=machine_queue.get()
            ping_report=subprocess.Popen("ping -c %d %s" %(ping_count,ip),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            out=ping_report.stdout.readlines()
            for line in out:
                if line.find('packet loss')!=-1:
                    packet_loss_per=line.split(',',2)[2].split(' ')[1]
            if packet_loss_per!="100.0%":
                #print "%s is alive" %ip
                alive_machineQueue.put({ip:packet_loss_per})
            #else:
                #print "Don't find a response for %s" %ip
    
    def run_multiprocess(self,process_num,process_target,process_args):
        '''
        多进程执行方法
        '''
        #创建指定数量的进程池
        process_pool=Pool(processes=process_num)
        #指定并行执行的进程数量
        for i in range(process_num):
            process_pool.apply_async(process_target,args=process_args)
        process_pool.close()
        process_pool.join()
        
        
        
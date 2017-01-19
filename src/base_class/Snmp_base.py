#!/usr/bin/env python2.7
#coding:utf-8

'''
Created on 2016年6月30日

@author: lichen
'''

#from multiprocessing import Queue
import netsnmp
import time
import copy_reg
import types
from random import uniform
from multiprocessing import Pool

def _pickle_method(m):
    '''
    用copy_reg将当前类注册为可序列化，以便进程池调用
    '''
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)

class snmp_base(object):
    '''
    snmp相关操作基础类
    '''
    __slots__=("__oid","__version","__destHost","__community")

    def __init__(self):
       self.__oid=None
       self.__version=2
       self.__destHost=None
       self.__community="public"

    def get_community(self):
        return self.__community


    def set_community(self, value):
        self.__community = value


    def get_oid(self):
        return self.__oid


    def get_version(self):
        return self.__version


    def get_dest_host(self):
        return self.__destHost


    def set_oid(self, value):
        self.__oid = value


    def set_version(self, value):
        self.__version = value


    def set_dest_host(self, value):
        self.__destHost = value

    oid = property(get_oid, set_oid, None, None)
    version = property(get_version, set_version, None, None)
    destHost = property(get_dest_host, set_dest_host, None, None)
    community = property(get_community, set_community, None, None)
    
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

    def querySysInfo_By_snmpwalk(self):
        '''
        查询系统信息(基于snmpwalk方式)
        '''
        try:
            qurey_result=netsnmp.snmpwalk(self.__oid,Version=self.__version,DestHost=self.__destHost,Community=self.__community)
        except Exception,err:
            print "snmpget walk:",err
            qurey_result=None
        return qurey_result
    
    def querySysInfo_By_snmpwalk_ver_mp(self,desthost_queue,result_queue):
        '''
        查询系统信息(基于snmpwalk方式,多进程,需要配合run_multiprocess使用)
        '''
        time.sleep(uniform(0,2))
        while not desthost_queue.empty():
            result_map={}
            self.__destHost=desthost_queue.get()
            try:
                qurey_result=netsnmp.snmpwalk(self.__oid,Version=self.__version,DestHost=self.__destHost,Community=self.__community)
                print int(qurey_result[0])
            except Exception,err:
                print "snmpget walk:",err
                qurey_result=None
            result_map[self.__destHost]=qurey_result
            result_queue.put(result_map)
        
    def querySysInfo_By_snmpget(self):
        '''
        查询系统信息(基于snmpget方式)
        '''
        try:
            qurey_result=int(netsnmp.snmpget(self.__oid,Version=self.__version,DestHost=self.__destHost,Community=self.__community)[0])
        except Exception,err:
            print "snmpget error:",err
            qurey_result=None
        return qurey_result
        
    def querySysInfo_By_snmpget_ver_mp(self,desthost_queue,result_queue):
        '''
        查询内存相关信息(基于snmpget方式,多进程,需要配合run_multiprocess使用)
        ''' 
        time.sleep(uniform(0,2))
        while not desthost_queue.empty():
            result_map={}
            self.__destHost=desthost_queue.get()
            try:
                qurey_result=netsnmp.snmpget(self.__oid,Version=self.__version,DestHost=self.__destHost,Community=self.__community)
            except Exception,err:
                print "snmpget error:",err
                qurey_result=None
            result_map[self.__destHost]=qurey_result
            result_queue.put(result_map)
    
    def get_machineStorageUsed(self,alive_machineList,manager):
        '''
        获取集群各主机存储使用率(基于snmpget方式,多进程,需要配合run_multiprocess使用)
        '''
        result_list=[]
        alive_machine=manager.Queue()
        snmp_resultQueue=manager.Queue()
        for am in alive_machineList:
            alive_machine.put(am)
        self.oid=".1.3.6.1.4.1.2021.9.1.9.1"
        self.run_multiprocess(4,self.querySysInfo_By_snmpget_ver_mp,(alive_machine,snmp_resultQueue))
        while not snmp_resultQueue.empty():
            result_map=snmp_resultQueue.get()
            result_list.append(result_map)
        return result_list
            #for key in result_map:
                #print "Host %s's Percentage of space used on disk:%d%%" %(key,int(result_map[key][0]))

    def get_machineAvalaibleSpace(self,alive_machineList,manager):
        '''
        获取集群各主机剩余空间(基于snmpget方式,多进程,需要配合run_multiprocess使用)
        '''
        result_list=[]
        alive_machine=manager.Queue()
        snmp_resultQueue=manager.Queue()
        for am in alive_machineList:
            alive_machine.put(am)
        self.oid=".1.3.6.1.4.1.2021.9.1.7.1"
        self.run_multiprocess(4,self.querySysInfo_By_snmpget_ver_mp,(alive_machine,snmp_resultQueue))
        while not snmp_resultQueue.empty():
            result_map=snmp_resultQueue.get()
            result_list.append(result_map)
        return result_list
            #for key in result_map:
                #print "Host %s's Avalaible Space:%dG" %(key,int(result_map[key][0])/(1024*1024))

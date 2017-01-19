#!/usr/bin/env python2.7
#coding:utf-8

'''
Created on 2016年7月12日

@author: lichen
'''

import multiprocessing as mp
import time
from multiprocessing import Manager
import subprocess

def query_alive(machine_queue,alive_machineQueue):
    '''
    心跳检测主方法，需要配合run_multiprocess使用(基于ping,多进程)
    '''
    while True:
        time.sleep(.1)
        if machine_queue.empty():
            break
        ip=machine_queue.get()
        ret=subprocess.call("ping -c 1 %s" %ip,shell=True,stdout=open("/dev/null","w"),stderr=subprocess.STDOUT)
        if ret==0:
            print "%s is alive" %ip
            alive_machineQueue.put(ip)
        else:
            print "Don't find a response for %s" %ip

def foo_pool(x):
    time.sleep(2)
    return x*x

result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback():
    manager=Manager()
    all_machine=manager.Queue()
    alive_machine=manager.Queue()
    snmp_resultQueue=manager.Queue()
    all_machine.put("172.16.5.137")
    all_machine.put("172.16.5.133")
    all_machine.put("10.8.4.237")
    pool = mp.Pool()
    for i in range(10):
        pool.apply_async(query_alive, args=(all_machine,alive_machine), callback = log_result)
    print(result_list)
    pool.close()
    pool.join()
    print(result_list)

if __name__ == '__main__':
    apply_async_with_callback()
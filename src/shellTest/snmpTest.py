#!/usr/bin/env python2.7
#coding:utf-8

'''
Created on 2016年6月30日

@author: lichen
'''

import optparse
import base_class.OS_operation_base as os_operationbase
import base_class.Snmp_base as snmpbase
from multiprocessing import Manager

def main():
    manager=Manager()
    all_machine=manager.Queue()
    alive_machine=manager.Queue()
    snmp_resultQueue=manager.Queue()
    o=os_operationbase.os_operation_base()
    s=snmpbase.snmp_base()
    #创建命令行工具
    p=optparse.OptionParser(description="A tool that check machines",
                            prog="Daliycheck",
                            version="Daliycheck 1.0",
                            usage="usage:%prog [options] ip1 ip2...")
    p.add_option("--o","--oid",help="set oid [default=%default]",default=".1.3.6.1.2.1.25.2.3.1.6",dest="oid")
    p.add_option("--sv","--snmpversion",type="int",help="set snmp version [default=%default]",default="2",dest="snmp_version")
    p.add_option("--c","--community",help="set snmp community [default=%default]",default="public",dest="community")
    options,arguments=p.parse_args()
    #获取ip list
    if arguments:
        iplist_length=len(arguments)
    for i in range(iplist_length):
        all_machine.put(arguments[i])
    #心跳检测
    o.run_multiprocess(2,o.query_alive,(all_machine,alive_machine))
    #查询机器信息
    s.oid=options.oid
    s.version=options.snmp_version
    s.community=options.community
    s.run_multiprocess(2, s.querySysInfo_By_snmpget_ver_mp,(alive_machine,snmp_resultQueue))
    while not snmp_resultQueue.empty():
        result_map=snmp_resultQueue.get()
        for key in result_map:
            print "Host %s's Total memory:%dM" %(key,int(result_map[key][0])/1024)

if __name__ == '__main__':  
    main()


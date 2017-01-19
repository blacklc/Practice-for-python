#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月24日

@author: lichen
'''

import base_class.File_base
import matplotlib.pyplot
import shelve

def dictify_logline(line):
    '''
    切割日志，并格式化
    '''
    split_log=line.split(' ',7)
    timestr='/'.join([split_log[0],split_log[1],split_log[2]])
    return{'time':timestr,
           'user':split_log[3],
           'permission':split_log[5],
           split_log[6]:split_log[7]
    }

def log_report(logpath):
    '''
    生成分析报告
    '''
    report_dict={}
    logfile=base_class.File_base.file_base()
    logfile.set_path(logpath)
    content=logfile.readlinesfile()
    for member in content:
        menber_dict=dictify_logline(member)
        time=menber_dict['time']
        menber_dict.pop('time')
        report_dict.setdefault(time,[]).append(menber_dict)
    return report_dict

def createImage(infile):
    logreport=log_report(infile)
    time=[key for key in logreport]
    command=[value[0]['CMD'] for value in logreport.itervalues()]
    
def main():
    logreport=log_report('/Users/lichen/Documents/workspace/PythonTest/testfile/syslog')
    print '分析报告为：'
    for key,value in logreport.iteritems():
        print key,':',value
    
main()
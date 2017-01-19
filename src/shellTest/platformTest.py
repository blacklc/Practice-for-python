#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月6日

@author: lichen
'''

import platform
import base_class.OsType_base as osinfo

'''
profile=[
         platform.architecture(),
         platform.dist(),
         platform.libc_ver(),
         platform.mac_ver(),
         platform.machine(),#返回系统位数
         platform.node(),#返回主机名
         platform.platform(),#返回机器有用信息
         platform.processor(),#返回处理器版本
         platform.python_build(),
         platform.python_version(),#返回python版本
         platform.python_compiler(),#返回编译器信息
         platform.system(),#返回操作系统名称
         platform.uname(),#返回操作系统相关信息
         platform.version()#返回内核版本等信息
        ]
print "部分系统信息："
for info in profile:
    print info
'''

#匹配操作系统
ostype=osinfo.osType_base()
print "当前操作系统为：",ostype.queryOS()





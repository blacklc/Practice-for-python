#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月1日

@author: lichen
'''

import sys
import time
from subprocess import call

sourcedir='/Users/lichen/Desktop/test-copy/test_1'
destinationdir='/Users/lichen/Desktop/test-copy/rsync'
commandstring='rsync'
argument='-a'
cmd='%s %s %s %s' %(commandstring,argument,sourcedir,destinationdir) 

#一直进行同步，直到到同步结束为止
def sync():
    ret=call(cmd,shell=True)
    if ret!=0:
        print 'sync failed,after 30sec will retry rsync'
        time.sleep(30)
        #sys.exit(1)
    print 'sync sucessful'
    sys.exit(0)
sync()
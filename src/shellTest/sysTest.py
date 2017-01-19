#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月19日

@author: lichen
'''
import sys

linenumber=1
while  True:
    line=sys.stdin.readline()
    if not line:
        break
    print "line%d: %s" %(linenumber,line)
    linenumber+=1
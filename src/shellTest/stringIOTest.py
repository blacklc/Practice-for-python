#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月19日

@author: lichen
'''

from StringIO import StringIO

testString=StringIO('this is line 1.\nthis is line 2.\nthis is line 3.\nthis is line 4.\n')
print testString.readline() 
print testString.readline() 
print testString.read()
#!/usr/bin/env python2.7
#coding:utf-8

'''
Created on 2016年7月5日

@author: lichen
'''

from multiprocessing import Pool

def print_str1(str1):
    print "**********"+str1

def aaa():
    p=Pool(processes=2)
    for i in range(4):
        p.apply_async(print_str1,("%d" %i))
        #p.apply(print_str,("%d" %i))
    p.close()
    p.join()
  
aaa()
print "end"
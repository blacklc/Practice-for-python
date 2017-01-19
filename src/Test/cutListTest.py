#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#切片特性
#初始化list
def makeList(n):
    r=[]
    for i in range(n):
        r.append(i)
    return r

m=makeList(10)
print 'list content is',m
print 'qie pian m[0:3] hou,list:',m[0:3] #数字1表示从索引几开始取；数字2表示取到索引几但不包括该索引；数字3表示步长
print 'qie pian m[2:4] hou,list:',m[1:4]
print 'qie pian m[:6:2] hou,list:',m[:6:2]
print 'qie pian m[::2] hou,list:',m[::2]

L1 = [1, 2, 3, 4,5]
L2 = [20, 30, 40,50,60,70]
L1[len(L1):len(L1)] = L2
print L1
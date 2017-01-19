#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#遍历dict(map/key-value)
#初始化dict
def adddict():
    map11={}
    i=0
    for i in range(5):
        map11[i]=i+1
    return map11

map111=adddict()
#默认是遍历dict中的key字段
print 'the key in map are:',
for key in map111:
    print key,
print '\n'+'the value in map are:',
for value in map111.itervalues():
    print value,
print '\n'+'the item in map are:',
for key,value in map111.iteritems():
    print '{%d:%d} ' %(key,value)
    
#迭代
#初始化map
def makemap(n):
    map2={}
    for x in range(n):
        y=x-1
        map2[x]=y
    return map2

map22=makemap(5)
print 'the keys in map are ',
for key in map22:
    print key,
print '\n'+'the values in map are ',
for values in map22.itervalues():
    print values,
print '\n'+'the map ={',
for key in map22:
    print key,':',map22[key],',',
print '}'
print 'print map=',map22
#判断是否可迭代
from collections import Iterable
boolean=isinstance(map22, Iterable)
print '判断结果为：',boolean

#对list遍历。原理为生成list的索引
#初始化list
def makeList(n):
    r=[]
    for i in range(n):
        r.append(i)
    return r

listm=makeList(10)
print 'before add,list mumbers are',listm
#对list遍历。原理为生成list的索引
for i,values in enumerate(listm):
    listm[i]=listm[i]+1
print 'after add,list mumbers are',listm



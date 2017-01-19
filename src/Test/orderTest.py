#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#排序
ll=[4,2,7,8,9]
print 'before 排序,the list\'s members are',ll
ll2=sorted(ll)
print 'after 排序,the list \'s members are',ll2

#自定义排序
def zdypx(x,y):
    #针对字母排序忽略大小写,原理为全部都转换成大写或者小写即可
    if 'A'<x<'z' and 'A'<y<'z':
        x=x.upper()
        y=y.upper()
    if x<y:
        return -1
    elif x==y:
        return 0
    else:
        return 1

ll3=['D','A','F','Z','h','y','l',2,5,3,8,5,'O','b']
print 'before 排序,the list\'s members are',ll3
ll4=sorted(ll3,zdypx)
print 'after 排序,the list \'s members are',ll4
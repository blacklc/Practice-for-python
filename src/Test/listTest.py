#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''

arr1=['name1','name2',1]
arrlength=len(arr1)
print('the arr1 member is %s,%s and %d') %(arr1[0],arr1[1],arr1[2])
arr1.append('new')
print('the new member is %s') %(arr1[-1])
#insert中填写的位置是数组下标，不是真实的位数
arr1.insert(3,4)
print('the new insert member is %d') %(arr1[3])
print 'the last member is',arr1[-1]
arr1.pop()
print 'after pop,the last member is',arr1[-1]
print arr1
arr1.pop(1)
print 'after pop(1),the list member is',arr1
arr2=[1,2,3,4,5,6]
arr1.append(arr2)
print 'after add other list,the list member is',arr1
print  'the arr2[0]=',arr1[3][0],'\n'
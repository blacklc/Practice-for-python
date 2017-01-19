#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''
#逻辑判断
arr1=['name1','name2',1]
i=10
#在录入数字的时候使用input，在录入字符串的时候使用raw_input
#n=input('please enter a number:')
#或者使用强制类型转换
n=int(raw_input('please enter a number:'))
if n >= i:
    print "the number >10"
elif n==6:
    print "the number=6"
else:    
    if n==4:
        print "the number=4 \n"
    else:
        print "the number !=6 and !=4 \n"
for member in arr1:
        print member,
arr3=range(1,6)
print "range list is"+'\n',arr3
m=4
sum1=0
while m>0:
    sum1=sum1+m
    m=m-1
print 'sum=%d\n' %(sum1)


#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月11日

@author: lichen
'''

map1={'stu1':1,'stu2':2,'stu3':3}
print 'stu1\'s number=%d' %(map1['stu1'])
map1['stu2']=5
print map1
stuname=raw_input('please enter the student\'s name:')
if stuname in map1:
    print 'student '+stuname+' number=%d\n' %(map1[stuname])
else:
    print 'student '+stuname+' not int map1\n'
print 'stu1\'s number=',map1.get('stu1')
print 'before pop,map1 member are',map1
a=map1.pop('stu3')
print a
print 'after pop.map1 memeber are',map1
print 'before add,map1 member are',map1
map1['stu4']=4
print 'after add,map1 member are',map1,'\n'

    
    
    
    
    
    
    
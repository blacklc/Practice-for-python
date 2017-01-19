#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月23日

@author: lichen
'''

import xml.etree.ElementTree

xmlfile='/Users/lichen/Documents/workspace/PythonTest/testfile/sysinfo.xml'
xmlobject=xml.etree.ElementTree.parse(xmlfile)
print xmlobject

first_filter=xmlobject.find('./array/dict')
print first_filter.find('dict').find('key').text

for d in xmlobject.findall('./array/dict'):
    if d.find('array').find('dict').find('string').text=='Safari':
        print d.find('array').find('dict').findall('string')
        


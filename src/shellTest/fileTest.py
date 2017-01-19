#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月18日

@author: lichen
'''

import base_class.File_base

def main ():
    f=base_class.File_base.filebase()
    f.set_path('/Users/lichen/Desktop/python/tmp.log')
    f.readallfile() 
    f.addcontent('this is new add string')
    print '修改文件后,',
    f.readallfile(1) 
    print '按行读取文件'
    f.readlinefile(2)
    print '读取文件的所有行'
    f.readlinesfile(2)
main()
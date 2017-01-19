#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月3日

@author: lichen
'''
import tarfile
import os

#归档指定文件
print '压缩前：'
for path in os.listdir('/Users/lichen/Desktop/HIS/'):
    re='中间层安装更新手册及规范' in path
    if re:
        print path
tar=tarfile.open('/Users/lichen/Desktop/HIS/中间层安装更新手册及规范.tar','w')
tar.add('/Users/lichen/Desktop/HIS/中间层安装更新手册及规范.docx')
tar.close()
print '压缩后：'
for path in os.listdir('/Users/lichen/Desktop/HIS/'):
    re='中间层安装更新手册及规范' in path
    if re:
        print path
        
#归档整个目录
print '压缩前：'
for path in os.listdir('/Users/lichen/Desktop'):
    re='HIS' in path
    if re:
        print path
tardir=tarfile.open('/Users/lichen/Desktop/HIS.tar','w','')
for dirpath,dirnames,filenames in os.walk('/Users/lichen/Desktop/HIS'): #os.walk()返回的是一个生成器
    for file_name in filenames:
        file_fullpath=os.path.join(dirpath,file_name)
        tardir.add(file_fullpath)
tardir.close()
print '压缩后：'
for path in os.listdir('/Users/lichen/Desktop'):
    re='HIS' in path
    if re:
        print path

#使用bzip2归档
print '压缩前：'
for path in os.listdir('/Users/lichen/Desktop/HIS/'):
    re='中间层安装更新手册及规范' in path
    if re:
        print path
tar=tarfile.open('/Users/lichen/Desktop/HIS/中间层安装更新手册及规范.tar.bzip2','w|bz2')
tar.add('/Users/lichen/Desktop/HIS/中间层安装更新手册及规范.docx')
tar.close()
print '压缩后：'
for path in os.listdir('/Users/lichen/Desktop/HIS/'):
    re='中间层安装更新手册及规范' in path
    if re:
        print path

#使用gzip归档
print '压缩前：'
for path in os.listdir('/Users/lichen/Desktop/HIS/'):
    re='中间层安装更新手册及规范' in path
    if re:
        print path
tar=tarfile.open('/Users/lichen/Desktop/HIS/中间层安装更新手册及规范.tar.gzip','w|gz')
tar.add('/Users/lichen/Desktop/HIS/中间层安装更新手册及规范.docx')
tar.close()
print '压缩后：'
for path in os.listdir('/Users/lichen/Desktop/HIS/'):
    re='中间层安装更新手册及规范' in path
    if re:
        print path

#检测tar文件内容
tarcontent=tarfile.open("/Users/lichen/Desktop/HIS.tar","r")
print "tar文件内容："
tartotal=tarcontent.list()
print tartotal
print "tar文件名称：",tarcontent.name
tarlist=tarcontent.getnames()
print "tar文件内子文件名："
for tarchlidfile in tarlist:
    tarchlidfile_fullpath="/"
    tarchlidfile_fullpath+=tarchlidfile
    print tarchlidfile_fullpath
print "tar members:"
for member in tarcontent.members:
    print member
    
#解压
#tarcontent.extractall()










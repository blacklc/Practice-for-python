#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月26日

@author: lichen
'''

import os
import shutil
import filecmp
import base_class.MD5_base as md5
from genericpath import getsize
from fnmatch import fnmatch
from glob import glob

print '当前目录为：',os.getcwd()
print 'll /Users/lichen/Desktop:'
i=0
for path in os.listdir('/Users/lichen/Desktop'):
    print path
try:
    os.mkdir('/Users/lichen/Desktop/testdir')
except Exception,e:
    print str(e)
finally:
    try:
        if os.listdir('/Users/lichen/Desktop/testdir')==[]:
            print '新建目录为空'
        else:
            print os.listdir('/Users/lichen/Desktop/testdir')
    except Exception,e:
        print str(e)   
print os.stat('/Users/lichen/Desktop/testdir')
os.rename('/Users/lichen/Desktop/testdir','/Users/lichen/Desktop/testdir_rename')
os.rmdir('/Users/lichen/Desktop/testdir_rename')

#使用shutil模块
os.chdir('/Users/lichen/Desktop/') #使之后的程序执行位置都在一个特定目录下进行
try:
    os.makedirs('test/test_1/test_2',0777)
except Exception,e:
    print str(e)
finally:
    try:
        shutil.copytree('test','test-copy') #复制相同的目录树结构,并且复制目录中的数据
    except Exception,e:
        print str(e)
    finally:
        shutil.move('test','test-move') #移动数据树
        try:
            shutil.rmtree('test-move') #删除数据树
        except Exception,e:
            print str(e)
 
#遍历一个目录及其子目录下的所有文件(不包括文件夹)       
def reportAllFiles(path):
    files=[]
    for dirpath,dirnames,filenames in os.walk(path): #os.walk()返回的是一个生成器
        for file_name in filenames:
            file_fullpath=os.path.join(dirpath,file_name)
            files.append(file_fullpath)
    return files

def returnAllDir(path):
    Dir=[]
    for dirpath,dirnames,filenames in os.walk(path): #os.walk()返回的是一个生成器
        for dir_name in dirnames:
            dir_fullpath=os.path.join(dirpath,dir_name)
            Dir.append(dir_fullpath)
    return Dir 

files_path=reportAllFiles('/Users/lichen/Desktop/')
print '目录下所有文件：'
for i,v in enumerate(files_path):
    print files_path[i]
print '目录下所有目录：'
dir_name=returnAllDir('/Users/lichen/Desktop/')
for i,v in enumerate(dir_name):
    print dir_name[i]

#文件比较
print 'compare file0 and file1:',filecmp.cmp('/Users/lichen/Documents/workspace/PythonTest/testfile/file0', '/Users/lichen/Documents/workspace/PythonTest/testfile/file1')
print 'compare file0 and file00:',filecmp.cmp('/Users/lichen/Documents/workspace/PythonTest/testfile/file0', '/Users/lichen/Documents/workspace/PythonTest/testfile/file00')

#目录比较
print '目录比较结果中不同部分：'
#dircmp.diff_files仅对文件名相同的文件进行比较
print filecmp.dircmp("/Users/lichen/Documents/workspace/PythonTest/testfile","/Users/lichen/Documents/workspace/PythonTest/testfile/test2").diff_files
#dircmp.same_files仅对两个目录中相同文件进行报告
print '目录比较结果中相同部分：'
print filecmp.dircmp("/Users/lichen/Documents/workspace/PythonTest/testfile","/Users/lichen/Documents/workspace/PythonTest/testfile/test2").same_files
print '目录比较报告：'
print filecmp.dircmp("/Users/lichen/Documents/workspace/PythonTest/testfile","/Users/lichen/Documents/workspace/PythonTest/testfile/test2").report()
#set方法将队列转换为集合，之后使用集合运算来比较目录差异
print '利用集合运算比较目录内容：'
dirA=set(os.listdir("/Users/lichen/Documents/workspace/PythonTest/testfile"))
dirB=set(os.listdir("/Users/lichen/Documents/workspace/PythonTest/testfile/test2"))
print dirA-dirB
print dirB-dirA

#md5校验
md51=md5.MD5base()
md52=md5.MD5base()
md51.set_path('/Users/lichen/Documents/workspace/PythonTest/testfile/file0')
md52.set_path('/Users/lichen/Documents/workspace/PythonTest/testfile/test2/file1')
print 'md5校验：'
if md51.create_checksum(md51.get_path())==md52.create_checksum(md52.get_path()):
    print 'md51=md52,文件相同'
else:
    print '文件不相同'
    
#查找重复文件
def findDupes(path):
    f=reportAllFiles(path)
    md53=md5.MD5base()
    dup=[]
    record={}
    for files1 in f:
        r_key=(getsize(files1),md53.create_checksum(files1))
        if r_key in record:
            dup.append(files1)
        else:
            record[r_key]=files1
    return dup
dupes=findDupes('/Users/lichen/Documents/workspace/PythonTest/testfile/')
print '重复文件为：',dupes

#删除重复文件
def deleteDupes(path):
    dupes=findDupes(path)
    for dupfile in dupes:
        print 'deleting %s' %dupfile
        try:
            status=os.remove(dupfile)
        except Exception,err:
            print err
    return status

#删除文件(有用户确认)
def interatcive(file1):
    input=raw_input('你确定要删除 %s [N]/Y' %file1)
    if input.upper()=='Y':
        print 'deleting : %s' %file1
        try:
            status=os.remove(file1)
        except Exception,err:
            print err
            return status
    else:
        print 'skipping %s' %file1
        return status

#文件匹配
f=reportAllFiles('/Users/lichen/Documents/workspace/PythonTest/testfile')    
for files2 in f:
    if fnmatch(files2, '*.xml'):
        print files2
print glob('*')

#将制定类文件重命名
for files1 in f:
    if fnmatch(files1, '*.txt'):
        shutil.move(files1,'%s.mp3' %files1)
print '重命名后：'
for files23 in f:
    if fnmatch(files23, '*.mp3'):
        print files23











#!/usr/bin/env python
#coding=utf-8

'''
Created on 2017年1月22日

@author: lichen
'''

import os

ls=os.linesep #该方法返回一个代码运行的当前平台的换行符

def file_exist():
    """
    判断文件是否已存在
    
    :return fname 文件名
    :type   string
    """
    while True:
        fname = raw_input('请输入新建文件名:')
        if os.path.exists('/Users/lichen/Desktop/'+fname+'.txt'):
            print "文件'%s'已存在，请使用其他文件名" %(fname)
        else:
            break
    return fname
    
def read_userInput():
    """
    读取用户输入内容
    
    :return input 生成器 用户输入的每行内容
    """
    print "请输入文件每一行内容。使用回车表示完成当前行输入；使用.表示输入完毕."
    while True:
        input = raw_input('>')
        if input == '.':
            break
        else:
            yield input
    
def makeFile():
    """
    将用户输入的所有信息都保存在一个指定文件中
    """
    fname=file_exist() #判断创建文件是否已经存在
    try:
        file=open('/Users/lichen/Desktop/'+fname+'.txt','w')
    except IOError,e:
        print 'file make error:',e
        return None
    file.writelines(['%s%s' %(input,ls) for input in read_userInput()]) #读取用户输入内容
    file.close()

def readFile():
    """
    读取指定文件内容
    """
    fname=raw_input('请输入要读取的文件名:')
    while True:
        if not os.path.exists('/Users/lichen/Desktop/'+fname):
            print '文件不存在，请重新输入.'
        else:
            break
    try:
        file=open('/Users/lichen/Desktop/'+fname,'r')
    except IOError,e:
        print 'file open error:',e
        return None
    for output in file.readlines():
        print output,
    file.close()
    
if __name__ == '__main__':
    makeFile()
    readFile()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
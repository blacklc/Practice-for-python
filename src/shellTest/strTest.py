#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月16日

@author: lichen
'''

import subprocess

string1='This is string'

print 'the string1 type is',type(string1)
print 'And the string1 content is "',string1,'"'

#字符串转义
s='\n'
print '字符串转义：',s

#原始字符串
s1=r'\n'
print '原始字符串：',s1

#字符串包含
res=subprocess.Popen(['uname','-sv'],stdout=subprocess.PIPE)
uname=res.stdout.read().strip() #strip方法参数为空时用来删除空白符
print type(uname)
print '\n'+'command report is',uname
re='lichen' in uname
print 'lichen in report is',re
re1='Darwin' in uname
print 'Darwin in report2 is',re1
re2='lichen' not in uname
print 'lichen not in report is',re2

#字符串中查找，索引
#zein=uname.find('lichen')
zein=uname.find('Darwin')
if zein==-1:
    print ('不存在')
else:
    print '存在，并且索引为',zein
#zein2=uname.index('lichen')
zein2=uname.index('Version')
print '存在，并且索引为',zein2
#利用索引进行字符串剪切
print '切片之前为',uname
cutedlist=uname[zein2:]
print '切片过后为',cutedlist,'\n'

#删除字符串前空白，开始到结束中所有空白和后空白
teststr='\n\t this is test string\n \t\r'
print '原有字符串为',teststr
cutstr1=teststr.lstrip()
print '前导空白为',cutstr1
cutstr2=teststr.rstrip()
print '后导空白为',cutstr2
cutstr3=teststr.strip()
print '中间的所有空白',cutstr3

#删除字符串中的指定内容
teststr2='<teststr>'
delstr1=teststr2.lstrip('<')
print '删除左括号后为',delstr1
delstr2=teststr2.rstrip('>')
print '删除右括号后为',delstr2
delstr3=teststr2.strip('<>')
print '删除中间内容后为',delstr3

#大小写转换
teststr3=teststr2.upper()
print '大写化以后为',teststr3
teststr3=teststr2

#字符串切割
teststr4='post1,post2,post3'
cutlist=teststr4.split(',')
print '按逗号切割后为',
for cutcontent in cutlist:
    print '"',cutcontent,'"',
teststr5='this is a test string'
cutlist1=teststr5.split('a')
print '\n'+'按某一字符串切割后为',
for cutcontent in cutlist1:
    print '"',cutcontent,'"',
teststr6='this is test string1,this is test string2,this is test string3'
cutlist2=teststr6.split(',',1)
print '\n'+'控制切割次数后为',
for cutcontent in cutlist2:
    print '"',cutcontent,'"',
#teststr5='May 20 06:55:01 vmwelcome-you CRON[13438]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)'
cutlist3=teststr5.split(' ',7)
print '\n'+'默认是按空格切割',
for cutcontent in cutlist3:
    print '"',cutcontent,'"',
teststr7='''this is test string,
is to long,
the string has too many lines.
'''
cutlinelist=teststr7.splitlines()
print '\n'+'处理多行文本为',
for cutcontent in cutlinelist:
    print '"',cutcontent,'"',
print '\n'+'之后在对每行进行切割',
for line in cutlinelist:
    print '这一行的单词为',
    for cutcontent in line.split():
        print '"',cutcontent,'"',

#字符串拼接
a='this is '
b='test string'
a+=b
print '\n\n',a
listcontent=['str1','str2','str3','str4']
joinlist1=','.join(listcontent)
print '用逗号拼接为',joinlist1
joinlist2=' '.join(listcontent)
print '用空格拼接为',joinlist2

#字符串替换
print '替换之前字符串内容为',teststr5
updatelist=teststr5.replace('test', 'update')
print '替换后内容为',updatelist




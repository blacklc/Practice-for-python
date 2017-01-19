#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月2日

@author: lichen
'''

from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.orm import mapper,sessionmaker
import os

#创建表映射类
class filesystem_class(object):
    def __init__(self,id,path,file):
        self.id=id
        self.path=path
        self.file=file
    
    def __repr__(self):
        return 'filesystem("%s","%s")' %(self.path,self.file)

#创建数据库引擎
engine=create_engine('sqlite:///:memory:',echo=False)

#创建元数据实例和创建表
metadata=MetaData()
f_table=Table('filesystem',metadata,
              Column('id',Integer,primary_key=True,),
              Column('path',String(10000)),
              Column('file',String(10000)),
              )
metadata.create_all(engine)

#将类映射到表中
mapper(filesystem_class,f_table)

#创建数据库会话
Session=sessionmaker(bind=engine,autoflush=True)
session=Session()

#完成常规操作
path='/Users/lichen/Desktop/'
path_unicode=unicode(path) #sqlite推荐使用unicode存储字符串
i=0
for dirpath,dirnames,filenames in os.walk(path_unicode): #os.walk()返回的是一个生成器。同时，os.walk传入的path是unicode，返回的信息也是unicode
    for file_name in filenames:
        file_fullpath=os.path.join(dirpath,file_name)
        record=filesystem_class(i,file_fullpath,file_name)
        session.add(record)
        i=i+1

#提交数据库操作
session.commit()

#从数据库中查询操作结果
print 'database record:'
for rec in session.query(filesystem_class):
    print 'id:%s,path:%s,file:%s' %(rec.id,rec.path,rec.file)









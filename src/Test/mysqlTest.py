#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年7月15日

@author: lichen
'''

import base_class.SQL_MYSQL_base as mysql_base

def main():
    #创建数据库连接
    #ms=mysql_base.SQL_MYSQL_base("root","123456","test")
    ms=mysql_base.SQL_MYSQL_base("root","123456","DaliyCheck")
    """
    #创建表格
    sql_create_table="create table test1 (id int(100) primary key NOT NULL AUTO_INCREMENT,name varchar(10) DEFAULT NULL,text varchar(100) DEFAULT NULL)"
    if ms.create_table(sql_create_table):
        print "create table sucessful"
    """
    
    """
    #插入数据
    sql_insert1="insert into test1 (name,text) values ('test1','11111111111111')"
    sql_insert2="insert into test1 (id,name,text) values (%s,%s,%s)"
    data2=(2,"test2","2222222")
    sql_insert3="insert into test1 (id,name,text) values (%(id)s,%(name)s,%(text)s)"
    data3={"id":3,"name":"test3","text":"33333333"}
    if ms.insert_data(sql_insert3,data3):
        print "insert sucessful"
    """
    
    """
    #查询数据
    sql_query1="select * from test1 where id=1"
    sql_query2="select * from test1 where id=%s"
    data2=(1,)
    sql_query3="select * from test1 where id<%s"
    data3=(4,)
    query_list=ms.query_data(sql_query2,data2)
    print query_list
    """
    sql="select * from DC_MachineInfo where hostname like 'ehr%'"
    sql2="select * from DC_MachineInfo where hostname like %s"
    data=("%s%%"%("ehr"),)
    query_list=ms.query_data(sql2,data)
    for result in query_list:
        id=result[0]
        ip=result[1]
        hostname=result[2]
        query_date=result[3]
        alivespace=result[4]
        used=result[5]
        print id,ip,hostname,alivespace,used
    """
    #删除数据
    sql_delete1="delete from test1 where name='test3'"
    sql_delete2="delete from test1 where id=%s"
    data2=(2,)
    if ms.delete_data(sql_delete2,data2):
        print "delete sucessful"
    """
    """
    #修改数据
    sql_update="update test1 set text='33333333' where id=1"
    sql_update2="update test1 set text=%s where id=%s"
    data=("222222222",1)
    if ms.update_data(sql_update2,data):
        print "update sucessful"
    """
    
    ms.connect_close()
main()










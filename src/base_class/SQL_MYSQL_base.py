#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年7月15日

@author: lichen
'''

import mysql.connector

class SQL_MYSQL_base(object):
    '''
    基于mysql.connector驱动的MYSQL相关操作类
    '''
    
    __slots__=("__conn",)

    def __init__(self,p_user,p_password,p_database,p_host="localhost",p_port=3306,p_charset="utf8"):
        """
        创建数据库连接
        """
        try:
            self.__conn=mysql.connector.connect(host=p_host,user=p_user,password=p_password,database=p_database,port=p_port,charset=p_charset)
        except mysql.connector.Error as e:
            print('Connect fails!{}'.format(e))
    
    def connect_close(self):
        """
        关闭数据库连接
        """
        self.__conn.close()
            
    def create_table(self,sql):
        """
        创建表格
        """
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print('Create Table fails!{}'.format(e))
            cursor.close()
            return False
        
    def insert_data(self,sql,data=None):
        """
        插入单条数据
        """    
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql,data)
            self.__conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print('Insert Data fails!{}'.format(e))
            cursor.close()
            return False
        
    def insert_many_data(self,sql,data=None):
        """
        插入多条数据
        """  
        try:
            cursor = self.__conn.cursor()
            cursor.executemany(sql,data)
            self.__conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print('Insert Many Data fails!{}'.format(e))
            cursor.close()
            return False
        
    def query_data(self,sql,data=None):
        """
        查询数据
        """
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql,data)
            remaining_rows = cursor.fetchall()
            cursor.close()
            if len(remaining_rows)==0:
                print "Don't query any data."
                return remaining_rows
            else:
                return remaining_rows
        except mysql.connector.Error as e:
            print('Query Data fails!{}'.format(e))
            cursor.close()
            return False
        
    def delete_data(self,sql,data=None):
        """
        删除数据
        """   
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql,data)
            self.__conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print('Delete Data fails!{}'.format(e))
            cursor.close()
            return False
        
    def update_data(self,sql,data=None):
        """
        修改数据
        """     
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql,data)
            self.__conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print('Update data fails!{}'.format(e))
            cursor.close()
            return False
        
        
        
        
        
        
        
        
        
        
        

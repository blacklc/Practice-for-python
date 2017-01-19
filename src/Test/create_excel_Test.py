#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年7月20日

@author: lichen
'''

import time
import xlsxwriter as xw
import base_class.SQL_MYSQL_base as mysql_base

def create_excel(system_list,_database):
    bg_color={"EHR":"CCFFCC","TEST":"CCFFFF"}
    #建立游标
    cursor=1
    #创建excel文件
    report_path="/Users/lichen/Desktop/"
    report_fullpath=report_path+"DaliyCheck_report-"+time.strftime("%Y-%m-%d")+".xlsx"
    workbook=xw.Workbook(report_fullpath)
    #在文件中新建一个sheet
    worksheet=workbook.add_worksheet("test_sheet")
    #设置格式
    title_format=workbook.add_format()
    title_format.set_align("vcenter") 
    title_format.set_align("center")
    title_format.set_bg_color("FFCC99")
    title_format.set_border()
    detail_fromat=workbook.add_format()
    detail_fromat.set_align("vcenter") 
    detail_fromat.set_align("center")
    detail_fromat.set_border()
    #设置行格式
    worksheet.set_column("A:F",15)
    #写入指定单元格(若增加新列务必要修改后边的列数迭代处)
    worksheet.write(0,0,"System",title_format)
    worksheet.write(0,1,"IP",title_format)
    worksheet.write(0,2,"HostName",title_format)
    worksheet.write(0,3,"Date",title_format)
    worksheet.write(0,4,"AvalaibleSpace",title_format)
    worksheet.write(0,5,"StorgeUesd",title_format)
    for name in system_list:
        sql_query="select * from DC_MachineInfo where hostname like %s"
        sql_data=("%s%%"%name,) 
        result_list=_database.query_data(sql_query,sql_data)
        result_number=len(result_list)
        #合并单元格
        system_name_format=workbook.add_format()
        system_name_format.set_align("vcenter") 
        system_name_format.set_align("center")
        system_name_format.set_bg_color(bg_color[name])
        system_name_format.set_border()
        worksheet.merge_range(cursor, 0, cursor+result_number-1, 0, name,system_name_format)
        z=result_number
        #将结果写入表中
        #行数迭代
        for i in range(cursor,cursor+result_number):
            #查询结果迭代
            z=z-1
            #列数迭代
            for y in range(1,6):
                    worksheet.write(i,y,result_list[z][y],detail_fromat)
        cursor=cursor+result_number
    workbook.close()

def main():
    system_list=["EHR","TEST"]
    m=mysql_base.SQL_MYSQL_base(p_user="root",p_password="123456",p_database="DaliyCheck")
    create_excel(system_list,m)
    
if __name__ == '__main__':
    main()
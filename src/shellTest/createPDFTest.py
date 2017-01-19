#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月24日

@author: lichen
'''

import subprocess
import reportlab.pdfgen.canvas

from datetime import datetime
from reportlab.lib.units import inch

def disk_report(command):
    p=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
    return p.stdout.readlines() #将命令输出的每行内容组成一个list作为返回值

def createpdf(content,filename):
    try:
        path='/Users/lichen/Desktop/'
        path+=filename
        c=reportlab.pdfgen.canvas.Canvas(path)
        c.drawString(250,800,content) #参数分别为x,y,内容
        c.showPage()
        c.save()
        print '创建成功'
    except Exception,e:
        print '创建失败，原因为：',str(e)

def create_reportPDF(content,filename):
    try:
        path='/Users/lichen/Desktop/'
        path+=filename
        now_time=datetime.today() #获取当前时间
        format_time=now_time.strftime("%h %d %Y %H:%M:%S") #格式化时间
        c=reportlab.pdfgen.canvas.Canvas(path)
        textcontent=c.beginText() #创建一个textobject对象(文本对象)
        textcontent.setTextOrigin(inch,11*inch) #定义在文档的11英寸处开始输出
        textcontent.textLine('''
        Storage informantion report: %s
        ''' %format_time)        #将字符串写入文本对象
        for line in content:
            textcontent.textLine(line.strip()) #将字符串写入文本对象，使用strip()删除换行字符
        c.drawText(textcontent)  #绘制文本内容
        c.showPage()             #停止绘制
        c.save()
        print '创建成功'
    except Exception,e:
        print '创建失败，原因为：',str(e) 

def main():
    content='This is test pdf'
    filename='test.pdf'
    command='df -h'
    #createpdf(content, filename)
    info=disk_report(command)
    create_reportPDF(info,filename)
    
main()



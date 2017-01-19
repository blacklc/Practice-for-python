#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年12月23日

@author: lichen
'''

import numpy as np

def plus():
    a=1
    result=0
    result_list=[]
    result_dlist=[]
    #计算每一个d的结果
    for d in np.arange(0,0.08,0.001):
        #计算(1+d)^n之和
        for p in range(120):
            a=1
            #计算(1+d)^n
            for n in range(p+1):
                #print "n=",n
                a=(1+d/12)*a
            #print "p=",p+1,"阶乘＝",a
            result=result+a
        #print "d=",d,"result=",result
        result_dlist.append(d)
        result_list.append(result)
        result=0
    return result_dlist,result_list
        
def main():
    dl,l=plus()
    for d,result in zip(dl,l):
        #print "d=",d,"result=",result
        if result<=151.2:
            min=result
            min_d=d
        else:
            max=result
            print "min=",min,"max=",max
            print "d=",min_d,"result=",min
            return None
        
main()
    
            



























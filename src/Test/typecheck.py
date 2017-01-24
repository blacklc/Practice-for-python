#!/usr/bin/env python
#coding:utf-8

'''
Created on 2017年1月24日

@author: lichen
'''

from types import IntType,LongType,FloatType,ComplexType

def checkNumType(num):
    """
    检查输入参数类型是否为数值类型
    
    :param  num
            待检查参数
    
    :return None
    """
    if isinstance(num,(IntType,LongType,FloatType,ComplexType)):
        print num,'is','a number of type:',type(num).__name__
    else:
        print num,"isn't a number type"
        
if __name__ == '__main__':
    checkNumType('SKDFJWKEFSLDKF')
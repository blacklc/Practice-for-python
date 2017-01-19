#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年5月19日

@author: lichen
'''

import urllib

uf=urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738281887b88350bd21544e6095d55eaf54cac23f000")
urlcontent=uf.read()
uf.close()
print urlcontent
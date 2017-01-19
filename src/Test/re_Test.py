#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年11月29日

@author: lichen
'''

import re

def match_test(re_string,match_string):
    """
    re.match方法使用示例
    
    :param  re_string
            正则表达式
    :param  match_string
            需匹配文本
    
    :return result 匹配结果
    """
    pattern=re.compile(re_string) #将正则表达式编译成pattern对象
    result=re.match(pattern,match_string) #进行正则匹配并生成匹配结果(match对象)
    if result:
        print "m.string:", result.string #返回被匹配的文本
        print "m.re:", result.re #返回匹配时使用的pattern对象
        print "m.pos:", result.pos #文本中正则表达式开始搜索的索引
        print "m.endpos:", result.endpos #文本中正则表达式结束搜索的索引
        print "m.lastindex:", result.lastindex #最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None
        print "m.lastgroup:", result.lastgroup #最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
        print "m.group():", result.group() #获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
        print "m.group(1,2):", result.group(1, 2)#以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
        print "m.groups():", result.groups() #返回所有组，以list形式
        print "m.groupdict():", result.groupdict() #返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
        print "m.start(2):", result.start(2) #返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
        print "m.end(2):", result.end(2) #返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
        print "m.span(2):", result.span(2) #返回(start(group), end(group))。
        print r"m.expand(r'\g \g\g'):", result.expand(r'\2 \1\3') #将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。
    return result

def search_test(re_string,match_string):
    """
    re.search方法使用示例
    
    :param  re_string
            正则表达式
    :param  match_string
            需匹配文本
    
    :return result 匹配结果
    """
    pattern=re.compile(re_string) #将正则表达式编译成pattern对象
    result=re.search(pattern,match_string) #进行正则匹配并生成匹配结果(match对象)
    if result:
        print "m.string:", result.string #返回被匹配的文本
        print "m.re:", result.re #返回匹配时使用的pattern对象
        print "m.pos:", result.pos #文本中正则表达式开始搜索的索引
        print "m.endpos:", result.endpos #文本中正则表达式结束搜索的索引
        print "m.lastindex:", result.lastindex #最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None
        print "m.lastgroup:", result.lastgroup #最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
        print "m.group():", result.group() #获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；截获了多次的组返回最后一次截获的子串。
        print "m.group(1,2):", result.group(1, 2)#以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None。
        print "m.groups():", result.groups() #返回所有组，以list形式
        print "m.groupdict():", result.groupdict() #返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内。default含义同上。
        print "m.start(2):", result.start(2) #返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
        print "m.end(2):", result.end(2) #返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
        print "m.span(2):", result.span(2) #返回(start(group), end(group))。
        print r"m.expand(r'\g \g\g'):", result.expand(r'\2 \1\3') #将匹配到的分组代入template中然后返回。template中可以使用\id或\g、\g引用分组，但不能使用编号0。\id与\g是等价的；但\10将被认为是第10个分组，如果你想表达\1之后是字符’0’，只能使用\g0。
    return result

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

def main():
    result=match_test(r"(\w+) (\w+)(?P<sign>.)","hello world!") #match是从文本开头匹配，匹配成功一次就返回；遇第一个未匹配项就返回None;匹配如下内容：单词+空格+单词+任意字符
    if result:
        print "match匹配成功",result.groups()
    else:
        print "match匹配失败"
    result=search_test(r"(\w+) (\w+)(?P<sign>!)","This is hello world!") #search是匹配文本全部内容，其它同match；匹配如下内容：单词+空格+单词+任意字符
    if result:
        print "search匹配成功",result.groups()
    else:
        print "search匹配失败"
    #re.split
    pattern=re.compile(r"-")
    result=re.split(pattern, "20160822-warning-this is a log") #按照匹配的子串切割文本；若匹配成功，则返回的分组中不包括分隔符；返回一个list
    if result:
        print "split匹配成功",result #若匹配成功，则返回的分组中不包括分隔符
    else:
        print "split匹配失败"
    #re.findall
    pattern=re.compile(r"\d{1,3}%") #匹配百分数
    result=re.findall(pattern,"This 100% is 20% test 1% string%") #匹配文本中所有的子串并返回所有匹配结果；返回一个list
    if result:
        print "findall匹配成功",result #若匹配成功，则返回的分组中不包括分隔符
    else:
        print "findall匹配失败"
    #re.finditer
    result=re.finditer(pattern,"This 100% is 20% test 1% string%") #返回一个匹配文本中所有的子串的匹配结果的迭代器
    if result:
        print "finditer匹配成功",
        for m in result:
            print m.group(),
    else:
        print "finditer匹配失败"
    #re.sub
    """
    使用repl替换string中每一个匹配的子串后返回替换后的字符串。
    当repl是一个字符串时，可以使用\id或\g、\g引用分组，但不能使用编号0。
    当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。
    count用于指定最多替换次数，不指定时全部替换。
    """
    pattern = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world!'
    print re.sub(pattern,r'\2 \1', s) #常用于删除指定内容
    print re.sub(pattern,func, s)
    #re.subn 返回 (sub(repl, string[, count]), 替换次数)
    
    pattern = re.compile(r'(.*?)(?P<base_url>.*?443)(.*?)')
    result=re.match(pattern,"https://172.16.1.102:443/tmui/Control/jspmap/tmui/locallb/pool/list.jsp?Filter=*")
    print result.groupdict()["base_url"]
    
if __name__ == '__main__':    
    main()

















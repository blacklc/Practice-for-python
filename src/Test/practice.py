#!/usr/bin/env python
#coding:utf-8

import math
import re
from types import IntType,LongType,FloatType,ComplexType

if -1<0:
    print (1 + 2 * 4)
else:
    print "@@@@@@"

str='teststirng'
n=0
while n<len(str):
    print str[n],
    n += 1
print ''
for s in str:
    print s,
    
sum=0
list=[1,2,3,4,6]
for num in list:
    sum += num
print '\n',sum

sum=0
n=0
while n < len(list):
    sum += list[n]
    n += 1
print sum

#除法 /：不四舍五入;如果计算结果为float型，会 计算小数点后数值。两个除数里只有有一个是float型，计算结果就为float型.
#除法 //:四舍五入
avg = float(sum) / len(list)
print avg,type(avg)

n=72
retry=1
while retry:
    if 1<n<100:
        print 'success'
        retry=0
    else:
        print 'fail'

#3个数排序，按从小到大，不使用队列，不使用排序算法
a=100
b=100
c=1
if a > b:
    if a > c:
        if b > c:
            max = a
            min = b
            middle = c
        elif b < c:
            max = a
            min = b
            middle = c
        else:
            max= a
            middle = c
            min= b
    elif a < c:
        middle = a
        max = c
        min = b
elif a < b:
    if a > c:
        max = b
        min = c
        middle = a
    elif a < c:
        if b > c:
            middle = c
            max = b
            min = a
        elif b < c:
            max = c
            min = a
            middle = b
        else:
            max = b
            middle = c
            min = a
else:
    if a > c:
        max = a
        middle = b
        min = c
    elif a < c:
        max = c
        middle = b
        min = a
    else:
        middle = 0
        num = a
if middle:
    print '从大到小:',min,middle,max
    print '从小到大:',max,middle,min
else:
    print '3个数相等',num,num,num

for eachnum in (.2,.7):
    print 'int(%.1f)\t%+.2f' % (eachnum,float(int(eachnum)))
    print 'floor(%.1f)\t%+.2f' % (eachnum,math.floor(eachnum))
    print 'round(%.1f)\t%+.2f' % (eachnum,round(eachnum))

a=hex(255)
print a,type(a),a*1

class c:
    @classmethod
    def __nonzero__(self):
        return False
a=c()
print bool(c)
print bool(a)
print c.__nonzero__()

def socre(**socres):
    """
    根据分数返回评分成绩(A-F)
    
    :param  **sorcres
            分数字典：key-学生姓名;value-学生成绩
    :type   map
    
    :return 生成器;返回每个学生的评分成绩字典:key-学生姓名;value-评分成绩
    """
    for name in socres:
        if 0 <= socres[name] < 60:
            yield {name:'F'}
        elif 60 <= socres[name] <= 69:
            yield {name:'D'}
        elif 70 <= socres[name] <= 79:
            yield {name:'C'}
        elif 80 <= socres[name] <= 89:
            yield {name:'B'}
        elif 90 <= socres[name] <= 100:
            yield {name:'A'}
        else:
            yield {name:'error_socre'}

sc={
    'stu1':60,
    'stu2':80,
    'stu3':99,
    'lc':100,
    'zz':250,
    'maomao':-1
}
for mark in socre(**sc):
    for student in mark:
        print student+':'+mark[student]

def leapYear(year):
    """
    判断给定年份是否为闰年
    
    :param  year
            给定年份
    :type   int
    
    :return boolean True-是闰年;False-不是闰年
    """
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == ］0:
        return True
    else:
        return False

print leapYear(2002)

def get_coin(money):
    """
    计算给定金钱数量可兑换成硬币的最少数量
    
    :param  money
            需兑换的金钱面额
    :type   float
    
    :return 兑换信息字典:key-硬币面值与硬币总量sum;value-硬币个数
    """
    num_25,remainder = divmod(money*100,25)
    num_10,remainder = divmod(remainder,10)
    num_5,remainder = divmod(remainder,5)  
    return {
            25:num_25,
            10:num_10,
            5:num_5,
            1:remainder,
            'sum':remainder+num_5+num_10+num_25,
            } 

print get_coin(0.99)
        
def check_negative_sign(equation_list):
    """
    检查数字前的负号数量
    
    :param  equation_list
            算式列表
    :type   list
    
    :return element 计算操作数
    """
    negative_sign=0 #负号数量标记
    element = equation_list.pop(0)
    #检查数字前是否有负号
    while element in ['+','-','*','/','**','//']:
        if element not in ['+','-']:
            return False
        elif element == '-':
            negative_sign += 1
        element = equation_list.pop(0)
    try:
        element = float(element)
        print element
        if negative_sign % 2 == 0:
            return element
        else:
            return -element
    except:
        raise "The formula is not standardized"
    

def calculator(equation):
    """
    简单计算器实现
    
    :param  equation
            需计算的算式
    :type   string
    
    :return result 返回运算结果
    """
    equation_list = re.split(r'(\+|-|\*\*|//|\*|/|%)', equation) #re.split可以支持同时使用多个切割符，并且如果对切割符加上括号则返回的list中也会加上切割符;实际上切割符部分是正则表达式；因此需要注意写法
    #删除多余空白
    for i,elem in enumerate(equation_list):
        if elem == '':
            equation_list.pop(i)
    num1 = check_negative_sign(equation_list) #获取第一个操作数，并检查数字前是否有负号
    opreation = equation_list.pop(0) #获取操作符
    num2 = check_negative_sign(equation_list) #获取第二个操作数，并检查数字前是否有负号
    #计算结果
    if opreation == '+':
        result = num1 + num2
        return result
    elif opreation == '-':
        result = num1 - num2
        return result
    elif opreation == '*':
        result = num1 * num2
        return result
    elif opreation == '/':
        result = num1 / num2
        return result
    elif opreation == '//':
        result = num1 // num2
        return result
    else:
        result = num1 ** num2
        return result

result = calculator('--2**------3')
print result

result = eval("---1+2") #上述计算器功能可直接使用eval函数实现:将字符串str当成有效的表达式来求值并返回计算结果
print result






















































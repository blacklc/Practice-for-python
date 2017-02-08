#!/usr/bin/env python
#coding:utf-8

from __future__ import division

import math
import re
import random
import sys

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
    elif year % 400 == 0:
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

def divide(num1,num2):
    """
    判断两个整型之间的整出关系
    
    :param  num1
            整型数1
    :type   int
    :param  num2
            整型数2
    :type   int
    
    :return boolean True为两数之间存在整除关系；False为不存在整除关系
    """
    if num1 % num2:
        return True
    elif num2 % num1:
        return True
    else:
        return False

print sys.maxint #输出当前环境支持的最大整型数
print -sys.maxint-1 #输出当前环境支持的最小整型数
print sys.float_info #输出当前环境支持的浮点型信息
print sys.long_info #输出当前环境支持的长整型信息

def hour_to_min(time_string):
    """
    将小时分钟显示的时间转换成分钟显示
    
    :param  time_string
            时间字符串
    :type   string
    
    :return min 分钟表示的时间
    """
    timestr_list = time_string.split(':')
    timestr_list = [int(time) for time in timestr_list]
    min = timestr_list[0]*60 + timestr_list[1]
    return min

min=hour_to_min("11:10")
print min

def Gcd(num1,num2):
    """
    求两个数的最大公约数(辗转相除法)
    
    :param  num1
            数值1
    :type   int
    :param  num2
            数值2
    :type   int
    
    :return gcd 最大公约数
    """
    while num2:
        r = num1 % num2
        (num1,num2) = (num2,r) #辗转相除
    return num1

def Lcm(num1,num2):
    """
    求两个数的最小公倍数(最小公倍数＝两数乘积／最大公约数)
    
    :param  num1
            数值1
    :type   int
    :param  num2
            数值2
    :type   int
    
    :return lcm 最小公倍数
    """
    return (num1 * num2) // Gcd(num1, num2)

g = Gcd(140, 21)
print g

l = Lcm(15,6)
print l

def payment(balance,paid):
    """
    计算家庭财务
    
    :param  balance
            起始金额
    :type   float
    :param  paid
            每月支出金额
    :type   float
    
    :return 
    """
    print 'Pymt#','Pald','Balance'
    print '-----','------','---------'
    mouth = 0
    while balance >= paid:
        if mouth == 0:
            print mouth,'$',0.00,'$',balance
        else:
            balance = balance - paid
            print mouth,'$',paid,'$',balance
        mouth += 1
    print mouth,'$',balance,'$',0.00

payment(100.00, 16.13)

def random_list(rand_list):
    """
    按指定要求生成随机数列表
    
    :param  rand_list
            随机数队列
    :type   list
    
    :return None
    """
    #list_len = random.randint(2,100) #randint的范围为左闭右闭
    while len(rand_list) <= random.randint(2,100):
        rand_list.append(random.uniform(0,(2**31)-1))

def getElement_from_RandomList(random_list):
    """
    按指定要求从随机数队列中取出子集并排序
    
    :param  random_list
            随机数队列
    :type   list
    
    :return child_list 返回子集
    """
    #childList_len = random.randint(1,100)
    chlid_list = [ random_list[random.randrange(len(random_list))] for n in range(random.randint(1,100))]
    chlid_list.sort()
    return chlid_list

rand_list = []
random_list(rand_list)
childlist = getElement_from_RandomList(rand_list)
print rand_list
print childlist

print childlist * 2

print rand_list[1:4] #切片是左闭右开，切片的范围是用序列索引描述的

mlist = range(-5,-1)
mlist.insert(0,None) #注意list的大部分方法返回的都是None;即方法是对原list进行操作，方法本身并不返回list
print mlist

s = 'abcde'
i = -1
for i in range(-1,-len(s),-1):
    print s[:i],i





























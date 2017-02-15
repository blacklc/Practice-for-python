#!/usr/bin/env python
#coding:utf-8

from __future__ import division

import keyword
import math
import re
import random
import string
import sys

from types import IntType,LongType,FloatType,ComplexType
from string import Template

if -1<0:
    print (1 + 2 * 4)
else:
    print "@@@@@@"

str1='teststirng'
n=0
while n<len(str1):
    print str1[n],
    n += 1
print ''
for s in str1:
    print s,
    
sum=0
list1=[1,2,3,4,6]
for num in list1:
    sum += num
print '\n',sum

sum=0
n=0
while n < len(list1):
    sum += list1[n]
    n += 1
print sum

#除法 /：不四舍五入;如果计算结果为float型，会 计算小数点后数值。两个除数里只有有一个是float型，计算结果就为float型.
#除法 //:四舍五入
avg = float(sum) / len(list1)
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
    print '-' * 5,'-' * 6,'-' * 9 #*表示重复
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
    list_len = random.randint(2,100) #randint的范围为左闭右闭
    while len(rand_list) <= list_len:
        rand_list.append(random.uniform(0,(2**31)-1))

def getElement_from_RandomList(random_list):
    """
    按指定要求从随机数队列中取出子集并排序
    
    :param  random_list
            随机数队列
    :type   list
    
    :return child_list 返回子集
    """
    childList_len = random.randint(1,100)
    randomlist_len = len(random_list)
    chlid_list = [ random_list[random.randrange(randomlist_len)] for n in range(childList_len)]
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
print mlist[:None] #当不提供索引值或索引值为None时，切片返回整个字符串

s = 'abcde'
i = -1
for i in range(-1,-len(s),-1):
    print s[:i],i

print '''sdkfjl:sdfks
djflks'''

print '%(test)s' % {'test':'test map'}

tem_str = Template('This is a ${word} test ${word2}.') #字符串模版;除了字符串格式化输出的另一种字符串输出操作
print tem_str.substitute(word='string.template',word2='string')

print chr(65) #返回对应ASCII码对应的字符
print unichr(300) #返回对应的unicode码对应字符z

print ord('A') #返回对应ASCII字符串或unicode对象

str_test = 'test'
join_list = range(10)
print join_list
print str_test.join(repr(join_list))

print join_list,
for i in reversed(join_list):
    print i,

strlist = ['test','test']
print '\n',strlist.pop()
print `strlist.pop()`

t_test = (['xyz',123],23,-103.4)
t_list = list(t_test)
print id(t_test),id(t_list)
#t_string = str(t_test)
#print t_string

alphas = string.letters +'_' #大小写字母再加上下划线
nums = string.digits #所有阿拉伯数字

def idcheck(check_string):
    """
    标示符合法性检查
    
    :param  check_string
            待检查字符串
    :type   string
    
    :return boolean True 合法 False 存在非法标示符
    """
    alphas = string.letters +'_' #大小写字母再加上下划线
    nums = string.digits #所有阿拉伯数字
    kw = keyword.kwlist #所有关键字
    
    cs_length = len(check_string)
    if cs_length >= 1:
        #判断是否以字母或下划线开头
        if check_string[0] not in alphas: return False
        #判断是否存在关键字
        elif check_string in kw: return False
        #判断是否有特殊字符
        else:
            for otherchar in check_string[1:]:
                if otherchar and (otherchar not in alphas + nums): return False
            else: return True

if idcheck('7'):
    print 'ok' 
else:
    print 'no'
    
n_list = [random.randint(1,9) for i in range(10)]
print 'old:',n_list
n_list2 = n_list[:]
n_list.sort(reverse=True) #列表倒序排列:从大到小
print 'new:',n_list   
n_list2 = [str(n) for n in n_list2]         
n_list = [n for n in sorted(n_list2,reverse=True)] #按字典序排序：按ASCII码从大到小
print 'new with ascii:',n_list

string11 = 'teststring'
n = 0
s_l = len(string11)
while n <= s_l:
    print string11[n-1:n+2].strip()
    n += 1

def cmp_by_scan(string1,string2):
    """
    通过扫描字符串方式匹配字符串
    
    :param  string1
            待比较字符串
    :type   string
    
    :param  string2
            待比较字符串
    :type   string
    
    :return boolean True 匹配成功；False 匹配失败
    """
    if len(string1) != len(string2):
        return False
    for i,string1_member in enumerate(string1):
        if i != string2.find(string1_member):
            return False
    return True

if cmp_by_scan("123Abcd", "123Abcd"):
    print 'same'
else:
    print 'different'

def everse_string(str):
    """
    接受一个字符，并在其后加入一个反向拷贝，构成一个回文字符串
    
    :param  str
            待反转字符串
    :type   string
    
    :return string 返回一个回文字符串
    """
    return ''.join((str,str[-1::-1]))

print everse_string('abcdf')

fac = range(1,5)
print 'fac'

def search_reciprocal_number(num):
    """
    查找一个数的互质数
    
    :param  num
    :type   int
    
    :return list 互质数列表
    """
    if num % 2 == 0:
        fac_list = range(1,num+1)
        i = 0
        while i < len(fac_list):
            if num % fac_list[i] == 0:
                del fac_list[i]
            else:
                i += 1
        return fac_list
    else:
        return [1,num]

print search_reciprocal_number(30)

def num_to_eng(num):
    """
    给出一个整型值返回代表该值的英文
    
    :param  num(0~1000)
            待翻译的整型值
    :type   int
    
    :return string 整型的英文表示
    """
    digits = ['one','two','there','four','five','six','seven','eight','nine']
    ten_digits = ['ten','twenty','thrity','fourty','fivty','sixty','seventy','eighty','ninty']
    if 100 <= num < 1000:
        hundred_tuple = divmod(num,100)
        ten_tuple = divmod(hundred_tuple[1],10)
        hundred_digits_index = hundred_tuple[0] - 1
        ten_digits_index = ten_tuple[0] - 1
        digits_index = ten_tuple[1] - 1
        return '%s hunderd-%s-%s' %(digits[hundred_digits_index],ten_digits[ten_digits_index],digits[digits_index])
    elif 10 <= num <100:
        ten_tuple = divmod(num,10)
        ten_digits_index = ten_tuple[0] - 1
        digits_index = ten_tuple[1] - 1
        return '%s-%s' %(ten_digits[ten_digits_index],digits[digits_index])
    elif 0 < num < 10:
        digits_index = num - 1
        return '%s' %(digits[digits_index])
    else:
        return 'Error:"num must between 0~1000"'
    
print num_to_eng(847)
            
def min_to_hourMin(min):        
    """
    将分钟转换成小时分钟表现形式
    
    :param  min
            分钟数
    :type   int
    
    :return string 返回时间的小时分钟表现形式
    """
    hour_min_tuple = divmod(min,60)
    return '%02d:%02d' %(hour_min_tuple[0],hour_min_tuple[1])

print min_to_hourMin(90)

def int_to_ipaddress(ip_num):
    """
    整型到IP地址格式换
    
    :param  ip_num
            需转换的整型
    :type   int
    
    :return string ip address
    """
    if 1000 <= ip_num <= 255255255255:
        ip_str = repr(ip_num)
        ip_length = len(ip_str)
        ip_tuple = divmod(ip_length,4)
        ipaddress_str = ''
        str_tag = 0
        for i in range(ip_tuple[0]):
            ipaddress_str = '%s%s.' % (ipaddress_str,ip_str[str_tag:str_tag+3])
            str_tag += 3
        ipaddress_str = ''.join((ipaddress_str,ip_str[str_tag:]))
        if ipaddress_str.endswith('.'):
            ipaddress_str = ipaddress_str[:len(ipaddress_str)-1]
        return ipaddress_str

print int_to_ipaddress(172168182192)

def ipaddress_to_int(ip_str):
    """
    IP地址格式到整型转换
    
    :param  ip_num
            需转换的IP地址字符串
    :type   string
    
    :return int ip address
    """
    return int(ip_str[0:3])*(10**9)+int(ip_str[4:7])*(10**6)+int(ip_str[8:11])*(10**3)+int(ip_str[12:])

print ipaddress_to_int('172.168.123.132')

def findchr(str,chr):
    """
    自实现string.find()函数(单一字符版)
    
    :param  str
            被搜索字符串
    :type   string
    
    :param  chr
            被查找字符
    :type   char
    
    :return char_index 若查找到，则返回字符的索引；若未查找到则返回-1
    """
    char_index = -1
    for i,c in enumerate(str):
        if c == chr:
            char_index = i
            break
    return char_index

print findchr('string', 'a')

def findstr(str1,str2):
    """
    自实现string.find()函数
    
    :param  str1
            被搜索字符串
    :type   string
    
    :param  str2
            被查找字符串
    :type   string
    
    :return str_index 若查找到，则返回字符串的首索引；若未查找到则返回-1
    
    """
    str_index = -1
    i = 0
    y = findchr(str1[0:], str2[i])
    str2_len = len(str2)
    while y != -1:
        if i+1 == str2_len or findchr(str1[y:str2_len+1], str2[i]) != 0:
            break
        i += 1
        y += 1
    if i+1 == str2_len:
        str_index = y-(str2_len-1)
    return str_index     

print findstr('string', 'rin')            

def rfindchr(str,chr):
    """
    自实现string.rfind()函数
    
    :param  str
            被搜索字符串
    :type   string
    
    :param  chr
            被查找字符
    :type   char
    
    :return index 若查找到，则返回字符的索引；若未查找到则返回0
    """
    char_index = 0
    for i in range(-1,-len(str)-1,-1):
        if chr == str[i]:
            char_index = i
            break
    return char_index

print rfindchr('string', 'a')

def subchf(str,origchar,newchar):
    """
    查找字符;若存在，则将其替换成指定字符
    
    :param  str
            被搜索字符串
    :type   string
    
    :param  origchar
            被查找字符
    :type   char 
    
    :param  newchar
            替换字符
    :type   char   
    
    :return string 返回修改过后的字符串 
    """
    for i,c in enumerate(str):
        if c == origchar:
            str = ''.join((str[0:i],newchar,str[i+1:]))
    return str

print subchf('aaabbb','a','c')

def atoc(complex_str):
    """
    字符串转复数类型
    
    :param  complex_str
            复数对应的字符串表达
    :type   string
    
    :return complex 字符串转换的复数类型
    """
    #对应情况：只有实数部分
    if 'j' not in complex_str:
        return complex(float(complex_str))
    else:
        c_str = complex_str.split('j')
        #对应情况：标准形式；-5.67e-8j-1.23e+4
        if '' not in c_str:
            return complex(float(c_str[1]),float(c_str[0]))
        #对应情况：标准形式；-1.23e+4-5.67e-8j
        else:
            re_string = r'(?P<real>[+-].*?\.*?e[+-].*?)(?P<imag>[+-].*?)j'
            pattern = re.compile(re_string) #将正则表达式编译成pattern对象
            result = re.match(pattern, complex_str)  
            print result.groupdict()
            return complex(float(result.groupdict()['real']),float(result.groupdict()['imag']))

print atoc('-1.23e+4-5.67e-8j')
print atoc('-5.67e-8j-1.23e+4')







        















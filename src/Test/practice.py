#!/usr/bin/env python
#coding:utf-8

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


























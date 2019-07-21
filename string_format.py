# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: moziran

name = input("name:").strip(A)
# strip方法可以去掉头部和尾部的所有空格；如果在括号中加入参数，可以去掉特定的值
age = input("age:")
job = input("job:")

# 三个单引号对 or三个双引号对和对多行进行注释
msg = '''
Information of %s:
    Name:%s
    Age:%s
    Job:%s
''' % (name, name, age, job)
print(msg)
print(name)

# print("Information of "+name+":\nName:"+name+"\nAge:"+age+"\nJob:"+job)

# print("Information of %s:\nName:%s\nAge:%s\nJob:%s" % (name, name, age, job))




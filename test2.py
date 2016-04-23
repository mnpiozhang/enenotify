#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import tushare as ts
from tushare.util import dateu as du
import datetime
a = du.today()
print a
a = str(datetime.datetime.today().date() + datetime.timedelta(-1))
print du.is_holiday(a)

print str(datetime.datetime.strptime(a, '%Y-%m-%d') + datetime.timedelta(-1))
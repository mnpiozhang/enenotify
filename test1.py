#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tushare as ts
from threading import Thread
#print ts.get_hist_data('601199')
#print ts.get_h_data('601199')
def Foo(arg):
    print ts.get_realtime_quotes(arg)

print 'before'
t1 = Thread(target=Foo,args=('601199',))
t1.start()

print t1.getName()

t2 = Thread(target=Foo,args=('601199',))
t2.start()

print t2.getName()

print 'after'
#print ts.get_realtime_quotes('601199')
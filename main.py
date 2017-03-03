#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import function
import time
from common import  EmailNotify
from common import  GetConfigList
import threading

lst = GetConfigList('stock_number')


def get_ene(stock_number):
    while True:
        realtimePrice = function.GetRealTimePrice(stock_number)
        enelst = function.CalculateRealTimeENE(stock_number, 10, 11, 9)
        upperprice = enelst[0]
        lowerprice = enelst[1]
        middleprice = enelst[2]
        print realtimePrice,upperprice,middleprice,lowerprice
        if realtimePrice > upperprice:
            message = u'打到上轨了  %s 现价 %s 上轨 %s 中轨%s 下轨%s'%(i,realtimePrice,upperprice,middleprice,lowerprice)  
            EmailNotify(message,message)
            time.sleep(1800)
        elif realtimePrice < lowerprice:
            message = u'跌到下轨了  %s 现价 %s 上轨 %s 中轨%s 下轨%s'%(i,realtimePrice,upperprice,middleprice,lowerprice)
            EmailNotify(message,message)
            time.sleep(1800)
        else:
            print  u'还在轨道通道内  %s 现价 %s 上轨 %s 中轨%s 下轨%s'%(i,realtimePrice,upperprice,middleprice,lowerprice)
            time.sleep(10)

if __name__=='__main__':
    threadlst = []
    for i in lst:
        t = threading.Thread(target=get_ene,args=(i,))
        t.start()
        threadlst.append(t)
    print "ene calculate start"
    for i in threadlst:
        i.join()

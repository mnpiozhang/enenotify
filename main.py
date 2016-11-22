#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import function
import time
from common import  EmailNotify
from common import  GetConfigList
lst = GetConfigList('stock_number')
if __name__=='__main__':
    while True:
        for i in lst:
            realtimePrice = function.GetRealTimePrice(i)
            enelst = function.CalculateRealTimeENE(i, 10, 11, 9)
            upperprice = enelst[0]
            lowerprice = enelst[1]
            middleprice = enelst[2]
            print realtimePrice,upperprice,middleprice,lowerprice
            if realtimePrice > upperprice:
                message = u'打到上轨了  %s 现价 %s 上轨 %s 中轨%s 下轨%s'%(i,realtimePrice,upperprice,middleprice,lowerprice)  
                EmailNotify(message,message)
            elif realtimePrice < lowerprice:
                message = u'跌到下轨了  %s 现价 %s 上轨 %s 中轨%s 下轨%s'%(i,realtimePrice,upperprice,middleprice,lowerprice)
                EmailNotify(message,message)
            else:
                print  u'还在轨道通道内  %s 现价 %s 上轨 %s 中轨%s 下轨%s'%(i,realtimePrice,upperprice,middleprice,lowerprice)
            time.sleep(1800)

#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from __future__ import division
import tushare as ts
from common import WorkdayList
import time
from tushare.util import dateu as du
'''
都使用前复权
'''
def CalculateMA(stocknumber,n):
    '''
    计算历史均价 不含当天交易日的，使用前复权
    stocknumber 股票代码 类型int 
    n 几日均价 类型int
    '''
    tmplst = WorkdayList(n)
    startday = tmplst[-1]
    endday = tmplst[0]
    a = ts.get_h_data(str(stocknumber),startday,endday)
    numlst = a.head(n)['close'].values
    sumclose = 0
    for i in numlst:
        sumclose = sumclose + i 
    return sumclose/n


def CalculateRealTimeMA(stocknumber,n):
    '''
    计算实时均价，包含实时现价作为当天收盘价，使用前复权。开盘前不要用，建议只开盘时使用
    stocknumber 股票代码 类型int 
    n 几日均价 类型int
    '''
    nowtime = int(time.strftime('%H',time.localtime(time.time())))
    today = du.today()
    if du.is_holiday(today) or nowtime > 16 or nowtime < 9:
        return CalculateMA(stocknumber,n)
    else:
        price = ts.get_realtime_quotes(str(stocknumber))['price'].values
        behandma = CalculateMA(stocknumber,n-1)
        for i in price: 
            c = behandma*(n-1) + float(i)
        return float(c)/n


def CalculateENE(stocknumber,N,M1,M2):
    '''
    计算历史轨道线
    返回列表为 上轨下轨中轨
    '''
    maCloseN = CalculateMA(stocknumber,N)
    upper = (1 + float(M1)/100)*maCloseN
    lower = (1 - float(M2)/100)*maCloseN
    ene = (upper+lower)/2
    return [round(upper,2),round(lower,2),round(ene,2)]


def CalculateRealTimeENE(stocknumber,N,M1,M2):
    '''
    计算实时轨道线
    返回列表为 上轨下轨中轨，开盘前不要用。建议只开盘时使用
    '''
    maCloseN = CalculateRealTimeMA(stocknumber,N)
    upper = (1 + float(M1)/100)*maCloseN
    lower = (1 - float(M2)/100)*maCloseN
    ene = (upper+lower)/2
    return [round(upper,2),round(lower,2),round(ene,2)]

def GetRealTimePrice(stocknumber):
    '''
    获得股票的实时股价
    stocknumber 股票代码 类型int 
    '''
    return float(''.join(ts.get_realtime_quotes(str(stocknumber))['price'].values))

#print GetRealTimePrice(601199)
#print CalculateRealTimeENE(601199,10,11,9)
#print CalculateENE(601199,10,11,9)
    
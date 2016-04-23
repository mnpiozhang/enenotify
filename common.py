#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import smtplib  
from email.mime.text import MIMEText
from configparser import ConfigParser
from tushare.util import dateu as du
import datetime


def GetConfig(section,key):
    cfg = ConfigParser()
    cfg.read('config.ini')
    return cfg.get(section,key)


def GetConfigList(section):
    '''
    通过配置文件 编辑出一个收邮寄的邮箱的列表  section为 to_list
    '''
    cfg = ConfigParser()
    cfg.read('config.ini')
    datadict={}
    for (key, value) in cfg.items(section):
        datadict[key] = value
    return datadict.values()



def EmailNotify(subject,content):
    receiver = GetConfigList('to_list')
    sender = GetConfig('email','sender')
    subject = subject
    smtpserver = GetConfig('email','smtpserver')
    username = GetConfig('email','username')
    password = GetConfig('email','password')

    msg = MIMEText(content,'html','utf-8')
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    msg['From'] = sender
    msg['Subject'] = subject
    msg['To'] = ";".join(receiver)  

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()


def WorkdayList(n):
    '''
    根据输入的天数，返回过去的n天数为工作日的列表
    '''
    workdaylst = []
    yesterday = datetime.datetime.today().date() + datetime.timedelta(-1)
    yesterdatstr = str(yesterday)
    while len(workdaylst) < n:
        if du.is_holiday(yesterdatstr):
            yesterday = yesterday + datetime.timedelta(-1)
            yesterdatstr = str(yesterday)
        else:
            workdaylst.append(yesterdatstr)
            yesterday = yesterday + datetime.timedelta(-1)
            yesterdatstr = str(yesterday)
    return workdaylst
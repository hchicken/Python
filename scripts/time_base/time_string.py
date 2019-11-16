# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2019/11/16 15:23

import time
import datetime
from dateutil.relativedelta import relativedelta


def datetimeDeal():
    nowTime = datetime.datetime.now()  # 获取当前时间
    print(f"type：{type(nowTime)}", nowTime)

    nowTimeString = nowTime.strftime("%Y-%m-%d %H:%M:%S")  # time 转换成字符串
    print(f"type：{type(nowTimeString)}", nowTimeString)

    stringTonowTime = datetime.datetime.strptime(nowTimeString, "%Y-%m-%d %H:%M:%S")  # 字符串转 time类型
    print(f"type：{type(stringTonowTime)}", stringTonowTime)

    beforeTime = nowTime + datetime.timedelta(days=-1)  # 时间间隔 +-
    print(f"type：{type(beforeTime)}", beforeTime)

    beforeTime = nowTime + relativedelta(month=1)  # 范围广
    print(f"type：{type(beforeTime)}", beforeTime)


def timeDeal():
    nowTimeStamp = time.time()  # 当前时间戳
    print(f"type：{type(nowTimeStamp)}", nowTimeStamp)

    nowTime = time.localtime(nowTimeStamp)  # 时间戳装换为time类型
    print(f"type：{type(nowTime)}", nowTime)

    nowTimeString = time.strftime("%Y-%m-%d %H:%M:%S", nowTime)  # time 转换成字符串
    print(f"type：{type(nowTimeString)}", nowTimeString)


if __name__ == "__main__":
    datetimeDeal()

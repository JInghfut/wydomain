#! -*- coding:utf-8 -*-

"""

@version:1.0
@date:14-7-16
@description:日期时间工具模块
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time

from datetime import datetime, timedelta


class DateUtil(object):
    """
    提供系统所需日期时间等相关静态数据

    """

    @classmethod
    def get_end_date(cls, start_date, alive_days):
        """获取过期日期"""
        start_date_arr = str(start_date).split('-')
        start_date = datetime(int(start_date_arr[0]), int(start_date_arr[1]), int(start_date_arr[2]))
        alive_days = timedelta(days=alive_days)
        end_date = start_date + alive_days
        return end_date.strftime('%Y-%m-%d')

    @classmethod
    def get_timestamp(cls):
        """获取当前时间戳"""
        return time.time()

    @classmethod
    def get_sys_date(cls):
        """系统当前日期"""
        local_time = time.localtime()
        sys_date = time.strftime('%Y-%m-%d', local_time)
        return sys_date

    @classmethod
    def str_2_date(cls, data_str, split_str):
        """将字符串转换成datetime类型"""
        str_arr = data_str.split(split_str)
        if len(str_arr) < 3:
            return None
        format_date = datetime(int(str_arr[0]), int(str_arr[1]), int(str_arr[2]))
        return format_date

    @classmethod
    def str_2_time(cls, time_str, split_date, split_time):
        """将字符串转换成datetime类型"""
        str_arr = time_str.split(' ')
        if len(str_arr) < 2:
            return None
        date_str_arr = str_arr[0].lstrip().rstrip().split(split_date)
        time_str_arr = str_arr[1].lstrip().rstrip().split(split_time)
        format_date = datetime(year=int(date_str_arr[0]), month=int(date_str_arr[1]), day=int(date_str_arr[2]), hour=int(time_str_arr[0]), minute=int(time_str_arr[1]), second=int(time_str_arr[2]))
        return format_date

    @classmethod
    def get_sys_time(cls, format_str=None, split_date='-', split_time=':'):
        """系统当前时间"""
        sys_time = datetime.now()
        if not format_str:
            return None
        now = sys_time.strftime(format_str)
        str_arr = now.split(' ')
        if len(str_arr) != 2:
            return None
        date_str_arr = str_arr[0].lstrip().rstrip().split(split_date)
        time_str_arr = str_arr[1].lstrip().rstrip().split(split_time)
        format_date = datetime(year=int(date_str_arr[0]), month=int(date_str_arr[1]), day=int(date_str_arr[2]), hour=int(time_str_arr[0]), minute=int(time_str_arr[1]), second=int(time_str_arr[2]))
        return format_date

    @classmethod
    def delta(cls, time, hours=0, minutes=0):
        return time - timedelta(hours=hours, minutes=minutes)

    @classmethod
    def time_before(cls, hours=0, minutes=0):
        """quantity(unit)以前，如两小时以前"""
        now = cls.get_sys_time('%Y-%m-%d %H:%M:%S')
        return cls.delta(now, hours, minutes)


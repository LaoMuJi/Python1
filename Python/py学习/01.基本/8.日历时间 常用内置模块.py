# calendar  日历
# https://github.com/tulingxueyuan/CookBook_and_code/blob/master/06-%E5%B8%B8%E7%94%A8%E6%A8%A1%E5%9D%97.ipynb

import calendar

# 判断某一年是否是闰年
print(calendar.isleap(2019))

# 获取指定年份之间的闰年的个数
print(calendar.leapdays(2001, 1998))

# time 时间

import time

# 检测是否是夏令时 0是
print(time.daylight)

# 获取时间戳
print(time.time())


# 获取当前时间 年 月 时
t = time.localtime()
print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

# \\\\\\\传入时间元祖格式化？
print(t)
tt = time.asctime((2000,1,1,0,0,0,0,0,0))
print(tt)
tt = time.asctime(t)
print(tt)

# 获取字符串化的当前时间
t = time.ctime()
print(t)

# 获取对应的时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(ts)

# 睡眠N秒
time.sleep(1)

# 自定义时间格式
'''
格式  含义  备注
%a    本地（locale）简化星期名称    
%A    本地完整星期名称    
%b    本地简化月份名称    
%B    本地完整月份名称    
%c    本地相应的日期和时间表示    
%d    一个月中的第几天（01 - 31）   
%H    一天中的第几个小时（24 小时制，00 - 23）   
%I    一天中的第几个小时（12 小时制，01 - 12）   
%j    一年中的第几天（001 - 366）  
%m    月份（01 - 12） 
%M    分钟数（00 - 59）    
%p    本地 am 或者 pm 的相应符    注1
%S    秒（01 - 61）  注2
%U    一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w    一个星期中的第几天（0 - 6，0 是星期天） 注3
%W    和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x    本地相应日期  
%X    本地相应时间  
%y    去掉世纪的年份（00 - 99）    
%Y    完整的年份   
%z    用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%    %号本身
'''
# 把时间表示成， 2018年3月26日 21:05
t = time.localtime()
ft = time.strftime("%Y{y}%m{m}%d{d} %H:%M", t).format(y='年',m='月',d='日')
print(ft)






# datetime 模块

import datetime


# 提供一个理想的时间格式属性

dt = datetime.date(2008,12,31)
print(dt)
print(dt.month)

dt = datetime.time(1,5,58)
print(dt)

dt = datetime.timedelta(hours=99999)
print(dt)

'''
1 <= month <= 12
1 <= day <= n
0 <= hour < 24
0 <= minute < 60
0 <= second < 60
0 <= microsecond < 10**
'''



# 生成列表比较时间

import timeit
t1 = timeit.timeit(stmt='[i for i in range(1000)]', number=100)
print(t1)

c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
t1 = timeit.timeit(stmt=c, number=100)
print(t1)


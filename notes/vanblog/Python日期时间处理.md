# 日期相关
- 判断是否闰年
```python
import calendar
calendar.isleap(2024) # True
```
- 打印某月日历
```python
import calendar
calendar.prmonth(2023,2)
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e85e1a3fa208755a635b9750374a04cf.image.png)

- 查询每月多少天
```python
import calendar
# 返回该月首日星期和天数
calendar.monthrange(2023,2) # (2,28)
```

<!-- more -->

# 时间相关
- 获取当前时间戳  

方法一：
```python
import time
time.now() # 1680240112.9216447
```
方法二：
```python
import datetime
t = datetime.datetime.now() # datetime.datetime(2023, 3, 31, 13, 17, 55, 211020)
t.timestamp() # 1680239875.21102
```

- 格式化时间输出：`strftime`
```python
import datetime
t = datetime.datetime.now() # datetime.datetime(2023, 3, 31, 13, 17, 55, 211020)
t.strftime("%Y-%m-%d %H:%M:%S") # '2023-03-31 13:17:55'
```

- 提取时间字段信息
```python
import datetime
t = datetime.datetime.now() # datetime.datetime(2023, 3, 31, 13, 17, 55, 211020)
t.year      # 2023
t.month     # 3
t.day       # 31
t.hour      # 13
t.minute    # 17
t.second    # 55
t.weekday() # 4
t.date()    # datetime.date(2023, 3, 31)
t.timestamp() # 1680239875.21102
```

- 从格式字符串构造时间：`strptime`
```python
import datetime
t2 = datetime.datetime.strptime("2022-03-31 13:24:34", "%Y-%m-%d %H:%M:%S")
t2 # datetime.datetime(2022, 3, 31, 13, 24, 34)
```

# 时间增量
- 计算两个日期之间的天数差
```python
import datetime
begin = datetime.datetime(2023,3,1)
end = datetime.datetime(2023,4,1)
(end-begin).days
```

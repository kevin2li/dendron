# 简介

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/fca5978a62e219c7bdb3a79b73c22516.image.png)


<!-- more -->


# 示例
```python
#! /home/kevin2li/miniconda3/bin/python
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
from loguru import logger
import httpx
import schedule
import time
logger.add("/home/kevin2li/love/morning.log")

sender_email = "kevin2li@qq.com"
receiver_email = "lyouyou0118@163.com"
password = "hjcpxgbykyvhfhhf"

tianxing_key = "50fbff4c2585e14f38263aa9b5ed10b6"
gaode_key = "b3dd05aa4727b6bd75af8e578ed23256"

def main():
    try_times = 3
    for i in range(try_times):
        try:
            message = MIMEMultipart("alternative")
            message["Subject"] = "🌞早安问候"
            message["From"] = sender_email
            message["To"] = receiver_email
            
            # 获取今天日期
            today = datetime.now()
            start = datetime(2023,1,18)
            one_year = datetime(2024,1,18)
            passed_days = (today-start).days+1
            left_days = (one_year-today).days
            days_sentence    = f"今天是我们恋爱的第{passed_days}天，距离下次我们的生日还有{left_days}天。"

            # 获取黄历
            logger.info("[1/4] 获取黄历")
            r = httpx.get(f"https://apis.tianapi.com/lunar/index?key={tianxing_key}&date={today.year}-{today.month}-{today.day}")
            res = r.json()
            logger.info(res)
            weekday = {0:"一", 1: "二", 2: "三", 3: "四", 4: "五",5: "六",6: "日"}
            calendar_sentence   = f"今天是{today.year}年{today.month}月{today.day}日，星期{weekday[today.weekday()]}，农历{res['result']['lubarmonth']}{res['result']['lunarday']}。"

            # 获取壁纸
            logger.info("[2/4] 获取壁纸")
            r = httpx.get("https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1")
            res = r.json()
            imgurl = "https://www.bing.com"+res['images'][0]['url']
            image_title = res['images'][0]['title']
            logger.info(res)

            # 获取诗词
            logger.info("[3/4] 获取诗词")
            r = httpx.get(f"https://apis.tianapi.com/zmsc/index?key={tianxing_key}")
            res = r.json()
            poem_sentence = f"{res['result']['content']} ——{res['result']['source']}"
            logger.info(res)

            # 获取天气
            logger.info("[4/4] 获取天气")
            city = "340104"
            r = httpx.get(f"https://restapi.amap.com/v3/weather/weatherInfo?key={gaode_key}&city={city}&extensions=all")
            res = r.json()
            logger.info(res)
            if res['status'] == '1':
                city = res['forecasts'][0]['city']
                province = res['forecasts'][0]['province']
                casts = res['forecasts'][0]['casts'][0]
                weather_sentence = f"{city}今天天气{casts['dayweather']}，今日气温{casts['nighttemp_float']}℃至{casts['daytemp_float']}℃，有{casts['daypower']}级{casts['daywind']}风。"

            html = f"""\
            <html>
            <body>
                <p>
            <section id="nice" data-tool="mdnice编辑器" data-website="https://www.mdnice.com" style="font-size: 16px; color: black; padding: 0 10px; line-height: 1.6; word-spacing: 0px; letter-spacing: 0px; word-break: break-word; word-wrap: break-word; text-align: left; counter-reset: counterh1 counterh2 counterh3; font-family: Optima-Regular, Optima, PingFangSC-light, PingFangTC-light, 'PingFang SC', Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;"><p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">{calendar_sentence}</p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">{days_sentence}</p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">琳妹妹，今天也是爱你的一天哦，早安啦💕</p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;"><strong style="font-weight: bold; color: rgb(37,132,181);">每日壁纸：</strong></p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;"><img src="{imgurl}" alt style="display: block; margin: 0 auto; max-width: 100%;">
            {image_title}</p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;"><strong style="font-weight: bold; color: rgb(37,132,181);">每日诗词：</strong></p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">{poem_sentence}</p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;"><strong style="font-weight: bold; color: rgb(37,132,181);">今日天气：</strong></p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">{weather_sentence}</p>
            <p data-tool="mdnice编辑器" style="font-size: 16px; padding-top: 8px; padding-bottom: 8px; margin: 0; line-height: 26px; color: black;">(👆以上是来自男朋友的早安问候，希望能带给你好心情，我会一直陪伴你哦，爱你😘)</p>
            </section>
                </p>
            </body>
            </html>
            """

            logger.info("发送邮件...")
            # Turn these into plain/html MIMEText objects
            part = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )
            logger.info("发送完成！")
            break
        except:
            logger.error(f"[{i+1}/{try_times}]发送失败！")
            traceback.print_exc()

if __name__=='__main__':
    schedule.every().day.at("07:30").do(main)
    # schedule.every().minute.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)

```

# 参考
[1] https://realpython.com/python-send-email/
from common.wifi import *
import ntptime
import uasyncio as asyncio
import machine
import time
import utime
from lib import urequests
timezone_offset=8*3600
# 获取当前网络时区
def get_network_timezone():
    try:
        response = urequests.get("https://freeipapi.com/api/json")
        data = response.json()
        #print(data)
        response.close()
        timezone_offset = data['timeZone']
        hours_offset = int(timezone_offset[1:3])
        minutes_offset = int(timezone_offset[4:6])
        total_offset = hours_offset + minutes_offset / 60
        if timezone_offset[0] == '-':
            total_offset = -total_offset
        return int(total_offset*60*60)
    except Exception as e:
        print("Failed to get timezone:", e)
        return 28800  # 默认使用+8:00

def print_current_time():
    print(f"当地时间:{get_local_time()}")

def get_local_time():
    return utime.localtime(time.time() + timezone_offset)
def get_utc_time():
    return utime.gmtime()

def sync_time():
    timezone_offset=get_network_timezone()
    ntptime.host="ntp.aliyun.com"
    ntptime.settime()
    print_current_time()
# 设置定时器定期同步时间
def init_sync_timer(interval=24*60*60*1000):
    def timer_callback(timer):
        sync_time()
    sync_time()
    timer = machine.Timer(-1)
    timer.init(period=interval, mode=machine.Timer.PERIODIC, callback=timer_callback)
    print(f"Timer set to sync every {interval // 1000} seconds")
    
asyncio.run(wifi_auto_connect())
if is_wifi_connect():
    init_sync_timer(12*60*60*1000)
    while is_wifi_connect():
        print_current_time()
        time.sleep(1)
    

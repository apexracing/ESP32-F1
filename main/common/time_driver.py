import ntptime
import uasyncio as asyncio
import machine
import time
import utime
from lib import urequests


def singleton(cls):
    instance = None

    def getinstance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return getinstance


@singleton
class TimeDriver:
    def __init__(self, timezone_offset: int = 8 * 3600):
        self.timezone_offset = timezone_offset
        if self.timezone_offset >= 0:
            self.timezone = "+"
        else:
            self.timezone = "-"
        minutes, seconds = divmod(timezone_offset, 60)
        hours, minutes = divmod(minutes, 60)
        self.timezone = self.timezone + "%02d:%02d" % (hours, minutes)

    # 获取当前网络时区
    def __get_network_timezone(self):
        '''
        根据网格IP获取当前时区，如果失败，则默认为驱动初始化的时区
        :return:
        '''
        try:
            response = urequests.get("https://freeipapi.com/api/json")
            data = response.json()
            # print(data)
            response.close()
            time_zone = data['timeZone']
            self.timezone = time_zone

            hours_offset = int(time_zone[1:3])
            minutes_offset = int(time_zone[4:6])
            total_offset = hours_offset + minutes_offset / 60
            if time_zone[0] == '-':
                total_offset = -total_offset
            return int(total_offset * 60 * 60)
        except Exception as e:
            print("Failed to get timezone:", e)
            return self.timezone_offset  # 默认使用+8:00

    def print_current_time(self):
        print(f"当地时间:{self.get_local_time()}")

    def get_local_time(self):
        return utime.localtime(time.time() + self.timezone_offset)
    def get_local_time_from(self,unixtime):
        return utime.localtime(unixtime+self.timezone_offset)
    def get_utc_time(self):
        return utime.gmtime()
    def get_unixtime(self):
        return int(time.time_ns()/1000/1000/1000)
    def iso8610_to_unixtime(self,time_str):
        time_tuple = (int(time_str[0:4]), int(time_str[5:7]), int(time_str[8:10]),
                      int(time_str[11:13]), int(time_str[14:16]), int(time_str[17:19]), 0, 0)

        # 将时间元组转换为Unix时间戳
        return utime.mktime(time_tuple)

    def get_time_zone(self):
        return self.timezone

    def __sync_time(self):
        ntp_ok = False
        ntp_hosts = ["ntp.aliyun.com", "ntp.tencent.com", "pool.ntp.org"]
        for ntp_host in ntp_hosts:
            try:
                self.timezone_offset = self.__get_network_timezone()
                ntptime.host = ntp_host
                ntptime.settime()
                print("Ntp synchronize Ok!")
                break
            except Exception as e:
                print("Failed to synchronize time:", e)

    # 设置定时器定期同步时间
    def init_sync_timer(self, interval=24 * 60 * 60 * 1000):
        '''
        :param interval: 同步时间周期，默认为24小时同步一次
        :return:
        '''

        def timer_callback(_):
            self.__sync_time()

        self.__sync_time()
        self.print_current_time()
        timer = machine.Timer(-1)
        timer.init(period=interval, mode=machine.Timer.PERIODIC, callback=timer_callback)
        print(f"Timer set to sync every {interval // 1000} seconds")

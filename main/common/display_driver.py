import lvgl as lv
from ili9XXX import gc9a01,COLOR_MODE_BGR
class DisplayDriver:
    def __init__(self):
        self.disp=gc9a01(miso=12, mosi=11, clk=10, cs=9, dc=8, rst=14, backlight=2, backlight_on=1, mhz=80, factor=8,colormode=COLOR_MODE_BGR)
        print("屏幕gc9a01驱动初始化完成")

    def __del__(self):
        self.disp.deinit()
        print("屏幕资源已释放")


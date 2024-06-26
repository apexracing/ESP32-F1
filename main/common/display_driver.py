import lvgl as lv
import espidf as esp
from lib.ili9xxx import gc9a01,COLOR_MODE_BGR
def singleton(cls):
    instance = None
    def getinstance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return getinstance
@singleton
class DisplayDriver:
    def __init__(self):
        self.disp=gc9a01(miso=12, mosi=11, clk=10, cs=9, dc=8, rst=14, backlight=2, backlight_on=0, mhz=80, factor=4,hybrid=True,colormode=COLOR_MODE_BGR, asynchronous=False)
        print("屏幕gc9a01驱动初始化完成,背光未开启，调用backlight_on开启背光")

    def __del__(self):
        self.disp.deinit()
        print("屏幕资源已释放")

    def backlight_on(self):
        esp.gpio_set_level(2, 1)

    def backlight_off(self):
        esp.gpio_set_level(2,0)
    def __delete__(self, instance):
        print("DisplayDriver Del")

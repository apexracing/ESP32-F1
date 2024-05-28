from ili9XXX import gc9a01,COLOR_MODE_BGR
from touch_driver import TouchDriver
import lvgl as lv
print("LVGL VERSION:%d.%d.%d"%(lv.version_major(),lv.version_minor(),lv.version_patch()))
disp = gc9a01(miso=12, mosi=11, clk=10, cs=9, dc=8, rst=14,backlight=2, backlight_on=1,mhz=80, factor=8, colormode=COLOR_MODE_BGR)
print("屏幕gc9a01驱动初始化完成")
touch_tensor=TouchDriver()
import ui

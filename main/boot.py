# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
import time
from ui.flash_screen import FlashScreen
lv.init()
print("LVGL VERSION:%d.%d.%d"%(lv.version_major(),lv.version_minor(),lv.version_patch()))
display=DisplayDriver()
touch_tensor=TouchDriver()
scr1=FlashScreen()
#加载Flash启动屏幕后，开启背光
display.backlight_on()

while True:
    lv.task_handler()
    time.sleep_ms(10)
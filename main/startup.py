from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
import time
from ui.flash_screen import FlashScreen
from ui.f1boy_screen import F1BoyScreen
import lv_utils
import uasyncio
from common.resource_manager import ResourceManager

r1=ResourceManager()
r2=ResourceManager()


lv.init()
if not lv_utils.event_loop.is_running():
    print("LVGL VERSION:%d.%d.%d"%(lv.version_major(),lv.version_minor(),lv.version_patch()))
    display=DisplayDriver()
    touch_tensor=TouchDriver()
scr1=FlashScreen()
#加载Flash启动屏幕后，开启背光
display.backlight_on()
scr1.load()
uasyncio.wait_for(scr1.loadResouces(),100)
scr2=F1BoyScreen()
scr1.ChangeScreen(scr2)
print("协程任务框架循环开始")
uasyncio.Loop.run_forever()

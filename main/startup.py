from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
import time
from ui.flash_screen import FlashScreen
from ui.f1boy_screen import F1BoyScreen
import lv_utils
import uasyncio
from common.resource_manager import ResourceManager
lv.init()
print("LVGL VERSION:%d.%d.%d"%(lv.version_major(),lv.version_minor(),lv.version_patch()))
display=DisplayDriver()
touch_tensor=TouchDriver()
#开机动画
scr1=FlashScreen()
scr1.src_load()
#加载Flash启动屏幕后，开启背光
display.backlight_on()
uasyncio.run(scr1.loadResouces())
scr2=F1BoyScreen()
scr2.src_load_anim(fademode=lv.SCR_LOAD_ANIM.MOVE_TOP,speed=200)


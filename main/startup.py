# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()


from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
import time
from ui.flash_screen import FlashScreen
from ui.emoil_screen import EmoilScreen
from ui.wifiscan_screen import WiFiScanScreen
from ui.schedule_screen import ScheduleScreen
from ui.team_radio_screen import TeamRadioScreen
from ui.race_screen import RaceScreen
from ui.telemetry_screen import TelemetryScreen
from  ui.setup_screen import SetupScreen
import lv_utils
import uasyncio
from ui.theme_manager import ThemeManager, Themes

lv.init()
print("LVGL VERSION:%d.%d.%d" % (lv.version_major(), lv.version_minor(), lv.version_patch()))
display = DisplayDriver()
touch_tensor = TouchDriver()
theme = ThemeManager()
theme.ui_theme_manager_reset()
theme.ui_theme_set(Themes.UI_THEME_DEFAULT)
# 开机动画
scr1 = FlashScreen()
scr1.src_load()
# 加载Flash启动屏幕后，开启背光
display.backlight_on()
uasyncio.run(scr1.loadResouces())
# scr2=WiFiScanScreen()
#scr2 = ScheduleScreen()
#scr2 = EmoilScreen()
scr2 = RaceScreen()
#scr2 = TelemetryScreen()
#scr2 = SetupScreen()
scr2.src_load_anim(fademode=lv.SCR_LOAD_ANIM.MOVE_LEFT, speed=150)
print("协程任务框架循环开始")
while True:
    lv.task_handler()
    time.sleep(0.01)

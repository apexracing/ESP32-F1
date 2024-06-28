# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()
print("Run boot.py")
from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
from ui.theme_manager import ThemeManager, Themes
from common.wifi import *
from ui.flash_screen import FlashScreen
import uasyncio as asyncio

print("LVGL VERSION:%d.%d.%d" % (lv.version_major(), lv.version_minor(), lv.version_patch()))
display = DisplayDriver()
touch_tensor = TouchDriver()
theme = ThemeManager()
theme.ui_theme_manager_reset()
theme.ui_theme_set(Themes.UI_THEME_DEFAULT)


async def main():
    # 开机动画
    scr1 = FlashScreen()
    scr1.src_load()
    display.backlight_on()
    await scr1.loadResouces()
    await wifi_auto_connect()
    if is_wifi_connect():
        from common.time_driver import TimeDriver
        time_driver = TimeDriver()
        time_driver.init_sync_timer()


asyncio.run(main())

# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()


from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
import time
from common.wifi import *
from lib.microdot import Microdot
from ui.flash_screen import FlashScreen
from ui.emoil_screen import EmoilScreen
from ui.wifiscan_screen import WiFiScanScreen
from ui.schedule_screen import ScheduleScreen
from ui.team_radio_screen import TeamRadioScreen
from ui.race_screen import RaceScreen
from ui.telemetry_screen import TelemetryScreen
from ui.setup_screen import SetupScreen
from ui.tyre_screen import TyreScreen
import uasyncio as asyncio
from ui.theme_manager import ThemeManager, Themes

print("LVGL VERSION:%d.%d.%d" % (lv.version_major(), lv.version_minor(), lv.version_patch()))
display = DisplayDriver()
touch_tensor = TouchDriver()
theme = ThemeManager()
theme.ui_theme_manager_reset()
theme.ui_theme_set(Themes.UI_THEME_DEFAULT)
loop = asyncio.get_event_loop()
display.backlight_on()

print("协程任务框架循环开始")


async def main():
    await wifi_auto_connect()
    if is_wifi_connect():
        from common.time_driver import TimeDriver
        time_driver = TimeDriver()
        time_driver.init_sync_timer()
    scr = ScheduleScreen()
    scr.src_load_anim(fademode=lv.SCR_LOAD_ANIM.MOVE_BOTTOM, speed=50)
    while True:
        lv.task_handler()
        await asyncio.sleep_ms(10)

if __name__ == '__main__':
    asyncio.create_task(main())
    print('Program Started')
    loop.run_forever()
    print('Program Exit')

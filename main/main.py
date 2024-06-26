# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()

print("Run boot.py")

from common.display_driver import DisplayDriver
import lvgl as lv
from common.wifi import *
from ui.emoil_screen import EmoilScreen
from ui.wifiscan_screen import WiFiScanScreen
from ui.schedule_screen import ScheduleScreen
from ui.team_radio_screen import TeamRadioScreen
from ui.race_screen import RaceScreen
from ui.telemetry_screen import TelemetryScreen
from ui.setup_screen import SetupScreen
from ui.tyre_screen import TyreScreen
import uasyncio as asyncio
display = DisplayDriver()
loop = asyncio.get_event_loop()
async def main():
    print('main is runing!')

    if is_wifi_connect() is False:
        wifiScanScr = WiFiScanScreen()
        wifiScanScr.src_load_anim(fademode=lv.SCR_LOAD_ANIM.MOVE_BOTTOM, speed=50)
    else:
        scr2 = ScheduleScreen()
        scr2.src_load_anim(fademode=lv.SCR_LOAD_ANIM.MOVE_LEFT, speed=150)
    while True:
        lv.task_handler()
        await asyncio.sleep_ms(10)


if __name__ == '__main__':
    asyncio.create_task(main())
    print('Program Started')
    loop.run_forever()
    print('Program Exit')

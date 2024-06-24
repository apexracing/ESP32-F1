from common.wifi import *
import uasyncio as asyncio
from common.display_driver import DisplayDriver
from ui.theme_manager import ThemeManager, Themes

import lvgl as lv
from ui.flash_screen import FlashScreen
from ui.tyre_screen import TyreScreen

display = DisplayDriver()
theme = ThemeManager()
theme.ui_theme_manager_reset()
theme.ui_theme_set(Themes.UI_THEME_DEFAULT)
loop = asyncio.get_event_loop()


async def main():
    print('异步执行main')
    # 开机动画
    scr1 = FlashScreen()
    scr1.src_load()
    display.backlight_on()
    await scr1.loadResouces()
    scr2 = TyreScreen()
    scr2.src_load_anim(fademode=lv.SCR_LOAD_ANIM.MOVE_LEFT, speed=150)
    while True:
        lv.task_handler()
        await asyncio.sleep_ms(10)


if __name__ == '__main__':
    asyncio.create_task(main())
    print('Runing')
    loop.run_forever()
    print('Exit')

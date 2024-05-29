from common.touch_driver import TouchDriver
from common.display_driver import DisplayDriver
import lvgl as lv
import time
lv.init()
print("LVGL VERSION:%d.%d.%d"%(lv.version_major(),lv.version_minor(),lv.version_patch()))
display=DisplayDriver()
touch_tensor=TouchDriver()
import ui.main_ui
while True:
    lv.task_handler()
    time.sleep_ms(10)

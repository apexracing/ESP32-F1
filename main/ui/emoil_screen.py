import time

from ui.screen import Screen
import lvgl as lv
from ui.emoil import Emoil
import random
from lib.qmi_8658 import QMI8658


class EmoilScreen(Screen):
    def __init__(self):
        super().__init__()
        self.qmi8658 = None
        self.checkmiuTimer = None
        self.SetFlag(self.screen, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.screen.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        self.screen.set_style_bg_color(lv.color_hex(0x0A00A9), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_grad_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_main_stop(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_grad_stop(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_grad_dir(lv.GRAD_DIR.VER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_EmoilScreen_Image1 = lv.img(self.screen)
        self.ui_EmoilScreen_Image1.set_src(self.resourceManager.load_img("ui/assets/Helmet_RedBull.bin"))
        self.ui_EmoilScreen_Image1.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_EmoilScreen_Image1.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_EmoilScreen_Image1.set_align(lv.ALIGN.CENTER)

        self.ui_EmoilScreen_Image1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

        self.ui_EmoilScreen_Container1 = lv.obj(self.screen)
        self.ui_EmoilScreen_Container1.remove_style_all()
        self.ui_EmoilScreen_Container1.set_width(150)
        self.ui_EmoilScreen_Container1.set_height(80)
        self.ui_EmoilScreen_Container1.set_x(0)
        self.ui_EmoilScreen_Container1.set_y(15)
        self.ui_EmoilScreen_Container1.set_align(lv.ALIGN.CENTER)
        self.ui_EmoilScreen_Container1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
        self.ui_EmoilScreen_Container1.set_style_bg_color(lv.color_hex(0xFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        print("init1")

        self.turn_num = 0
        self.turn_num2 = 0
        self.turn_time = time.ticks_ms()
        self.turn_time2 = time.ticks_ms()
        self.total_emoil = 10
        self.current_emoil = 1
        self.last_emoil = Emoil(self.ui_EmoilScreen_Container1, f'ui/assets/e{self.current_emoil:02}.json')
        self.screen.add_event_cb(self.EmoilScreen_eventhandler, lv.EVENT.ALL, None)
        print("init2")
        lv.timer_create(self.timer_callback, 30000, None);
        self.cpu_low()
    def EmoilScreen_eventhandler(self, event_struct):
        event = event_struct.code
        if event == lv.EVENT.GESTURE:
            direction = lv.indev_t.get_gesture_dir(lv.indev_get_act())
            if direction & lv.DIR.LEFT == lv.DIR.LEFT:
                print("左滑")
            if direction & lv.DIR.RIGHT == lv.DIR.RIGHT:
                print("右滑")
        if event == lv.EVENT.SCREEN_LOAD_START and True:
            print("screen loaded")
            self.top_Animation(self.ui_EmoilScreen_Image1, 0)
        if event == lv.EVENT.SCREEN_LOADED:
            self.qmi8658 = QMI8658()
            self.checkmiuTimer = lv.timer_create(self.timer_callback, 200, None);
        if event == lv.EVENT.SCREEN_UNLOADED:
            lv.timer_del(self.checkmiuTimer)
            self.qmi8658.Close()
        return

    def timer_callback(self, timer):
        _, _, _, gyro_x, gyro_y, gyro_z = self.qmi8658.Read_Raw_XYZ()
        if abs(gyro_z) > 10000:
            # if gyro_z > 0:
            #     print("右转")
            # else:
            #     print("左转")
            old_emoil = self.current_emoil

            self.turn_num += 1
            self.turn_num2 += 1

            diff2 = time.ticks_diff(time.ticks_ms(), self.turn_time2)
            if diff2 >= 10000:  # 持续10秒内转动6次，固定播放炫晕表情
                if self.turn_num2 >= 6:
                    print("固定表情")
                    self.current_emoil = 5
                self.turn_num2 = 0
                self.turn_time2 = time.ticks_ms()
            diff = time.ticks_diff(time.ticks_ms(), self.turn_time)
            if diff >= 3000:
                if self.turn_num >= 3:
                    print("随机表情")
                    last_num = self.current_emoil
                    while self.current_emoil == last_num:
                        self.current_emoil = random.randint(1, self.total_emoil)
                self.turn_num = 0
                self.turn_time = time.ticks_ms()

            if old_emoil != self.current_emoil:
                Emoil(self.ui_EmoilScreen_Container1, f'ui/assets/e{self.current_emoil:02}.json')
        if abs(gyro_y) > 25000:
            if gyro_y > 0:
                print("前滚")
            else:
                print("后滚")
        if abs(gyro_x) > 25000:
            if gyro_x > 0:
                print("左倾斜")
            else:
                print("右倾斜")

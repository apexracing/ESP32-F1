from ui.screen import Screen
import lvgl as lv
from ui.assets import ui_images
from ui.emoil import Emoil
import random
class F1BoyScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x0084CD), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_img_src(ui_images.ui_img_helmet_redbull_png, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_EmoilScreen_Container2 = lv.obj(self.screen)
        ui_EmoilScreen_Container2.remove_style_all()
        ui_EmoilScreen_Container2.set_width(lv.pct(100))
        ui_EmoilScreen_Container2.set_height(lv.pct(100))
        ui_EmoilScreen_Container2.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_EmoilScreen_Container2, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_EmoilScreen_Container2, lv.obj.FLAG.SCROLLABLE, False)

        self.ui_EmoilScreen_Container1 = lv.obj(ui_EmoilScreen_Container2)
        self.ui_EmoilScreen_Container1.remove_style_all()
        self.ui_EmoilScreen_Container1.set_width(150)
        self.ui_EmoilScreen_Container1.set_height(80)
        self.ui_EmoilScreen_Container1.set_x(0)
        self.ui_EmoilScreen_Container1.set_y(15)
        self.ui_EmoilScreen_Container1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_EmoilScreen_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_EmoilScreen_Container1, lv.obj.FLAG.SCROLLABLE, False)
        self.total_emoil=10
        self.current_emoil=1
        self.last_emoil=Emoil(self.ui_EmoilScreen_Container1, f'ui/assets/e{self.current_emoil:02}.json')
        self.screen.add_event_cb(self.EmoilScreen_Container2_eventhandler, lv.EVENT.GESTURE, None)
        lv.timer_create(self.timer_callback,30000,None);

    def EmoilScreen_Container2_eventhandler(self,event_struct):
        event = event_struct.code
        if event == lv.EVENT.GESTURE:
            direction=lv.indev_t.get_gesture_dir(lv.indev_get_act())
            if direction & lv.DIR.LEFT == lv.DIR.LEFT:
                self.play_emoil_pre()
            if direction & lv.DIR.RIGHT == lv.DIR.RIGHT:
                self.play_emoil_next()
                    
                    
        return

    def timer_callback(self,timer):
        last_num=self.current_emoil
        while self.current_emoil == last_num:
            self.current_emoil=random.randint(1,self.total_emoil)
        Emoil(self.ui_EmoilScreen_Container1,f'ui/assets/e{self.current_emoil:02}.json')
        
    def play_emoil_next(self):
        if self.current_emoil== self.total_emoil:
            self.current_emoil=1
        else:
            self.current_emoil+=1
        Emoil(self.ui_EmoilScreen_Container1,f'ui/assets/e{self.current_emoil:02}.json')
    
    def play_emoil_pre(self):
        if self.current_emoil== 1:
            self.current_emoil=self.total_emoil
        else:
            self.current_emoil-=1
        Emoil(self.ui_EmoilScreen_Container1,f'ui/assets/e{self.current_emoil:02}.json')


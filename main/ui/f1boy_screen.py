from ui.screen import Screen
import lvgl as lv
from ui.assets import ui_images
from ui.emoil import Emoil
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
        self.ui_EmoilScreen_Container1.set_width(120)
        self.ui_EmoilScreen_Container1.set_height(80)
        self.ui_EmoilScreen_Container1.set_x(0)
        self.ui_EmoilScreen_Container1.set_y(20)
        self.ui_EmoilScreen_Container1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_EmoilScreen_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_EmoilScreen_Container1, lv.obj.FLAG.SCROLLABLE, False)
        self.last_emoil=Emoil(self.ui_EmoilScreen_Container1, 'ui/assets/e01.json')
        self.screen.add_event_cb(self.EmoilScreen_Container2_eventhandler, lv.EVENT.ALL, None)

    def EmoilScreen_Container2_eventhandler(self,event_struct):
        event = event_struct.code
        if event == lv.EVENT.RELEASED:
            self.play_emoil(event_struct)
        return

    def play_emoil(self,event_struct):
        self.ui_EmoilScreen_Container1.clean()
        self.last_emoil=Emoil(self.ui_EmoilScreen_Container1,'ui/assets/e02.json',False,self.last_emoil)


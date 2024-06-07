from ui.screen import Screen
import lvgl as lv
from ui.assets import ui_images
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

        ui_EmoilScreen_Container1 = lv.obj(ui_EmoilScreen_Container2)
        ui_EmoilScreen_Container1.remove_style_all()
        ui_EmoilScreen_Container1.set_width(120)
        ui_EmoilScreen_Container1.set_height(80)
        ui_EmoilScreen_Container1.set_x(0)
        ui_EmoilScreen_Container1.set_y(20)
        ui_EmoilScreen_Container1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_EmoilScreen_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_EmoilScreen_Container1, lv.obj.FLAG.SCROLLABLE, False)
        lottie_data = self.resourceManager.load_raw('ui/assets/e01.json')
        lottie1 = lv.rlottie_create_from_raw(ui_EmoilScreen_Container1, 150, 80, lottie_data)
        lottie1.set_width(lv.SIZE.CONTENT)  # 1
        lottie1.set_height(lv.SIZE.CONTENT)  # 1
        lottie1.set_align(lv.ALIGN.CENTER)
        ui_EmoilScreen_Container2.add_event_cb(self.EmoilScreen_Container2_eventhandler, lv.EVENT.ALL, None)

        def EmoilScreen_Container2_eventhandler(self,event_struct):
            event = event_struct.code
            if event == lv.EVENT.RELEASED and True:
                self.play_emoil(event_struct)
            return

        def play_emoil(self,event_struct):
            pass

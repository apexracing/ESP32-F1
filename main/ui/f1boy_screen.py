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

        ui_EmoilScreen_Container1 = lv.obj(self.screen)
        ui_EmoilScreen_Container1.remove_style_all()
        ui_EmoilScreen_Container1.set_width(120)
        ui_EmoilScreen_Container1.set_height(80)
        ui_EmoilScreen_Container1.set_x(0)
        ui_EmoilScreen_Container1.set_y(20)
        ui_EmoilScreen_Container1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_EmoilScreen_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_EmoilScreen_Container1, lv.obj.FLAG.SCROLLABLE, False)
        lottie_data = self.resourceManager.load_raw('ui/assets/e01.json')
        lottie1 = lv.rlottie_create_from_raw(ui_EmoilScreen_Container1, 120, 80, lottie_data)
        lottie1.set_width(lv.SIZE.CONTENT)  # 1
        lottie1.set_height(lv.SIZE.CONTENT)  # 1
        lottie1.set_align(lv.ALIGN.CENTER)

        async def loadResouces(self):
            self.resourceManager.load_raw('ui/assets/e01.json')
            self.resourceManager.load_raw('ui/assets/Helmet_RedBull.png')
            self.resourceManager.load_font("F1R", 14)
            self.resourceManager.load_font("F1R", 16)
            for i in range(16, 28, 2):
                self.resourceManager.load_font("F1B", i)
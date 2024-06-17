from ui.screen import Screen
import lvgl as lv
import uasyncio

class FlashScreen(Screen):
    def __init__(self):
        super().__init__()
        self.ui_Flash_Label5 = lv.label(self.screen)
        self.ui_Flash_Label5.set_text("SPEED IMPRINT")
        self.ui_Flash_Label5.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Flash_Label5.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Flash_Label5.set_align(lv.ALIGN.CENTER)
        self.ui_Flash_Label5.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Flash_Label5.set_style_text_font(self.resourceManager.load_font("F1B",22), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.add_event_cb(self.Flash_eventhandler, lv.EVENT.ALL, None)

    def Flash_eventhandler(self,event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOADED and True:
            self.Flash_Animation(self.ui_Flash_Label5, 0)
        return

    async def loadResouces(self):
        await uasyncio.sleep(2)
        self.resourceManager.load_font("F1B", 22)
        self.resourceManager.load_font("DISPLAYB", 14)
        self.resourceManager.load_font("DISPLAYM", 10)
        self.resourceManager.load_font("DISPLAYM", 14)
        self.resourceManager.load_font("DISPLAYR", 30)
        self.resourceManager.load_font("DISPLAYR", 60)
        self.resourceManager.load_font("F1R", 14)
        # for i in range(1,10):
        #     self.resourceManager.load_raw(f'ui/assets/e{i:02}.json')
        # for i in range(8, 30, 2):
        #     self.resourceManager.load_font("DISPLAYR", i)
        # for i in range(10, 20, 2):
        #     self.resourceManager.load_font("F1R", i)
        # for i in range(16, 28, 2):
        #     self.resourceManager.load_font("F1B", i)

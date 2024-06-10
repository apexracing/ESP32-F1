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
    def Flash_Animation(self,TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_ease_in_out)
        PropertyAnimation_0.set_time(1000)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_style_text_opa(v,lv.PART.MAIN | lv.STATE.DEFAULT))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(lv.ANIM_REPEAT.INFINITE)
        PropertyAnimation_0.set_repeat_delay(0)  # + 1000
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(1000)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(255, 100)
        lv.anim_t.start(PropertyAnimation_0)
        print("Flash_Animation called")
        return True

    async def loadResouces(self):
        await uasyncio.sleep(3)
        for i in range(1,10):
            self.resourceManager.load_raw(f'ui/assets/e{i:02}.json')
        self.resourceManager.load_font("F1R", 14)
        self.resourceManager.load_font("F1R", 16)
        for i in range(16, 28, 2):
            self.resourceManager.load_font("F1B", i)

from ui.screen import Screen
import lvgl as lv


class WiFiScanScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        qr = lv.qrcode(self.screen, 100, lv.color_hex(0x000000), lv.color_hex(0xFFFFFF))
        qr.set_align(lv.ALIGN.CENTER)
        qr.set_x(0)
        qr.set_y(27)
        data = "http://192.168.0.1"
        qr.update(data, len(data))
        self.ui_QCodeTitle = lv.label(self.screen)
        self.ui_QCodeTitle.set_text("1:使用手机连接WIFI热点:\n  F1-LiveTime\n2:扫描下方二维码")
        self.ui_QCodeTitle.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_QCodeTitle.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_QCodeTitle.set_x(0)
        self.ui_QCodeTitle.set_y(-59)
        self.ui_QCodeTitle.set_align(lv.ALIGN.CENTER)
        self.ui_QCodeTitle.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_QCodeTitle.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_QCodeTitle.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_QCodeTitle.set_style_text_font(self.resourceManager.load_font("Chinese", 12),
                                               lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen.add_event_cb(self.WiFiScan_eventhandler, lv.EVENT.ALL, None)

    def WiFiScan_eventhandler(self, event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOADED and True:
            self.top_Animation(self.ui_QCodeTitle, 0)
        return

from ui.screen import Screen
import lvgl as lv
from lib.microdot import Microdot, URLPattern, Response
from common.wifi import *
import uasyncio as asyncio
import machine
from ui.theme_manager import Themes
from ui.components import PageComponent

class WiFiScanScreen(Screen):
    def __init__(self):
        super().__init__()
        # UI 配置HttpServer
        self.app = Microdot()

        Response.default_content_type = "application/json"
        self.app.url_map.append((["GET", "POST"], URLPattern("/"), self.wifi))
        self.app.url_map.append((["GET", "POST"], URLPattern("/wifi_result"), self.wifi_result))
        self.app.url_map.append((["GET", "POST"], URLPattern("/wifi_try"), self.wifi_try))
        self.app.url_map.append((["GET", "POST"], URLPattern("/wifi_try_msg"), self.wifi_try_msg))
        self.app.url_map.append((["GET", "POST"], URLPattern('/static/<path:path>'), self.static))

        # 用于显示连网过程消息
        self.wifi_msg = []
        # UI 部分
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_WiFiScanStep1 = lv.obj(self.screen)
        ui_WiFiScanStep1.remove_style_all()
        ui_WiFiScanStep1.set_width(lv.pct(100))
        ui_WiFiScanStep1.set_height(lv.pct(100))
        ui_WiFiScanStep1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_WiFiScanStep1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_WiFiScanStep1, lv.obj.FLAG.SCROLLABLE, False)

        ui_WiFiScan_Image4 = lv.img(ui_WiFiScanStep1)
        ui_WiFiScan_Image4.set_src(self.resourceManager.load_img("ui/assets/wifi_first_setup.bin",width=200,height=106))
        ui_WiFiScan_Image4.set_width(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Image4.set_height(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Image4.set_x(0)
        ui_WiFiScan_Image4.set_y(21)
        ui_WiFiScan_Image4.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_WiFiScan_Image4, lv.obj.FLAG.ADV_HITTEST, True)
        self.SetFlag(ui_WiFiScan_Image4, lv.obj.FLAG.SCROLLABLE, False)

        self.ui_WiFiScan_Container1 = lv.obj(ui_WiFiScanStep1)
        self.ui_WiFiScan_Container1.remove_style_all()
        self.ui_WiFiScan_Container1.set_width(240)
        self.ui_WiFiScan_Container1.set_height(240)
        self.ui_WiFiScan_Container1.set_x(0)
        self.ui_WiFiScan_Container1.set_y(0)
        self.ui_WiFiScan_Container1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_WiFiScan_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_WiFiScan_Container1, lv.obj.FLAG.SCROLLABLE, False)

        ui_QCodeTitle = lv.label(self.ui_WiFiScan_Container1)
        ui_QCodeTitle.set_text("第一步\n手机连接以下Wi-Fi")
        ui_QCodeTitle.set_width(lv.SIZE.CONTENT)  # 1
        ui_QCodeTitle.set_height(lv.SIZE.CONTENT)  # 1
        ui_QCodeTitle.set_x(-2)
        ui_QCodeTitle.set_y(-86)
        ui_QCodeTitle.set_align(lv.ALIGN.CENTER)
        ui_QCodeTitle.set_style_text_color(lv.color_hex(0x393939), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_QCodeTitle.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_QCodeTitle.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_QCodeTitle.set_style_text_font(self.resourceManager.load_font("ChineseB", 16), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_WiFiScan_Label3 = lv.label(self.ui_WiFiScan_Container1)
        ui_WiFiScan_Label3.set_text("Wi-Fi密码:12345678")
        ui_WiFiScan_Label3.set_width(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Label3.set_height(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Label3.set_x(0)
        ui_WiFiScan_Label3.set_y(-48)
        ui_WiFiScan_Label3.set_align(lv.ALIGN.CENTER)
        ui_WiFiScan_Label3.set_style_text_color(lv.color_hex(0x5A595A), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WiFiScan_Label3.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WiFiScan_Label3.set_style_text_font(self.resourceManager.load_font("Chinese", 12), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_WiFiScanStep2 = lv.obj(self.screen)
        ui_WiFiScanStep2.remove_style_all()
        ui_WiFiScanStep2.set_width(lv.pct(100))
        ui_WiFiScanStep2.set_height(lv.pct(100))
        ui_WiFiScanStep2.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_WiFiScanStep2, lv.obj.FLAG.HIDDEN, True)
        self.SetFlag(ui_WiFiScanStep2, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_WiFiScanStep2, lv.obj.FLAG.SCROLLABLE, False)

        ui_QCodeTitle2 = lv.label(ui_WiFiScanStep2)
        ui_QCodeTitle2.set_text("第二步\n打开手机浏览器")
        ui_QCodeTitle2.set_width(lv.SIZE.CONTENT)  # 1
        ui_QCodeTitle2.set_height(lv.SIZE.CONTENT)  # 1
        ui_QCodeTitle2.set_x(-2)
        ui_QCodeTitle2.set_y(-86)
        ui_QCodeTitle2.set_align(lv.ALIGN.CENTER)
        ui_QCodeTitle2.set_style_text_color(lv.color_hex(0x393939), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_QCodeTitle2.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_QCodeTitle2.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_QCodeTitle2.set_style_text_font(self.resourceManager.load_font("ChineseB", 16), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_WiFiScan_Label2 = lv.label(ui_WiFiScanStep2)
        ui_WiFiScan_Label2.set_text("在地址栏中输入\"192.168.1.1\"")
        ui_WiFiScan_Label2.set_width(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Label2.set_height(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Label2.set_x(-1)
        ui_WiFiScan_Label2.set_y(-48)
        ui_WiFiScan_Label2.set_align(lv.ALIGN.CENTER)
        ui_WiFiScan_Label2.set_style_text_color(lv.color_hex(0x5A595A), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WiFiScan_Label2.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WiFiScan_Label2.set_style_text_font(self.resourceManager.load_font("Chinese", 12), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_WiFiScan_Image2 = lv.img(ui_WiFiScanStep2)
        ui_WiFiScan_Image2.set_src(self.resourceManager.load_img("ui/assets/wifi_second_setup.bin",width=200,height=72))
        ui_WiFiScan_Image2.set_width(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Image2.set_height(lv.SIZE.CONTENT)  # 1
        ui_WiFiScan_Image2.set_x(0)
        ui_WiFiScan_Image2.set_y(14)
        ui_WiFiScan_Image2.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_WiFiScan_Image2, lv.obj.FLAG.ADV_HITTEST, True)
        self.SetFlag(ui_WiFiScan_Image2, lv.obj.FLAG.SCROLLABLE, False)

        self.pageComponent=PageComponent(self.screen,[ui_WiFiScanStep1,ui_WiFiScanStep2],0,84)
        self.screen.add_event_cb(self.WiFiScan_eventhandler, lv.EVENT.ALL, None)

    # def ui_Page_Container_create(self,comp_parent,pages):
    #     cui_Page_Container = lv.obj(comp_parent)
    #     cui_Page_Container.remove_style_all()
    #     cui_Page_Container.set_width(14)
    #     cui_Page_Container.set_height(10)
    #     cui_Page_Container.set_x(0)
    #     cui_Page_Container.set_y(84)
    #     cui_Page_Container.set_align(lv.ALIGN.CENTER)
    #     cui_Page_Container.set_flex_flow(lv.FLEX_FLOW.ROW)
    #     cui_Page_Container.set_flex_align(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.SPACE_AROUND)
    #     self.SetFlag(cui_Page_Container, lv.obj.FLAG.CLICKABLE, False)
    #     self.SetFlag(cui_Page_Container, lv.obj.FLAG.SCROLLABLE, False)
    #     cui_Page1 = lv.btn(cui_Page_Container)
    #     cui_Page1.set_width(4)
    #     cui_Page1.set_height(4)
    #     cui_Page1.set_align(lv.ALIGN.CENTER)
    #     self.SetFlag(cui_Page1, lv.obj.FLAG.SCROLLABLE, False)
    #     self.SetFlag(cui_Page1, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
    #     self.themeManager.ui_object_set_themeable_style_property(cui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.BG_COLOR,
    #                                            Themes.UI_THEME_COLOR_COLORTEAM)
    #     self.themeManager.ui_object_set_themeable_style_property(cui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.BG_OPA,
    #                                            Themes.UI_THEME_COLOR_COLORTEAM)
    #     self.themeManager.ui_object_set_themeable_style_property(cui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.SHADOW_COLOR,
    #                                            Themes.UI_THEME_COLOR_COLORTEAM)
    #     self.themeManager.ui_object_set_themeable_style_property(cui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.SHADOW_OPA,
    #                                            Themes.UI_THEME_COLOR_COLORTEAM)
    #     cui_Page1.set_style_shadow_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
    #     cui_Page1.set_style_shadow_spread(1, lv.PART.MAIN | lv.STATE.DEFAULT)
    #     cui_Page2 = lv.btn(cui_Page_Container)
    #     cui_Page2.set_width(4)
    #     cui_Page2.set_height(4)
    #     cui_Page2.set_align(lv.ALIGN.CENTER)
    #     self.SetFlag(cui_Page2, lv.obj.FLAG.SCROLLABLE, False)
    #     self.SetFlag(cui_Page2, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
    #     cui_Page2.set_style_bg_color(lv.color_hex(0x9A9A9A), lv.PART.MAIN | lv.STATE.DEFAULT)
    #     cui_Page2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    #
    #     self._ui_comp_table[id(cui_Page_Container)] = {"Page_Container": cui_Page_Container, "Page1": cui_Page1,
    #                                               "Page2": cui_Page2, "_CompName": "Page Container"}
    #     return cui_Page_Container

    def WiFiScan_eventhandler(self, event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOAD_START:
            self.top_Animation(self.ui_WiFiScan_Container1, 0)
        if event == lv.EVENT.SCREEN_LOADED:
            asyncio.create_task(self.run())
        if event == lv.EVENT.GESTURE:
            direction = lv.indev_t.get_gesture_dir(lv.indev_get_act())
            if direction & lv.DIR.LEFT == lv.DIR.LEFT:
                self.pageComponent.nextPage()
            if direction & lv.DIR.RIGHT == lv.DIR.RIGHT:
                self.pageComponent.prePage()
    async def run(self):
        # 开启配网模式
        start_ap(essid='F1-LiveTime', hostname="speedim.cn")
        print("MicroDot WebServer Running!")
        await self.app.start_server(port=80, debug=True)

    async def wifi(self, request):
        wifiList = wifi_scan()
        from lib.tpl import Template
        wifi_index = Template("wifi_index.html")
        return Response.send_file(filename="wifi_index.html", content_type="text/html",
                                  stream=wifi_index.render(wifis=wifiList))

    async def wifi_result(self, request):
        return Response.send_file("ui/html/wifi_result.html", content_type="text/html")
    async def wifi_connect_delay(self,ssid,pwd):
        await asyncio.sleep_ms(3000) #延迟3秒后，刷新到下一个页面再开始连接wifi
        asyncio.create_task(connect_wifi(ssid, pwd, self.wifi_conn_callback))
    async def wifi_try(self, request):
        ssid = request.json['ssid']
        pwd = request.json['pwd']
        self.wifi_msg.clear()
        print(f"用户正在配置网络->ssid:{ssid},pwd:{pwd}")
        asyncio.create_task(self.wifi_connect_delay(ssid,pwd))
        return Response({'code': 0, 'msg': "OK"}, 200,
                        {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "*",
                         "Content-Type": "application/json; charset=UTF-8"}, None)

    async def wifi_try_msg(self, request):
        is_ok = is_wifi_connect()
        if is_ok:
            asyncio.create_task(self.shutdown())
            self.wifi_msg.append({'msg': "已连接成功，设备将在5秒后自动重启.", 'flag': 1})
        return Response(self.wifi_msg, 200,
                        {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "*",
                         "Content-Type": "application/json; charset=UTF-8"}, None)

    async def static(self, request, path):
        print(f"static->{path}")
        if '..' in path:
            # directory traversal is not allowed
            return 'Not found', 404
        return Response.send_file('ui/html/static/' + path)

    def wifi_conn_callback(self, msg, flag, ssid=None, password=None):
        print(msg)
        self.wifi_msg.append({'msg': msg, 'flag': flag})
        if flag == 1:
            wifi_data[ssid] = password
            wifi_cfg_flush()

    async def shutdown(self):
        print("5秒后，设备将会重启...")
        await asyncio.sleep_ms(5000)
        self.app.shutdown()
        #self.dns.shutdown()
        machine.reset()

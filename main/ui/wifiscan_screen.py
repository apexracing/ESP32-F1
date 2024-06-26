from ui.screen import Screen
import lvgl as lv
from lib.microdot import Microdot, URLPattern, Response
from common.wifi import *
import uasyncio as asyncio
import machine


class WiFiScanScreen(Screen):
    def __init__(self):
        super().__init__()
        # UI 配置HttpServer
        self.app = Microdot()
        Response.default_content_type = "application/json"
        self.app.url_map.append((["GET"], URLPattern("/wifi"), self.wifi))
        self.app.url_map.append((["GET"], URLPattern("/wifi_result"), self.wifi_result))
        self.app.url_map.append((["POST"], URLPattern("/wifi_try"), self.wifi_try))
        self.app.url_map.append((["GET"], URLPattern("/wifi_try_msg"), self.wifi))
        self.app.url_map.append((["GET"], URLPattern('/static/<path:path>'), self.static))
        #用于显示连网过程消息
        self.wifi_msg = ""
        self.wifi_conn_flag = 0
        # UI 部分
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        qr = lv.qrcode(self.screen, 100, lv.color_hex(0x000000), lv.color_hex(0xFFFFFF))
        qr.set_align(lv.ALIGN.CENTER)
        qr.set_x(0)
        qr.set_y(27)
        data = "http://192.168.1.1/wifi"
        qr.update(data, len(data))
        self.ui_QCodeTitle = lv.label(self.screen)
        self.ui_QCodeTitle.set_text("1:使用手机连接Wi-Fi:\n  F1-LiveTime\n2:扫描下方二维码")
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
        if event == lv.EVENT.SCREEN_LOAD_START and True:
            self.top_Animation(self.ui_QCodeTitle, 0)
        if event == lv.EVENT.SCREEN_LOADED:
            asyncio.create_task(self.run())
        return

    async def run(self):
        # 开启配网模式
        start_ap(essid='F1-LiveTime', hostname="speedim.cn")
        print("MicroDot WebServer Running!")
        await self.app.start_server(port=80, debug=True)

    async def wifi(self, request):
        global wifi
        wifiList = wifi.scan()
        from lib.tpl import Template
        wifi_index = Template("wifi_index.html")
        return Response.send_file(filename="wifi_index.html", content_type="text/html",
                                  stream=wifi_index.render(wifis=wifiList))

    async def wifi_result(self, request):
        return Response.send_file("ui/html/wifi_result.html", content_type="text/html")

    async def wifi_try(self, request):
        ssid = request.json['ssid']
        pwd = request.json['pwd']
        print(f"用户正在配置网络->ssid:{ssid},pwd:{pwd}")
        await connect_wifi(ssid, pwd, self.wifi_conn_callback)
        return "ok"

    async def wifi_try_msg(self, request):
        print(self.wifi_msg)
        is_ok = is_wifi_connect()
        if is_ok:
            asyncio.create_task(self.shutdown)
            return {'code': self.wifi_conn_flag, "msg": "已连接成功，设备将在5秒后自动重启."}
        else:
            return {'code': self.wifi_conn_flag, 'msg': self.wifi_msg}

    async def static(self, request, path):
        print(f"static->{path}")
        if '..' in path:
            # directory traversal is not allowed
            return 'Not found', 404
        return Response.send_file('ui/html/static/' + path)

    def wifi_conn_callback(self, msg, flag):
        self.wifi_msg = msg
        self.wifi_conn_flag = flag

    async def shutdown(self, timer):
        asyncio.sleep_ms(5000)
        self.app.shutdown()
        machine.reset()

import lvgl as lv
from ui.screen import Screen
from ui.theme_manager import Themes, ThemeManager
class SetupScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_radius(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_main_stop(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_grad_stop(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_grad_dir(lv.GRAD_DIR.VER, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_WifiMenuItem = lv.obj(self.screen)
        self.ui_WifiMenuItem.remove_style_all()
        self.ui_WifiMenuItem.set_width(130)
        self.ui_WifiMenuItem.set_height(40)
        self.ui_WifiMenuItem.set_x(50)
        self.ui_WifiMenuItem.set_y(-60)
        self.ui_WifiMenuItem.set_align(lv.ALIGN.LEFT_MID)
        self.ui_WifiMenuItem.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.ui_WifiMenuItem.set_flex_align(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.SetFlag(self.ui_WifiMenuItem, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_WifiMenuItem, lv.obj.FLAG.SCROLLABLE, False)

        ui_WifiMenuIcon = lv.obj(self.ui_WifiMenuItem)
        ui_WifiMenuIcon.set_width(40)
        ui_WifiMenuIcon.set_height(40)
        ui_WifiMenuIcon.set_x(-44)
        ui_WifiMenuIcon.set_y(-50)
        ui_WifiMenuIcon.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_WifiMenuIcon, lv.obj.FLAG.SCROLLABLE, False)
        ui_WifiMenuIcon.set_style_radius(90, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_bg_color(lv.color_hex(0x01A3D8), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_border_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_border_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_border_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_shadow_color(lv.color_hex(0x01A3D8), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_shadow_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_shadow_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WifiMenuIcon.set_style_shadow_spread(1, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen_Label1 = lv.label(ui_WifiMenuIcon)
        self.screen_Label1.set_text("")
        self.screen_Label1.set_width(lv.SIZE.CONTENT)  # 1
        self.screen_Label1.set_height(lv.SIZE.CONTENT)  # 1
        self.screen_Label1.set_align(lv.ALIGN.CENTER)
        self.screen_Label1.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label1.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label1.set_style_text_font(lv.font_load(f"Z:ui/fonts/ui_font_SetupIcons.bin"), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_WifiMenuLabel = lv.label(self.ui_WifiMenuItem)
        ui_WifiMenuLabel.set_text("WiFi")
        ui_WifiMenuLabel.set_width(lv.SIZE.CONTENT)  # 1
        ui_WifiMenuLabel.set_height(lv.SIZE.CONTENT)  # 1
        ui_WifiMenuLabel.set_x(16)
        ui_WifiMenuLabel.set_y(-51)
        ui_WifiMenuLabel.set_align(lv.ALIGN.CENTER)
        ui_WifiMenuLabel.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 24), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_TeamMenuItem = lv.obj(self.screen)
        self.ui_TeamMenuItem.remove_style_all()
        self.ui_TeamMenuItem.set_width(130)
        self.ui_TeamMenuItem.set_height(40)
        self.ui_TeamMenuItem.set_x(20)
        self.ui_TeamMenuItem.set_y(0)
        self.ui_TeamMenuItem.set_align(lv.ALIGN.LEFT_MID)
        self.ui_TeamMenuItem.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.ui_TeamMenuItem.set_flex_align(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.SetFlag(self.ui_TeamMenuItem, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_TeamMenuItem, lv.obj.FLAG.SCROLLABLE, False)

        ui_TeamMenuIcon = lv.obj(self.ui_TeamMenuItem)
        ui_TeamMenuIcon.set_width(40)
        ui_TeamMenuIcon.set_height(40)
        ui_TeamMenuIcon.set_x(-66)
        ui_TeamMenuIcon.set_y(5)
        ui_TeamMenuIcon.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_TeamMenuIcon, lv.obj.FLAG.SCROLLABLE, False)
        ui_TeamMenuIcon.set_style_radius(90, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_bg_color(lv.color_hex(0x970FDB), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_bg_opa(970, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_border_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_border_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_border_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_shadow_color(lv.color_hex(0x970FDB), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_shadow_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_shadow_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TeamMenuIcon.set_style_shadow_spread(1, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen_Label3 = lv.label(ui_TeamMenuIcon)
        self.screen_Label3.set_text("")
        self.screen_Label3.set_width(lv.SIZE.CONTENT)  # 1
        self.screen_Label3.set_height(lv.SIZE.CONTENT)  # 1
        self.screen_Label3.set_align(lv.ALIGN.CENTER)
        self.screen_Label3.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label3.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label3.set_style_text_font(lv.font_load(f"Z:ui/fonts/ui_font_SetupIcons.bin"), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_TeamMenuLabel = lv.label(self.ui_TeamMenuItem)
        ui_TeamMenuLabel.set_text("Theme")
        ui_TeamMenuLabel.set_width(lv.SIZE.CONTENT)  # 1
        ui_TeamMenuLabel.set_height(lv.SIZE.CONTENT)  # 1
        ui_TeamMenuLabel.set_x(6)
        ui_TeamMenuLabel.set_y(-58)
        ui_TeamMenuLabel.set_align(lv.ALIGN.CENTER)
        ui_TeamMenuLabel.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 24), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_DriverMenuItem = lv.obj(self.screen)
        self.ui_DriverMenuItem.remove_style_all()
        self.ui_DriverMenuItem.set_width(130)
        self.ui_DriverMenuItem.set_height(40)
        self.ui_DriverMenuItem.set_x(50)
        self.ui_DriverMenuItem.set_y(60)
        self.ui_DriverMenuItem.set_align(lv.ALIGN.LEFT_MID)
        self.ui_DriverMenuItem.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.ui_DriverMenuItem.set_flex_align(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.SetFlag(self.ui_DriverMenuItem, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_DriverMenuItem, lv.obj.FLAG.SCROLLABLE, False)

        ui_DriverMenuIcon = lv.obj(self.ui_DriverMenuItem)
        ui_DriverMenuIcon.set_width(40)
        ui_DriverMenuIcon.set_height(40)
        ui_DriverMenuIcon.set_x(-40)
        ui_DriverMenuIcon.set_y(69)
        ui_DriverMenuIcon.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_DriverMenuIcon, lv.obj.FLAG.SCROLLABLE, False)
        ui_DriverMenuIcon.set_style_radius(90, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_bg_color(lv.color_hex(0xFF0101), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_border_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_border_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_border_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_shadow_color(lv.color_hex(0xFF0101), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_shadow_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_shadow_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_DriverMenuIcon.set_style_shadow_spread(1, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen_Label4 = lv.label(ui_DriverMenuIcon)
        self.screen_Label4.set_text("")
        self.screen_Label4.set_width(lv.SIZE.CONTENT)  # 1
        self.screen_Label4.set_height(lv.SIZE.CONTENT)  # 1
        self.screen_Label4.set_align(lv.ALIGN.CENTER)
        self.screen_Label4.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label4.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label4.set_style_text_font(lv.font_load(f"Z:ui/fonts/ui_font_SetupIcons.bin"), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_DriverMenuLabel = lv.label(self.ui_DriverMenuItem)
        ui_DriverMenuLabel.set_text("Driver")
        ui_DriverMenuLabel.set_width(lv.SIZE.CONTENT)  # 1
        ui_DriverMenuLabel.set_height(lv.SIZE.CONTENT)  # 1
        ui_DriverMenuLabel.set_x(23)
        ui_DriverMenuLabel.set_y(70)
        ui_DriverMenuLabel.set_align(lv.ALIGN.CENTER)
        ui_DriverMenuLabel.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 24), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen.add_event_cb(self.SetupScreen_eventhandler, lv.EVENT.ALL, None)


    def SetupScreen_eventhandler(self,event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOAD_START and True:
            self.right_Animation(self.ui_WifiMenuItem, 0)
            self.right_Animation(self.ui_TeamMenuItem, 0)
            self.left_Animation(self.ui_DriverMenuItem, 0)
        return
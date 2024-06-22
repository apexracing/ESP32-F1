import lvgl as lv
from ui.screen import Screen
from ui.theme_manager import Themes, ThemeManager
class TelemetryScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_SPEED_Arc = lv.arc(self.screen)
        self.ui_SPEED_Arc.set_width(230)
        self.ui_SPEED_Arc.set_height(230)
        self.ui_SPEED_Arc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.GESTURE_BUBBLE, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(self.ui_SPEED_Arc, lv.obj.FLAG.SCROLL_CHAIN, False)
        self.ui_SPEED_Arc.set_range(0, 360)
        self.ui_SPEED_Arc.set_value(280)
        self.ui_SPEED_Arc.set_bg_angles(0, 280)
        self.ui_SPEED_Arc.set_rotation(130)
        self.ui_SPEED_Arc.set_style_arc_color(lv.color_hex(0x3D3D3D), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_SPEED_Arc.set_style_arc_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_SPEED_Arc.set_style_arc_width(17, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_SPEED_Arc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Speed_Arc.set_style_arc_color(lv.color_hex(0x0093CC), lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Speed_Arc.set_style_arc_opa(255, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_SPEED_Arc.set_style_arc_width(17, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_SPEED_Arc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        #self.ui_SPEED_Arc.set_style_arc_img_src(ui_images.ui_img_speed_png, lv.PART.INDICATOR | lv.STATE.DEFAULT)
    

        self.ui_Throttle_Arc = lv.arc(self.screen)
        self.ui_Throttle_Arc.set_width(190)
        self.ui_Throttle_Arc.set_height(190)

        self.ui_Throttle_Arc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.EVENT_BUBBLE, True)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(self.ui_Throttle_Arc, lv.obj.FLAG.SCROLL_CHAIN, False)
        self.ui_Throttle_Arc.set_value(80)
        self.ui_Throttle_Arc.set_bg_angles(0, 178)
        self.ui_Throttle_Arc.set_rotation(130)
        self.ui_Throttle_Arc.set_style_arc_color(lv.color_hex(0x3D3D3D), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_arc_opa(200, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_arc_width(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Throttle_Arc.set_style_arc_color(lv.color_hex(0x00FD3B), lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_arc_opa(255, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_arc_width(20, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        #self.ui_Throttle_Arc.set_style_arc_img_src(ui_images.ui_img_throttle_png, lv.PART.INDICATOR | lv.STATE.DEFAULT)
    
        self.ui_Throttle_Arc.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_Throttle_Arc.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_Brake_Arc = lv.arc(self.screen)
        self.ui_Brake_Arc.set_width(190)
        self.ui_Brake_Arc.set_height(190)
        self.ui_Brake_Arc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.EVENT_BUBBLE, True)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(self.ui_Brake_Arc, lv.obj.FLAG.SCROLL_CHAIN, False)
        self.ui_Brake_Arc.set_value(40)
        self.ui_Brake_Arc.set_bg_angles(0, 100)
        self.ui_Brake_Arc.set_mode(self.ui_Brake_Arc.MODE.REVERSE)
        self.ui_Brake_Arc.set_rotation(310)
        self.ui_Brake_Arc.set_style_arc_color(lv.color_hex(0x3D3D3D), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_arc_opa(200, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_arc_width(20, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Brake_Arc.set_style_arc_color(lv.color_hex(0xFF0101), lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_arc_opa(255, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_arc_width(20, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        #self.ui_Brake_Arc.set_style_arc_img_src(ui_images.ui_img_brake_png, lv.PART.INDICATOR | lv.STATE.DEFAULT)
    
        self.ui_Brake_Arc.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_Brake_Arc.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
    
        self.ui_Gear = lv.label(self.screen)
        self.ui_Gear.set_text("N")
        self.ui_Gear.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Gear.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Gear.set_x(0)
        self.ui_Gear.set_y(-18)
        self.ui_Gear.set_align(lv.ALIGN.CENTER)
        self.ui_Gear.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Gear.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Gear.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Gear.set_style_text_font(self.resourceManager.load_font("DISPLAYB", 80), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Gear_Label = lv.label(self.screen)
        self.ui_Gear_Label.set_text("GEAR")
        self.ui_Gear_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Gear_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Gear_Label.set_x(-45)
        self.ui_Gear_Label.set_y(-25)
        self.ui_Gear_Label.set_align(lv.ALIGN.CENTER)
        self.ui_Gear_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Gear_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Gear_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_RPM_Label = lv.label(self.screen)
        self.ui_RPM_Label.set_text("RPM")
        self.ui_RPM_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_RPM_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_RPM_Label.set_x(0)
        self.ui_RPM_Label.set_y(41)
        self.ui_RPM_Label.set_align(lv.ALIGN.CENTER)
        self.ui_RPM_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_RPM_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_RPM_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_KHM_Label = lv.label(self.screen)
        ui_KHM_Label.set_text("KHM")
        ui_KHM_Label.set_width(lv.SIZE.CONTENT)  # 1
        ui_KHM_Label.set_height(lv.SIZE.CONTENT)  # 1
        ui_KHM_Label.set_x(43)
        ui_KHM_Label.set_y(92)
        ui_KHM_Label.set_align(lv.ALIGN.CENTER)
        ui_KHM_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_KHM_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_KHM_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_RPM = lv.label(self.screen)
        self.ui_RPM.set_text("7463")
        self.ui_RPM.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_RPM.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_RPM.set_x(0)
        self.ui_RPM.set_y(21)
        self.ui_RPM.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_RPM, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_RPM, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_RPM.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_RPM.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 24), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_SPEED = lv.label(self.screen)
        self.ui_SPEED.set_text("365")
        self.ui_SPEED.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_SPEED.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_SPEED.set_x(0)
        self.ui_SPEED.set_y(93)
        self.ui_SPEED.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_SPEED, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_SPEED, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.ui_SPEED.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_SPEED.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 24), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen_Container1 = lv.obj(self.screen)
        self.screen_Container1.remove_style_all()
        self.screen_Container1.set_width(52)
        self.screen_Container1.set_height(20)
        self.screen_Container1.set_x(0)
        self.screen_Container1.set_y(65)
        self.screen_Container1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.screen_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen_Container1, lv.obj.FLAG.SCROLLABLE, False)
        self.screen_Container1.set_style_bg_color(lv.color_hex(0xFF0101), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container1.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.screen_Label4 = lv.label(self.screen_Container1)
        self.screen_Label4.set_text("DRS")
        self.screen_Label4.set_width(lv.SIZE.CONTENT)  # 1
        self.screen_Label4.set_height(lv.SIZE.CONTENT)  # 1
        self.screen_Label4.set_align(lv.ALIGN.CENTER)
        self.screen_Label4.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label4.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Label4.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 18), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_TelemetryScreen_Txt = lv.label(self.screen)
        ui_TelemetryScreen_Txt.set_text("")
        ui_TelemetryScreen_Txt.set_width(lv.SIZE.CONTENT)  # 1
        ui_TelemetryScreen_Txt.set_height(lv.SIZE.CONTENT)  # 1
        ui_TelemetryScreen_Txt.set_x(0)
        ui_TelemetryScreen_Txt.set_y(-14)
        ui_TelemetryScreen_Txt.set_align(lv.ALIGN.CENTER)
        ui_TelemetryScreen_Txt.set_style_text_font(lv.font_load(f"Z:ui/fonts/ui_font_TelemetryTxt.bin"), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen.add_event_cb(self.TelemetryScreen_eventhandler, lv.EVENT.ALL, None)



    def TelemetryScreen_eventhandler(self,event_struct):
       event = event_struct.code
       if event == lv.EVENT.SCREEN_LOAD_START and True:
          self.bottom_Animation(self.ui_SPEED, 0)
          self.right_Animation(self.ui_RPM, 0)
          self.opa_on_Animation(self.ui_Gear, 0)
       return
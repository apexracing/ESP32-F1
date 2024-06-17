import lvgl as lv
from ui.screen import Screen
from ui.theme_manager import Themes

class RaceScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Weather_Image = lv.label(self.screen)
        self.ui_Weather_Image.set_text("")
        self.ui_Weather_Image.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Weather_Image.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Weather_Image.set_x(-85)
        self.ui_Weather_Image.set_y(-29)
        self.ui_Weather_Image.set_align(lv.ALIGN.CENTER)
        self.ui_Weather_Image.set_style_text_color(lv.color_hex(0xFFF100), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Weather_Image.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Weather_Image.set_style_text_font(self.resourceManager.load_font("IconE60F", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_TrackTempImg = lv.label(self.screen)
        self.ui_TrackTempImg.set_text("")
        self.ui_TrackTempImg.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_TrackTempImg.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_TrackTempImg.set_x(90)
        self.ui_TrackTempImg.set_y(-29)
        self.ui_TrackTempImg.set_align(lv.ALIGN.CENTER)
        self.ui_TrackTempImg.set_style_text_color(lv.color_hex(0xFF0101), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_TrackTempImg.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_TrackTempImg.set_style_text_font(self.resourceManager.load_font("IconE604", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_WindImg = lv.label(self.screen)
        self.ui_WindImg.set_text("")
        self.ui_WindImg.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_WindImg.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_WindImg.set_x(-17)
        self.ui_WindImg.set_y(77)
        self.ui_WindImg.set_align(lv.ALIGN.CENTER)
        self.ui_WindImg.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_WindImg.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_WindImg.set_style_text_font(self.resourceManager.load_font("IconE603", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_HumidnessImg = lv.label(self.screen)
        self.ui_HumidnessImg.set_text("")
        self.ui_HumidnessImg.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_HumidnessImg.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_HumidnessImg.set_x(-23)
        self.ui_HumidnessImg.set_y(-88)
        self.ui_HumidnessImg.set_align(lv.ALIGN.CENTER)
        self.ui_HumidnessImg.set_style_text_color(lv.color_hex(0x23ABD7), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_HumidnessImg.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_HumidnessImg.set_style_text_font(self.resourceManager.load_font("IconE602", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_PercetImg = lv.label(self.screen)
        ui_PercetImg.set_text("")
        ui_PercetImg.set_width(lv.SIZE.CONTENT)  # 1
        ui_PercetImg.set_height(lv.SIZE.CONTENT)  # 1
        ui_PercetImg.set_x(90)
        ui_PercetImg.set_y(30)
        ui_PercetImg.set_align(lv.ALIGN.CENTER)
        ui_PercetImg.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_PercetImg.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_PercetImg.set_style_text_font(self.resourceManager.load_font("IconE606", 18), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_PercetImg2 = lv.label(self.screen)
        ui_PercetImg2.set_text("")
        ui_PercetImg2.set_width(lv.SIZE.CONTENT)  # 1
        ui_PercetImg2.set_height(lv.SIZE.CONTENT)  # 1
        ui_PercetImg2.set_x(-85)
        ui_PercetImg2.set_y(30)
        ui_PercetImg2.set_align(lv.ALIGN.CENTER)
        ui_PercetImg2.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_PercetImg2.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_PercetImg2.set_style_text_font(self.resourceManager.load_font("IconE606", 18), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Air_Temp = lv.label(self.screen)
        self.ui_Air_Temp.set_text("32")
        self.ui_Air_Temp.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Air_Temp.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Air_Temp.set_x(-86)
        self.ui_Air_Temp.set_y(10)
        self.ui_Air_Temp.set_align(lv.ALIGN.CENTER)
        self.ui_Air_Temp.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Air_Temp.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Air_Temp.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 18), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Track_Temp = lv.label(self.screen)
        self.ui_Track_Temp.set_text("55")
        self.ui_Track_Temp.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Track_Temp.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Track_Temp.set_x(92)
        self.ui_Track_Temp.set_y(12)
        self.ui_Track_Temp.set_align(lv.ALIGN.CENTER)
        self.ui_Track_Temp.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Track_Temp.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Track_Temp.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 18), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_AirLabel = lv.label(self.screen)
        ui_AirLabel.set_text("Air")
        ui_AirLabel.set_width(lv.SIZE.CONTENT)  # 1
        ui_AirLabel.set_height(lv.SIZE.CONTENT)  # 1
        ui_AirLabel.set_x(-85)
        ui_AirLabel.set_y(-8)
        ui_AirLabel.set_align(lv.ALIGN.CENTER)
        ui_AirLabel.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_AirLabel.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_AirLabel.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 12), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_TrackLabel = lv.label(self.screen)
        ui_TrackLabel.set_text("Track")
        ui_TrackLabel.set_width(lv.SIZE.CONTENT)  # 1
        ui_TrackLabel.set_height(lv.SIZE.CONTENT)  # 1
        ui_TrackLabel.set_x(91)
        ui_TrackLabel.set_y(-6)
        ui_TrackLabel.set_align(lv.ALIGN.CENTER)
        ui_TrackLabel.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TrackLabel.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TrackLabel.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 12), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_WindLabel2 = lv.label(self.screen)
        ui_WindLabel2.set_text("m/s")
        ui_WindLabel2.set_width(lv.SIZE.CONTENT)  # 1
        ui_WindLabel2.set_height(lv.SIZE.CONTENT)  # 1
        ui_WindLabel2.set_x(17)
        ui_WindLabel2.set_y(93)
        ui_WindLabel2.set_align(lv.ALIGN.CENTER)
        ui_WindLabel2.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WindLabel2.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WindLabel2.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 12), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_WindLabel = lv.label(self.screen)
        ui_WindLabel.set_text("Wind")
        ui_WindLabel.set_width(lv.SIZE.CONTENT)  # 1
        ui_WindLabel.set_height(lv.SIZE.CONTENT)  # 1
        ui_WindLabel.set_x(-16)
        ui_WindLabel.set_y(93)
        ui_WindLabel.set_align(lv.ALIGN.CENTER)
        ui_WindLabel.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WindLabel.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_WindLabel.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 12), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Humidness = lv.label(self.screen)
        self.ui_Humidness.set_text("100")
        self.ui_Humidness.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Humidness.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Humidness.set_x(3)
        self.ui_Humidness.set_y(-88)
        self.ui_Humidness.set_align(lv.ALIGN.CENTER)
        self.ui_Humidness.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Humidness.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Humidness.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 18), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Wind = lv.label(self.screen)
        self.ui_Wind.set_text("2.3")
        self.ui_Wind.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Wind.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Wind.set_x(16)
        self.ui_Wind.set_y(77)
        self.ui_Wind.set_align(lv.ALIGN.CENTER)
        self.ui_Wind.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Wind.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Wind.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 18), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_HumidnessP = lv.label(self.screen)
        self.ui_HumidnessP.set_text("%")
        self.ui_HumidnessP.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_HumidnessP.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_HumidnessP.set_x(26)
        self.ui_HumidnessP.set_y(-89)
        self.ui_HumidnessP.set_align(lv.ALIGN.CENTER)
        self.ui_HumidnessP.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_HumidnessP.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_HumidnessP.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 18), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_AirTempArc = lv.arc(self.screen)
        self.ui_AirTempArc.set_width(230)
        self.ui_AirTempArc.set_height(230)
        self.ui_AirTempArc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.EVENT_BUBBLE, True)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(self.ui_AirTempArc, lv.obj.FLAG.SCROLL_CHAIN, False)
        self.ui_AirTempArc.set_range(0, 42)
        self.ui_AirTempArc.set_value(32)
        self.ui_AirTempArc.set_bg_angles(155, 205)
        self.ui_AirTempArc.set_style_arc_width(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_AirTempArc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_AirTempArc.set_style_arc_width(3, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_AirTempArc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_AirTempArc.set_style_arc_img_src(self.resourceManager.load_img("/ui/assets/d.png"), lv.PART.INDICATOR | lv.STATE.DEFAULT)
    
        self.ui_AirTempArc.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_AirTempArc.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
    
        self.ui_TrackTempArc = lv.arc(self.screen)
        self.ui_TrackTempArc.set_width(230)
        self.ui_TrackTempArc.set_height(230)
        self.ui_TrackTempArc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_TrackTempArc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_TrackTempArc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_TrackTempArc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_TrackTempArc, lv.obj.FLAG.EVENT_BUBBLE, True)
        self.SetFlag(self.ui_TrackTempArc, lv.obj.FLAG.SNAPPABLE, False)
        self.ui_TrackTempArc.set_range(0, 60)
        self.ui_TrackTempArc.set_value(55)
        self.ui_TrackTempArc.set_bg_angles(155, 205)
        self.ui_TrackTempArc.set_mode(self.ui_TrackTempArc.MODE.REVERSE)
        self.ui_TrackTempArc.set_rotation(180)
        self.ui_TrackTempArc.set_style_arc_width(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_TrackTempArc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_TrackTempArc.set_style_arc_width(3, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_TrackTempArc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_TrackTempArc.set_style_arc_img_src(self.resourceManager.load_img("/ui/assets/d.png"), lv.PART.INDICATOR | lv.STATE.DEFAULT)
    
        self.ui_TrackTempArc.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_TrackTempArc.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
    
        self.ui_HumidnessArc = lv.arc(self.screen)
        self.ui_HumidnessArc.set_width(230)
        self.ui_HumidnessArc.set_height(230)
        self.ui_HumidnessArc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_HumidnessArc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_HumidnessArc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_HumidnessArc, lv.obj.FLAG.EVENT_BUBBLE, True)
        self.SetFlag(self.ui_HumidnessArc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_HumidnessArc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_HumidnessArc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.ui_HumidnessArc.set_value(50)
        self.ui_HumidnessArc.set_bg_angles(140, 220)
        self.ui_HumidnessArc.set_rotation(90)
        self.ui_HumidnessArc.set_style_arc_width(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_HumidnessArc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.themeManager.ui_object_set_themeable_style_property(self.ui_HumidnessArc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_HumidnessArc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_HumidnessArc.set_style_arc_width(3, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_HumidnessArc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
    
        self.ui_HumidnessArc.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_HumidnessArc.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
    
        self.ui_WindArc = lv.arc(self.screen)
        self.ui_WindArc.set_width(230)
        self.ui_WindArc.set_height(230)
        self.ui_WindArc.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.EVENT_BUBBLE, True)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(self.ui_WindArc, lv.obj.FLAG.SCROLL_CHAIN, False)
        self.ui_WindArc.set_range(0, 50)
        self.ui_WindArc.set_value(30)
        self.ui_WindArc.set_bg_angles(140, 220)
        self.ui_WindArc.set_mode(self.ui_WindArc.MODE.REVERSE)
        self.ui_WindArc.set_rotation(270)
        self.ui_WindArc.set_style_arc_width(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_WindArc.set_style_arc_rounded(False, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.themeManager.ui_object_set_themeable_style_property(self.ui_WindArc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_WindArc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_WindArc.set_style_arc_width(3, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_WindArc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)
    
        self.ui_WindArc.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_WindArc.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
        self.ui_Flag_Container = lv.obj(self.screen)
        self.ui_Flag_Container.remove_style_all()
        self.ui_Flag_Container.set_width(127)
        self.ui_Flag_Container.set_height(4)
        self.ui_Flag_Container.set_x(55)
        self.ui_Flag_Container.set_y(53)
        self.SetFlag(self.ui_Flag_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Flag_Container, lv.obj.FLAG.SCROLLABLE, False)
    
        self.screen_Container1 = lv.obj(self.ui_Flag_Container)
        self.screen_Container1.remove_style_all()
        self.screen_Container1.set_width(4)
        self.screen_Container1.set_height(4)
        self.SetFlag(self.screen_Container1, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen_Container1, lv.obj.FLAG.SCROLLABLE, False)
        self.screen_Container1.set_style_bg_color(lv.color_hex(0xFF0101), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container1.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Red_Flag = lv.obj(self.ui_Flag_Container)
        self.ui_Red_Flag.remove_style_all()
        self.ui_Red_Flag.set_width(34)
        self.ui_Red_Flag.set_height(4)
        self.ui_Red_Flag.set_x(6)
        self.ui_Red_Flag.set_y(0)
        self.SetFlag(self.ui_Red_Flag, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Red_Flag, lv.obj.FLAG.SCROLLABLE, False)
        self.ui_Red_Flag.set_style_bg_color(lv.color_hex(0x3D3D3D), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Red_Flag.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.screen_Container4 = lv.obj(self.ui_Flag_Container)
        self.screen_Container4.remove_style_all()
        self.screen_Container4.set_width(4)
        self.screen_Container4.set_height(4)
        self.screen_Container4.set_x(42)
        self.screen_Container4.set_y(0)
        self.SetFlag(self.screen_Container4, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen_Container4, lv.obj.FLAG.SCROLLABLE, False)
        self.screen_Container4.set_style_bg_color(lv.color_hex(0x00FD3B), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container4.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Green_Flag = lv.obj(self.ui_Flag_Container)
        self.ui_Green_Flag.remove_style_all()
        self.ui_Green_Flag.set_width(34)
        self.ui_Green_Flag.set_height(4)
        self.ui_Green_Flag.set_x(48)
        self.ui_Green_Flag.set_y(0)
        self.SetFlag(self.ui_Green_Flag, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Green_Flag, lv.obj.FLAG.SCROLLABLE, False)
        self.ui_Green_Flag.set_style_bg_color(lv.color_hex(0x00FD3B), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Green_Flag.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.screen_Container7 = lv.obj(self.ui_Flag_Container)
        self.screen_Container7.remove_style_all()
        self.screen_Container7.set_width(4)
        self.screen_Container7.set_height(4)
        self.screen_Container7.set_x(87)
        self.screen_Container7.set_y(0)
        self.SetFlag(self.screen_Container7, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen_Container7, lv.obj.FLAG.SCROLLABLE, False)
        self.screen_Container7.set_style_bg_color(lv.color_hex(0xFFDD00), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container7.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Yellow_FLag = lv.obj(self.ui_Flag_Container)
        self.ui_Yellow_FLag.remove_style_all()
        self.ui_Yellow_FLag.set_width(34)
        self.ui_Yellow_FLag.set_height(4)
        self.ui_Yellow_FLag.set_x(92)
        self.ui_Yellow_FLag.set_y(0)
        self.SetFlag(self.ui_Yellow_FLag, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Yellow_FLag, lv.obj.FLAG.SCROLLABLE, False)
        self.ui_Yellow_FLag.set_style_bg_color(lv.color_hex(0xFFDD00), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Yellow_FLag.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_Page_Container = lv.obj(self.screen)
        ui_Page_Container.remove_style_all()
        ui_Page_Container.set_width(35)
        ui_Page_Container.set_height(10)
        ui_Page_Container.set_x(1)
        ui_Page_Container.set_y(56)
        ui_Page_Container.set_align(lv.ALIGN.CENTER)
        ui_Page_Container.set_flex_flow(lv.FLEX_FLOW.ROW)
        ui_Page_Container.set_flex_align(lv.FLEX_ALIGN.SPACE_BETWEEN, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.SPACE_BETWEEN)
        self.SetFlag(ui_Page_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_Page_Container, lv.obj.FLAG.SCROLLABLE, False)
    
        ui_Page1 = lv.btn(ui_Page_Container)
        ui_Page1.set_width(4)
        ui_Page1.set_height(4)
        ui_Page1.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_Page1, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(ui_Page1, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
        self.themeManager.ui_object_set_themeable_style_property(ui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.BG_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(ui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.BG_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(ui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.SHADOW_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(ui_Page1, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.SHADOW_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        ui_Page1.set_style_shadow_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Page1.set_style_shadow_spread(1, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_Page2 = lv.btn(ui_Page_Container)
        ui_Page2.set_width(4)
        ui_Page2.set_height(4)
        ui_Page2.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_Page2, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(ui_Page2, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
        ui_Page2.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Page2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_Page3 = lv.btn(ui_Page_Container)
        ui_Page3.set_width(4)
        ui_Page3.set_height(4)
        ui_Page3.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_Page3, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(ui_Page3, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
        ui_Page3.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Page3.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_Page4 = lv.btn(ui_Page_Container)
        ui_Page4.set_width(4)
        ui_Page4.set_height(4)
        ui_Page4.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_Page4, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(ui_Page4, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
        ui_Page4.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Page4.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.ui_Driver_Container = lv.obj(self.screen)
        self.ui_Driver_Container.remove_style_all()
        self.ui_Driver_Container.set_width(140)
        self.ui_Driver_Container.set_height(100)
        self.ui_Driver_Container.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_Driver_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Driver_Container, lv.obj.FLAG.SCROLLABLE, False)
    
        self.ui_d1 = self.ui_DriverContainer_create(self.ui_Driver_Container)
        self.ui_d1.set_x(0)
        self.ui_d1.set_y(-39)
    
        self.ui_d2 = self.ui_DriverContainer_create(self.ui_Driver_Container)
        self.ui_d2.set_x(0)
        self.ui_d2.set_y(-20)
    
        self.ui_d3 = self.ui_DriverContainer_create(self.ui_Driver_Container)
        self.ui_d3.set_x(0)
        self.ui_d3.set_y(0)
    
        self.ui_d4 = self.ui_DriverContainer_create(self.ui_Driver_Container)
        self.ui_d4.set_x(0)
        self.ui_d4.set_y(20)
    
        self.ui_d5 = self.ui_DriverContainer_create(self.ui_Driver_Container)
        self.ui_d5.set_x(0)
        self.ui_d5.set_y(39)
    
        self.ui_ControllCenter_Container = lv.obj(self.screen)
        self.ui_ControllCenter_Container.remove_style_all()
        self.ui_ControllCenter_Container.set_width(225)
        self.ui_ControllCenter_Container.set_height(22)
        self.ui_ControllCenter_Container.set_x(-3)
        self.ui_ControllCenter_Container.set_y(74)
        self.ui_ControllCenter_Container.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_ControllCenter_Container, lv.obj.FLAG.HIDDEN, True)
        self.SetFlag(self.ui_ControllCenter_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_ControllCenter_Container, lv.obj.FLAG.SCROLLABLE, False)
        self.ui_ControllCenter_Container.set_style_bg_color(lv.color_hex(0xFF0101), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_ControllCenter_Container.set_style_bg_opa(200, lv.PART.MAIN | lv.STATE.DEFAULT)
    
        ui_CenterMsg = lv.label(self.ui_ControllCenter_Container)
        ui_CenterMsg.set_text("BLACK AND WHITE FLAG FOR CAR 1 (VER) - TRACK LIMITS")
        ui_CenterMsg.set_width(lv.SIZE.CONTENT)  # 1
        ui_CenterMsg.set_height(lv.SIZE.CONTENT)  # 1
        ui_CenterMsg.set_align(lv.ALIGN.CENTER)
        ui_CenterMsg.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_CenterMsg.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_CenterMsg.set_style_text_font(self.resourceManager.load_font("F1R", 10), lv.PART.MAIN | lv.STATE.DEFAULT)
    
        self.screen.add_event_cb(self.RaceScreen_eventhandler, lv.EVENT.ALL, None)
    def RaceScreen_eventhandler(self,event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOADED and True:
            self.opa_on_Animation(self.ui_WindImg, 0)
            self.opa_on_Animation(self.ui_TrackTempImg, 0)
            self.opa_on_Animation(self.ui_Weather_Image, 0)
            self.opa_on_Animation(self.ui_HumidnessImg, 0)
            self.left_Animation(self.ui_Air_Temp, 0)
            self.right_Animation(self.ui_Track_Temp, 0)
            self.top_Animation(self.ui_Humidness, 0)
            self.bottom_Animation(self.ui_Wind, 0)
            self.opa_on_Animation(self.ui_Flag_Container, 0)
            self.opa_on_Animation(self.ui_AirTempArc, 0)
            self.opa_on_Animation(self.ui_TrackTempArc, 0)
            self.opa_on_Animation(self.ui_HumidnessArc, 0)
            self.opa_on_Animation(self.ui_WindArc, 0)
            self.driver_left_Animation(self.ui_d1, 0)
            self.driver_left_Animation(self.ui_d2, 50)
            self.driver_left_Animation(self.ui_d3, 100)
            self.driver_left_Animation(self.ui_d4, 150)
            self.driver_left_Animation(self.ui_d5, 200)
        return

    def ui_DriverContainer_create(self,comp_parent):
        cui_DriverContainer = lv.obj(comp_parent)
        cui_DriverContainer.remove_style_all()
        cui_DriverContainer.set_width(131)
        cui_DriverContainer.set_height(16)
        cui_DriverContainer.set_x(0)
        cui_DriverContainer.set_y(-39)
        cui_DriverContainer.set_align(lv.ALIGN.CENTER)
        self.SetFlag(cui_DriverContainer, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(cui_DriverContainer, lv.obj.FLAG.SCROLLABLE, False)
        cui_RaceScreen_Label1 = lv.label(cui_DriverContainer)
        cui_RaceScreen_Label1.set_text("22")
        cui_RaceScreen_Label1.set_width(16)
        cui_RaceScreen_Label1.set_height(16)
        cui_RaceScreen_Label1.set_x(5)
        cui_RaceScreen_Label1.set_y(0)
        cui_RaceScreen_Label1.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label1.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label1.set_style_text_align(lv.TEXT_ALIGN.RIGHT, lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label1.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 14), lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Container3 = lv.obj(cui_DriverContainer)
        cui_RaceScreen_Container3.remove_style_all()
        cui_RaceScreen_Container3.set_width(3)
        cui_RaceScreen_Container3.set_height(14)
        cui_RaceScreen_Container3.set_x(25)
        cui_RaceScreen_Container3.set_y(0)
        self.SetFlag(cui_RaceScreen_Container3, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(cui_RaceScreen_Container3, lv.obj.FLAG.SCROLLABLE, False)
        cui_RaceScreen_Container3.set_style_bg_color(lv.color_hex(0x3671C6), lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Container3.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label3 = lv.label(cui_DriverContainer)
        cui_RaceScreen_Label3.set_text("VER")
        cui_RaceScreen_Label3.set_width(lv.SIZE.CONTENT)  # 1
        cui_RaceScreen_Label3.set_height(lv.SIZE.CONTENT)  # 1
        cui_RaceScreen_Label3.set_x(33)
        cui_RaceScreen_Label3.set_y(0)
        cui_RaceScreen_Label3.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label3.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label3.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 14), lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label4 = lv.label(cui_DriverContainer)
        cui_RaceScreen_Label4.set_text("Interval")
        cui_RaceScreen_Label4.set_width(60)
        cui_RaceScreen_Label4.set_height(16)
        cui_RaceScreen_Label4.set_x(70)
        cui_RaceScreen_Label4.set_y(0)
        cui_RaceScreen_Label4.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label4.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label4.set_style_text_align(lv.TEXT_ALIGN.RIGHT, lv.PART.MAIN | lv.STATE.DEFAULT)
        cui_RaceScreen_Label4.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 14), lv.PART.MAIN | lv.STATE.DEFAULT)
        self._ui_comp_table[id(cui_DriverContainer)] = {"DriverContainer": cui_DriverContainer,
                                                   "RaceScreen_Label1": cui_RaceScreen_Label1,
                                                   "RaceScreen_Container3": cui_RaceScreen_Container3,
                                                   "RaceScreen_Label3": cui_RaceScreen_Label3,
                                                   "RaceScreen_Label4": cui_RaceScreen_Label4,
                                                   "_CompName": "DriverContainer"}
        return cui_DriverContainer

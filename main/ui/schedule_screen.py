from ui.screen import Screen
import lvgl as lv
from ui.theme_manager import  Themes,ThemeManager

class ScheduleScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_img_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Second_Arc = lv.arc(self.screen)
        self.ui_Second_Arc.set_width(230)
        self.ui_Second_Arc.set_height(230)
        self.ui_Second_Arc.set_align(lv.ALIGN.CENTER)
        self.ui_Second_Arc.set_range(0, 60)
        self.ui_Second_Arc.set_value(45)
        self.ui_Second_Arc.set_bg_angles(0, 360)
        self.ui_Second_Arc.set_rotation(-90)
        self.ui_Second_Arc.set_style_arc_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Second_Arc.set_style_arc_opa(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Second_Arc.set_style_arc_width(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.GESTURE_BUBBLE, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(self.ui_Second_Arc, lv.obj.FLAG.SCROLL_CHAIN, False)

        self.themeManager.ui_object_set_themeable_style_property(self.ui_Second_Arc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Second_Arc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_Second_Arc.set_style_arc_width(2, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Second_Arc.set_style_arc_rounded(True, lv.PART.INDICATOR | lv.STATE.DEFAULT)

        self.ui_Second_Arc.set_style_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)

        self.ui_Upcoming_Label = lv.label(self.screen)
        self.ui_Upcoming_Label.set_text("Upcoming")
        self.ui_Upcoming_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Upcoming_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Upcoming_Label.set_x(0)
        self.ui_Upcoming_Label.set_y(20)
        self.ui_Upcoming_Label.set_align(lv.ALIGN.TOP_MID)
        self.ui_Upcoming_Label.set_style_text_color(lv.color_hex(0x8D8D8D), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Upcoming_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Upcoming_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYB",14), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_Gmt_Label = lv.label(self.screen)
        ui_Gmt_Label.set_text("UTC/GMT +8")
        ui_Gmt_Label.set_width(lv.SIZE.CONTENT)  # 1
        ui_Gmt_Label.set_height(lv.SIZE.CONTENT)  # 1
        ui_Gmt_Label.set_x(0)
        ui_Gmt_Label.set_y(-80)
        ui_Gmt_Label.set_align(lv.ALIGN.BOTTOM_MID)
        ui_Gmt_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_letter_space(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_line_space(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM",10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Session_Label = lv.label(self.screen)
        self.ui_Session_Label.set_text("Canadian Grand Prix")
        self.ui_Session_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Session_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Session_Label.set_x(0)
        self.ui_Session_Label.set_y(51)
        self.ui_Session_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Session_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Session_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_Session_Label.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Session_Label.set_style_text_font(self.resourceManager.load_font("F1R",12), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Event_Label = lv.label(self.screen)
        self.ui_Event_Label.set_text("Practice 1")
        self.ui_Event_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Event_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Event_Label.set_x(0)
        self.ui_Event_Label.set_y(79)
        self.ui_Event_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Event_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Event_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.ui_Event_Label.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Event_Label.set_style_text_font(self.resourceManager.load_font("F1R",14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Days = lv.label(self.screen)
        self.ui_Days.set_text("5")
        self.ui_Days.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Days.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Days.set_x(18)
        self.ui_Days.set_y(95)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Days, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Days, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Days.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days.set_style_text_font(self.resourceManager.load_font("DISPLAYM",14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Hours = lv.label(self.screen)
        self.ui_Hours.set_text("22")
        self.ui_Hours.set_width(22)
        self.ui_Hours.set_height(10)
        self.ui_Hours.set_x(18)
        self.ui_Hours.set_y(121)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Hours, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Hours, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.ui_Hours.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours.set_style_text_font(self.resourceManager.load_font("DISPLAYM",14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Minutes = lv.label(self.screen)
        self.ui_Minutes.set_text("13")
        self.ui_Minutes.set_width(22)
        self.ui_Minutes.set_height(10)
        self.ui_Minutes.set_x(18)
        self.ui_Minutes.set_y(146)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Minutes, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Minutes, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA,
                                               Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_Minutes.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes.set_style_text_font(self.resourceManager.load_font("DISPLAYM",14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Days_Label = lv.label(self.screen)
        self.ui_Days_Label.set_text("Days")
        self.ui_Days_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Days_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Days_Label.set_x(18)
        self.ui_Days_Label.set_y(83)
        self.ui_Days_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM",10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Hours_Label = lv.label(self.screen)
        self.ui_Hours_Label.set_text("Hours")
        self.ui_Hours_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Hours_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Hours_Label.set_x(18)
        self.ui_Hours_Label.set_y(109)
        self.ui_Hours_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM",10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Minutes_Label = lv.label(self.screen)
        self.ui_Minutes_Label.set_text("Mins")
        self.ui_Minutes_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Minutes_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Minutes_Label.set_x(19)
        self.ui_Minutes_Label.set_y(135)
        self.ui_Minutes_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM",10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen_Container2 = lv.obj(self.screen)
        self.screen_Container2.remove_style_all()
        self.screen_Container2.set_width(40)
        self.screen_Container2.set_height(40)
        self.screen_Container2.set_x(-27)
        self.screen_Container2.set_y(-53)
        self.screen_Container2.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.screen_Container2, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen_Container2, lv.obj.FLAG.SCROLLABLE, False)
        self.screen_Container2.set_style_radius(10, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container2.set_style_bg_color(lv.color_hex(0x1A1A1A), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Calendar_Month = lv.label(self.screen_Container2)
        self.ui_Calendar_Month.set_text("05")
        self.ui_Calendar_Month.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Month.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Month.set_align(lv.ALIGN.CENTER)
        self.ui_Calendar_Month.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Month.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Month.set_style_text_font(self.resourceManager.load_font("DISPLAYR",30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen_Container3 = lv.obj(self.screen)
        self.screen_Container3.remove_style_all()
        self.screen_Container3.set_width(40)
        self.screen_Container3.set_height(40)
        self.screen_Container3.set_x(34)
        self.screen_Container3.set_y(-53)
        self.screen_Container3.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.screen_Container3, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.screen_Container3, lv.obj.FLAG.SCROLLABLE, False)
        self.screen_Container3.set_style_radius(10, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container3.set_style_bg_color(lv.color_hex(0x1A1A1A), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen_Container3.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Calendar_Day = lv.label(self.screen_Container3)
        self.ui_Calendar_Day.set_text("28")
        self.ui_Calendar_Day.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Day.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Day.set_align(lv.ALIGN.CENTER)
        self.ui_Calendar_Day.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Day.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Day.set_style_text_font(self.resourceManager.load_font("DISPLAYR",30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Dot_Label = lv.label(self.screen)
        self.ui_Time_Dot_Label.set_text(":")
        self.ui_Time_Dot_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Dot_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Dot_Label.set_x(-1)
        self.ui_Time_Dot_Label.set_y(4)
        self.ui_Time_Dot_Label.set_align(lv.ALIGN.CENTER)
        self.ui_Time_Dot_Label.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Dot_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Dot_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYR",60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Min_Label = lv.label(self.screen)
        self.ui_Time_Min_Label.set_text("14")
        self.ui_Time_Min_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Min_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Min_Label.set_x(35)
        self.ui_Time_Min_Label.set_y(3)
        self.ui_Time_Min_Label.set_align(lv.ALIGN.CENTER)
        self.ui_Time_Min_Label.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Min_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Min_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYR",60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Hour_Label = lv.label(self.screen)
        self.ui_Time_Hour_Label.set_text("10")
        self.ui_Time_Hour_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Hour_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Hour_Label.set_x(-40)
        self.ui_Time_Hour_Label.set_y(3)
        self.ui_Time_Hour_Label.set_align(lv.ALIGN.CENTER)
        self.ui_Time_Hour_Label.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Hour_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Hour_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYR",60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen.add_event_cb(self.ScheduleScreen_eventhandler, lv.EVENT.ALL, None)

    def ScheduleScreen_eventhandler(self,event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOADED and True:
            self.top_Animation(self.ui_Calendar_Month, 0)
            self.top_Animation(self.ui_Calendar_Day, 0)
            self.left_Animation(self.ui_Time_Hour_Label, 0)
            self.right_Animation(self.ui_Time_Min_Label, 0)
            self.opa_on_Animation(self.ui_Days, 0)
            self.opa_on_Animation(self.ui_Hours, 0)
            self.opa_on_Animation(self.ui_Minutes, 0)
            self.opa_on_Animation(self.ui_Session_Label, 0)
            self.bottom_Animation(self.ui_Event_Label, 0)
            self.opa_on_Animation(self.ui_Time_Dot_Label, 0)
            self.top_Animation(self.ui_Upcoming_Label, 0)

        return


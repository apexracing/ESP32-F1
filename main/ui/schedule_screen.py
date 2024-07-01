from ui.screen import Screen
import lvgl as lv
from ui.theme_manager import Themes, ThemeManager
from common.time_driver import TimeDriver
from common.f1_api import F1Api
import time
import math
SEC_STEP = const(25)


def calculate_time_difference(start_time, end_time):
    # 计算总秒数差
    total_seconds = end_time - start_time
    # 计算天数
    days = total_seconds // (24 * 3600)
    total_seconds %= (24 * 3600)

    # 计算小时
    hours = total_seconds // 3600
    total_seconds %= 3600
    # 计算分钟
    minutes = total_seconds//60
    seconds=total_seconds%60
    if seconds>0:
        minutes+=1

    return days, hours, minutes


class ScheduleScreen(Screen):
    def __init__(self):
        super().__init__()
        self.f1 = F1Api()
        self.f1_event = self.f1.get_eventing()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_img_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Second_Arc = lv.arc(self.screen)
        self.ui_Second_Arc.set_width(230)
        self.ui_Second_Arc.set_height(230)
        self.ui_Second_Arc.set_align(lv.ALIGN.CENTER)
        self.ui_Second_Arc.set_range(0, 29999)
        self.ui_Second_Arc.set_value(0)
        self.ui_Second_Arc.set_bg_angles(0, 360)
        self.ui_Second_Arc.set_rotation(270)
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

        self.themeManager.ui_object_set_themeable_style_property(self.ui_Second_Arc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_COLOR, Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Second_Arc, lv.PART.INDICATOR | lv.STATE.DEFAULT, lv.STYLE.ARC_OPA, Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_Second_Arc.set_style_arc_width(2, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        self.ui_Second_Arc.set_style_arc_rounded(False, lv.PART.INDICATOR | lv.STATE.DEFAULT)

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
        self.ui_Upcoming_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYB", 14), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_Gmt_Label = lv.label(self.screen)
        ui_Gmt_Label.set_text(f"UTC/GMT {self.timeDriver.get_time_zone()}")
        ui_Gmt_Label.set_width(lv.SIZE.CONTENT)  # 1
        ui_Gmt_Label.set_height(lv.SIZE.CONTENT)  # 1
        ui_Gmt_Label.set_x(0)
        ui_Gmt_Label.set_y(-80)
        ui_Gmt_Label.set_align(lv.ALIGN.BOTTOM_MID)
        ui_Gmt_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_letter_space(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_line_space(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_Gmt_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Event_Name_Label = lv.label(self.screen)
        self.ui_Event_Name_Label.set_text("")
        self.ui_Event_Name_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Event_Name_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Event_Name_Label.set_x(0)
        self.ui_Event_Name_Label.set_y(51)
        self.ui_Event_Name_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Event_Name_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Event_Name_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_Event_Name_Label.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Event_Name_Label.set_style_text_font(self.resourceManager.load_font("F1R", 12), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Session_Name_Label = lv.label(self.screen)
        self.ui_Session_Name_Label.set_text("")
        self.ui_Session_Name_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Session_Name_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Session_Name_Label.set_x(0)
        self.ui_Session_Name_Label.set_y(79)
        self.ui_Session_Name_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Session_Name_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Session_Name_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.ui_Session_Name_Label.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Session_Name_Label.set_style_text_font(self.resourceManager.load_font("F1R", 14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Days = lv.label(self.screen)
        self.ui_Days.set_text("0")
        self.ui_Days.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Days.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Days.set_x(18)
        self.ui_Days.set_y(95)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Days, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Days, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Days.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Hours = lv.label(self.screen)
        self.ui_Hours.set_text("0")
        self.ui_Hours.set_width(22)
        self.ui_Hours.set_height(10)
        self.ui_Hours.set_x(18)
        self.ui_Hours.set_y(121)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Hours, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Hours, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.ui_Hours.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Minutes = lv.label(self.screen)
        self.ui_Minutes.set_text("0")
        self.ui_Minutes.set_width(22)
        self.ui_Minutes.set_height(10)
        self.ui_Minutes.set_x(18)
        self.ui_Minutes.set_y(146)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Minutes, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Minutes, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAMTHREE)
        self.ui_Minutes.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 14), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Days_Label = lv.label(self.screen)
        self.ui_Days_Label.set_text("Days")
        self.ui_Days_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Days_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Days_Label.set_x(18)
        self.ui_Days_Label.set_y(83)
        self.ui_Days_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Days_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Hours_Label = lv.label(self.screen)
        self.ui_Hours_Label.set_text("Hours")
        self.ui_Hours_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Hours_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Hours_Label.set_x(18)
        self.ui_Hours_Label.set_y(109)
        self.ui_Hours_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Hours_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Minutes_Label = lv.label(self.screen)
        self.ui_Minutes_Label.set_text("Mins")
        self.ui_Minutes_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Minutes_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Minutes_Label.set_x(19)
        self.ui_Minutes_Label.set_y(135)
        self.ui_Minutes_Label.set_style_text_color(lv.color_hex(0x9E9E9E), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Minutes_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYM", 10), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_TimeContinerNow = lv.obj(self.screen)
        self.ui_TimeContinerNow.remove_style_all()
        self.ui_TimeContinerNow.set_width(240)
        self.ui_TimeContinerNow.set_height(240)
        self.ui_TimeContinerNow.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_TimeContinerNow, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_TimeContinerNow, lv.obj.FLAG.SCROLLABLE, False)

        ui_ScheduleScreen_Container4 = lv.obj(self.ui_TimeContinerNow)
        ui_ScheduleScreen_Container4.remove_style_all()
        ui_ScheduleScreen_Container4.set_width(40)
        ui_ScheduleScreen_Container4.set_height(40)
        ui_ScheduleScreen_Container4.set_x(-27)
        ui_ScheduleScreen_Container4.set_y(-53)
        ui_ScheduleScreen_Container4.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_ScheduleScreen_Container4, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_ScheduleScreen_Container4, lv.obj.FLAG.SCROLLABLE, False)
        ui_ScheduleScreen_Container4.set_style_radius(10, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container4.set_style_bg_color(lv.color_hex(0x1A1A1A), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container4.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Calendar_Month_Now = lv.label(ui_ScheduleScreen_Container4)
        self.ui_Calendar_Month_Now.set_text("05")
        self.ui_Calendar_Month_Now.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Month_Now.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Month_Now.set_align(lv.ALIGN.CENTER)
        self.ui_Calendar_Month_Now.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Month_Now.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Month_Now.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_ScheduleScreen_Container5 = lv.obj(self.ui_TimeContinerNow)
        ui_ScheduleScreen_Container5.remove_style_all()
        ui_ScheduleScreen_Container5.set_width(40)
        ui_ScheduleScreen_Container5.set_height(40)
        ui_ScheduleScreen_Container5.set_x(34)
        ui_ScheduleScreen_Container5.set_y(-53)
        ui_ScheduleScreen_Container5.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_ScheduleScreen_Container5, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_ScheduleScreen_Container5, lv.obj.FLAG.SCROLLABLE, False)
        ui_ScheduleScreen_Container5.set_style_radius(10, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container5.set_style_bg_color(lv.color_hex(0x1A1A1A), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container5.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Calendar_Day_Now = lv.label(ui_ScheduleScreen_Container5)
        self.ui_Calendar_Day_Now.set_text("0")
        self.ui_Calendar_Day_Now.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Day_Now.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Day_Now.set_align(lv.ALIGN.CENTER)
        self.ui_Calendar_Day_Now.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Day_Now.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Calendar_Day_Now.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Dot_Label_Now = lv.label(self.ui_TimeContinerNow)
        self.ui_Time_Dot_Label_Now.set_text(":")
        self.ui_Time_Dot_Label_Now.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Dot_Label_Now.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Dot_Label_Now.set_x(-2)
        self.ui_Time_Dot_Label_Now.set_y(4)
        self.ui_Time_Dot_Label_Now.set_align(lv.ALIGN.CENTER)
        self.ui_Time_Dot_Label_Now.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Dot_Label_Now.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Dot_Label_Now.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Min_Label_Now = lv.label(self.ui_TimeContinerNow)
        self.ui_Time_Min_Label_Now.set_text("0")
        self.ui_Time_Min_Label_Now.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Min_Label_Now.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Min_Label_Now.set_x(44)
        self.ui_Time_Min_Label_Now.set_y(3)
        self.ui_Time_Min_Label_Now.set_align(lv.ALIGN.CENTER)
        self.ui_Time_Min_Label_Now.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Min_Label_Now.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Min_Label_Now.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Hour_Label_Now = lv.label(self.ui_TimeContinerNow)
        self.ui_Time_Hour_Label_Now.set_text("0")
        self.ui_Time_Hour_Label_Now.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Hour_Label_Now.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Hour_Label_Now.set_x(-40)
        self.ui_Time_Hour_Label_Now.set_y(3)
        self.ui_Time_Hour_Label_Now.set_align(lv.ALIGN.CENTER)
        self.ui_Time_Hour_Label_Now.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Hour_Label_Now.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Time_Hour_Label_Now.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_TimeContinerTarget = lv.obj(self.screen)
        self.ui_TimeContinerTarget.remove_style_all()
        self.ui_TimeContinerTarget.set_width(240)
        self.ui_TimeContinerTarget.set_height(240)
        self.ui_TimeContinerTarget.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_TimeContinerTarget, lv.obj.FLAG.HIDDEN, True)
        self.SetFlag(self.ui_TimeContinerTarget, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_TimeContinerTarget, lv.obj.FLAG.SCROLLABLE, False)

        ui_ScheduleScreen_Container2 = lv.obj(self.ui_TimeContinerTarget)
        ui_ScheduleScreen_Container2.remove_style_all()
        ui_ScheduleScreen_Container2.set_width(40)
        ui_ScheduleScreen_Container2.set_height(40)
        ui_ScheduleScreen_Container2.set_x(-27)
        ui_ScheduleScreen_Container2.set_y(-53)
        ui_ScheduleScreen_Container2.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_ScheduleScreen_Container2, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_ScheduleScreen_Container2, lv.obj.FLAG.SCROLLABLE, False)
        ui_ScheduleScreen_Container2.set_style_radius(10, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container2.set_style_bg_color(lv.color_hex(0x1A1A1A), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container2.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Calendar_Month = lv.label(ui_ScheduleScreen_Container2)
        self.ui_Calendar_Month.set_text("0")
        self.ui_Calendar_Month.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Month.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Month.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Calendar_Month, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Calendar_Month, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Calendar_Month.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_ScheduleScreen_Container3 = lv.obj(self.ui_TimeContinerTarget)
        ui_ScheduleScreen_Container3.remove_style_all()
        ui_ScheduleScreen_Container3.set_width(40)
        ui_ScheduleScreen_Container3.set_height(40)
        ui_ScheduleScreen_Container3.set_x(34)
        ui_ScheduleScreen_Container3.set_y(-53)
        ui_ScheduleScreen_Container3.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_ScheduleScreen_Container3, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_ScheduleScreen_Container3, lv.obj.FLAG.SCROLLABLE, False)
        ui_ScheduleScreen_Container3.set_style_radius(10, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container3.set_style_bg_color(lv.color_hex(0x1A1A1A), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_ScheduleScreen_Container3.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Calendar_Day = lv.label(ui_ScheduleScreen_Container3)
        self.ui_Calendar_Day.set_text("0")
        self.ui_Calendar_Day.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Day.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Calendar_Day.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Calendar_Day, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Calendar_Day, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Calendar_Day.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 30), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Dot_Label = lv.label(self.ui_TimeContinerTarget)
        self.ui_Time_Dot_Label.set_text(":")
        self.ui_Time_Dot_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Dot_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Dot_Label.set_x(-2)
        self.ui_Time_Dot_Label.set_y(4)
        self.ui_Time_Dot_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Time_Dot_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Time_Dot_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Time_Dot_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Min_Label = lv.label(self.ui_TimeContinerTarget)
        self.ui_Time_Min_Label.set_text("0")
        self.ui_Time_Min_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Min_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Min_Label.set_x(44)
        self.ui_Time_Min_Label.set_y(3)
        self.ui_Time_Min_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Time_Min_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Time_Min_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Time_Min_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Time_Hour_Label = lv.label(self.ui_TimeContinerTarget)
        self.ui_Time_Hour_Label.set_text("0")
        self.ui_Time_Hour_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Hour_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Time_Hour_Label.set_x(-40)
        self.ui_Time_Hour_Label.set_y(3)
        self.ui_Time_Hour_Label.set_align(lv.ALIGN.CENTER)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Time_Hour_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Time_Hour_Label, lv.PART.MAIN | lv.STATE.DEFAULT, lv.STYLE.TEXT_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Time_Hour_Label.set_style_text_font(self.resourceManager.load_font("DISPLAYR", 60), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.screen.add_event_cb(self.ScheduleScreen_eventhandler, lv.EVENT.ALL, None)
        lv.timer_create(self.ui_update_now, SEC_STEP, None)
        lv.timer_create(self.ui_update_target, 60 * 1000, None)  # 1分钟更新一次
    def ScheduleScreen_eventhandler(self, event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOADED and True:
            self.ui_update_now()
            self.ui_update_target()
            self.top_Animation(self.ui_Calendar_Month_Now, 0)
            self.top_Animation(self.ui_Calendar_Day_Now, 0)
            self.left_Animation(self.ui_Time_Min_Label_Now, 0)
            self.right_Animation(self.ui_Time_Hour_Label_Now, 0)
            self.opa_on_Animation(self.ui_Time_Dot_Label_Now, 0)
            self.opa_on_Animation(self.ui_Days, 0)
            self.opa_on_Animation(self.ui_Hours, 0)
            self.opa_on_Animation(self.ui_Minutes, 0)
            self.opa_on_Animation(self.ui_Event_Name_Label, 0)
            self.bottom_Animation(self.ui_Session_Name_Label, 0)
            self.top_Animation(self.ui_Upcoming_Label, 0)
        if event == lv.EVENT.SCREEN_LOADED:
            self.Breath_Animation(self.ui_Time_Dot_Label_Now)
        return

    def map_range(self, value, original_min, original_max, target_min, target_max):
        # 计算线性映射
        return target_min + (value - original_min) * (target_max - target_min) / (original_max - original_min)

    def ui_update_target(self, _=None):
        '''
        更新赛历时间标签
        :return:
        '''
        self.f1_event = self.f1.get_eventing()
        event_name, session, tip = self.f1_event
        y, month, d, h, m, s, *_ = self.timeDriver.get_local_time_from(session["session_begin_utc"])
        self.ui_Calendar_Month.set_text(f"{month:02}")
        self.ui_Calendar_Day.set_text(f"{d:02}")
        self.ui_Time_Hour_Label.set_text(f"{h:02}")
        self.ui_Time_Min_Label.set_text(f"{m:02}")
        self.ui_Event_Name_Label.set_text(event_name)
        self.ui_Session_Name_Label.set_text(session["session_name"])

    def ui_update_now(self, _=None):
        '''
        1:更新本地时间标签
        :return:
        '''
        y, month, d, h, m, s, *_ = self.timeDriver.get_local_time()
        # 获取当前毫秒数
        current_millis = (time.time_ns() // 1000000) % 1000
        # 计算秒针的位置
        arc_value = (s * 1000 + current_millis)
        self.ui_Second_Arc.set_value(int(self.map_range(arc_value, 0, 59999, 0, 30000)))
        # 更新当前表盘时间
        self.ui_Calendar_Month_Now.set_text(f"{month:02}")
        self.ui_Calendar_Day_Now.set_text(f"{d:02}")
        self.ui_Time_Hour_Label_Now.set_text(f"{h:02}")
        self.ui_Time_Min_Label_Now.set_text(f"{m:02}")
        # 更新左侧剩余时间标签
        event_name, session, tip = self.f1_event
        event_unixtime = session["session_begin_utc"]
        now_unixtime = self.timeDriver.get_unixtime()
        if now_unixtime > event_unixtime:
            self.ui_Days.set_text("0")
            self.ui_Hours.set_text("0")
            self.ui_Minutes.set_text("0")
        else:
            days, hours, minutes = calculate_time_difference(now_unixtime, event_unixtime)
            self.ui_Days.set_text(f'{days}')
            self.ui_Hours.set_text(f'{hours:02}')
            self.ui_Minutes.set_text(f'{minutes:02}')

import lvgl as lv
from ui.screen import Screen
from ui.theme_manager import Themes, ThemeManager


class TeamRadioScreen(Screen):
    def __init__(self):
        super().__init__()

        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.screen.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Team_Label = lv.label(self.screen)
        self.ui_Team_Label.set_text("RedBull Racing")
        self.ui_Team_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Team_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Team_Label.set_x(-1)
        self.ui_Team_Label.set_y(lv.pct(12))
        self.ui_Team_Label.set_align(lv.ALIGN.TOP_MID)
        self.ui_Team_Label.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Label.set_style_text_font(self.resourceManager.load_font("F1R", 14),
                                               lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Team_Color_Container = lv.obj(self.screen)
        self.ui_Team_Color_Container.remove_style_all()
        self.ui_Team_Color_Container.set_width(105)
        self.ui_Team_Color_Container.set_height(3)
        self.ui_Team_Color_Container.set_x(67)
        self.ui_Team_Color_Container.set_y(19)
        self.SetFlag(self.ui_Team_Color_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Team_Color_Container, lv.obj.FLAG.SCROLLABLE, False)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Team_Color_Container,
                                                                 lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.BG_COLOR,
                                                                 Themes.UI_THEME_COLOR_COLORTEAMSECOND)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Team_Color_Container,
                                                                 lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.BG_OPA, Themes.UI_THEME_COLOR_COLORTEAMSECOND)

        self.ui_wave_Container = lv.obj(self.screen)
        self.ui_wave_Container.remove_style_all()
        self.ui_wave_Container.set_width(178)
        self.ui_wave_Container.set_height(44)
        self.ui_wave_Container.set_x(0)
        self.ui_wave_Container.set_y(-50)
        self.ui_wave_Container.set_align(lv.ALIGN.CENTER)
        self.SetFlag(self.ui_wave_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_wave_Container, lv.obj.FLAG.SCROLLABLE, False)
        self._lottie = lv.rlottie_create_from_raw(self.ui_wave_Container, 178, 44, self.resourceManager.load_raw(
            f'ui/assets/team_{self.themeManager.getCurrentThemeIndex():02}.json'))
        lv.rlottie_set_play_mode(self._lottie, lv.RLOTTIE_CTRL.LOOP)
        self._lottie.set_width(lv.SIZE.CONTENT)  # 1
        self._lottie.set_height(lv.SIZE.CONTENT)  # 1
        self._lottie.set_align(lv.ALIGN.CENTER)

        ui_Msg_Container = lv.obj(self.screen)
        ui_Msg_Container.remove_style_all()
        ui_Msg_Container.set_width(193)
        ui_Msg_Container.set_height(163)
        ui_Msg_Container.set_x(32)
        ui_Msg_Container.set_y(48)
        self.SetFlag(ui_Msg_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_Msg_Container, lv.obj.FLAG.SCROLLABLE, False)

        self.ui_Team_Color_Container2 = lv.obj(ui_Msg_Container)
        self.ui_Team_Color_Container2.remove_style_all()
        self.ui_Team_Color_Container2.set_width(5)
        self.ui_Team_Color_Container2.set_height(25)
        self.ui_Team_Color_Container2.set_x(7)
        self.ui_Team_Color_Container2.set_y(54)
        self.SetFlag(self.ui_Team_Color_Container2, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Team_Color_Container2, lv.obj.FLAG.SCROLLABLE, False)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Team_Color_Container2,
                                                                 lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.BG_COLOR, Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Team_Color_Container2,
                                                                 lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.BG_OPA, Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Team_Color_Container2.set_style_shadow_color(lv.color_hex(0x00CCB7), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Color_Container2.set_style_shadow_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Color_Container2.set_style_shadow_width(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Color_Container2.set_style_shadow_spread(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Color_Container2.set_style_shadow_ofs_x(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Team_Color_Container2.set_style_shadow_ofs_y(0, lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_Customer_Person = lv.img(ui_Msg_Container)
        ui_Customer_Person.set_src(self.resourceManager.load_img("/ui/assets/loading_person.bin"))
        ui_Customer_Person.set_width(lv.SIZE.CONTENT)  # 1
        ui_Customer_Person.set_height(lv.SIZE.CONTENT)  # 1
        ui_Customer_Person.set_x(63)
        ui_Customer_Person.set_y(42)
        ui_Customer_Person.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_Customer_Person, lv.obj.FLAG.ADV_HITTEST, True)
        self.SetFlag(ui_Customer_Person, lv.obj.FLAG.SCROLLABLE, False)
        ui_Customer_Person.set_zoom(235)
        self.msg_txt = ''''''
        self.msg_length = len(self.msg_txt)
        self.msg_index = 0
        self.ui_Msg_Label = lv.label(ui_Msg_Container)
        self.ui_Msg_Label.set_text(self.msg_txt)
        self.ui_Msg_Label.set_width(134)
        self.ui_Msg_Label.set_height(54)
        self.ui_Msg_Label.set_x(7)
        self.ui_Msg_Label.set_y(93)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Msg_Label, lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.TEXT_COLOR,
                                                                 Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(self.ui_Msg_Label, lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.TEXT_OPA,
                                                                 Themes.UI_THEME_COLOR_COLORTEAM)
        self.ui_Msg_Label.set_style_text_letter_space(0, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Msg_Label.set_style_text_line_space(3, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Msg_Label.set_style_text_align(lv.TEXT_ALIGN.LEFT, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Msg_Label.set_style_text_font(self.resourceManager.load_font("F1R", 10),
                                              lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_Driver_Label = lv.label(ui_Msg_Container)
        self.ui_Driver_Label.set_text("VER")
        self.ui_Driver_Label.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_Driver_Label.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_Driver_Label.set_x(20)
        self.ui_Driver_Label.set_y(57)
        self.ui_Driver_Label.set_style_text_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Driver_Label.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_Driver_Label.set_style_text_font(self.resourceManager.load_font("F1B", 18),
                                                 lv.PART.MAIN | lv.STATE.DEFAULT)
        self.timer = lv.timer_create(self.update_msg, 30, None)
        self.timer.pause()
        self.screen.add_event_cb(self.TeamRadioScreen_eventhandler, lv.EVENT.ALL, None)

    def TeamRadioScreen_eventhandler(self, event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOAD_START and True:
            self.left_Animation(self.ui_Team_Color_Container, 0)
            self.right_Animation(self.ui_Team_Label, 0)
            self.opa_on_Animation(self.ui_wave_Container, 0)
            self.opa_on_Animation(self.ui_Driver_Label, 0)
        if event == lv.EVENT.SCREEN_LOADED:
            self.play_msg('''"I CAN'T BELIEVE YOU GUYS *** *** ME. CAN'T TELL YOU HOW **** *I AM"''')
        return

    def play_msg(self, msg):
        self.timer.pause()
        #self.ui_Msg_Label("")
        self.msg_txt = msg
        self.msg_length = len(self.msg_txt)
        self.msg_index = 0
        self.timer.resume()

    def update_msg(self,timer):
        self.msg_index += 1
        if self.msg_index > self.msg_length:
            self.timer.pause()
        self.ui_Msg_Label.set_text(self.msg_txt[:self.msg_index])

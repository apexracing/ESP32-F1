import lvgl as lv

class _ui_theme_variable:
    def __init__(self):
        self.target = None
        self.color = 0


def singleton(cls):
    instance = None

    def getinstance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return getinstance

class Themes:
    UI_THEME_DEFAULT = 0
    UI_THEME_AMG = 1
    UI_THEME_FERRARI = 2

    UI_THEME_COLOR_COLORTEAMTHREE = 0
    UI_THEME_COLOR_COLORTEAM = 1
    UI_THEME_COLOR_COLORTEAMSECOND = 2
@singleton
class ThemeManager:


    def __init__(self):
        dispp = lv.disp_get_default()
        theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True,lv.font_default())
        dispp.set_theme(theme)
        self._ui_theme_color_Default = [0xFFDD00, 0x3671C6, 0xFF0101]
        self._ui_theme_alpha_Default = [255, 255, 255]

        self._ui_theme_color_AMG = [0xFFDD00, 0x00D1BA, 0xFFFFFF]
        self._ui_theme_alpha_AMG = [255, 255, 255]

        self._ui_theme_color_ferrari_ = [0x04AFFA, 0xFF2800, 0xFFDD00]
        self._ui_theme_alpha_ferrari_ = [255, 255, 255]

        self._ui_theme_list_colors = [self._ui_theme_color_Default, self._ui_theme_color_AMG,
                                      self._ui_theme_color_ferrari_]
        self._ui_theme_list_alphas = [self._ui_theme_alpha_Default, self._ui_theme_alpha_AMG,
                                      self._ui_theme_alpha_ferrari_]

        self.ui_theme_current_colors = []

        self.ui_theme_current_alphas = []
        self.ui_local_style_list = {}
        self.current_theme_index=Themes.UI_THEME_DEFAULT

    def ui_object_set_themeable_style_property(self, target, selector, property, coloridx):

        if not (id(target) in self.ui_local_style_list):
            self.ui_local_style_list[id(target)] = {}

        if not property in self.ui_local_style_list[id(target)]:
            self.ui_local_style_list[id(target)][property] = {}

        self.ui_local_style_list[id(target)][property][selector] = _ui_theme_variable()
        self.ui_local_style_list[id(target)][property][selector].target = target
        self.ui_local_style_list[id(target)][property][selector].color = coloridx
        self.ui_update_theme_value(target, property, selector)

    def ui_update_theme_value(self, target, property, selector):

        if not (id(target) in self.ui_local_style_list):
            return

        if not property in self.ui_local_style_list[id(target)]:
            return

        if not selector in self.ui_local_style_list[id(target)][property]:
            return

        coloridx = self.ui_local_style_list[id(target)][property][selector].color
        color = lv.style_value_t()

        if (property == lv.STYLE.BG_COLOR or
                property == lv.STYLE.BG_GRAD_COLOR or
                property == lv.STYLE.BORDER_COLOR or
                property == lv.STYLE.OUTLINE_COLOR or
                property == lv.STYLE.TEXT_COLOR or
                property == lv.STYLE.LINE_COLOR or
                property == lv.STYLE.ARC_COLOR or
                property == lv.STYLE.SHADOW_COLOR or
                property == lv.STYLE.BG_IMG_RECOLOR or
                property == lv.STYLE.IMG_RECOLOR):
            color.color = lv.color_hex(self.ui_theme_current_colors[coloridx])
        else:
            color.num = self.ui_theme_current_alphas[coloridx]
        target.set_local_style_prop(property, color, selector)

    def ui_theme_manager_reset(self):
        self.ui_local_style_list = {}

    def ui_theme_update_all(self):
        for obj in self.ui_local_style_list:
            targetid = obj
            proplist = self.ui_local_style_list[obj]
            for prop in proplist:
                lvprop = prop
                selectlist = self.ui_local_style_list[obj][prop]
                for select in selectlist:
                    lvselect = select
                    target = self.ui_local_style_list[obj][prop][lvselect].target
                    self.ui_update_theme_value(target, lvprop, lvselect)

    def ui_theme_set(self, index):
        self.current_theme_index=index
        self.ui_theme_current_colors = self._ui_theme_list_colors[index]
        self.ui_theme_current_alphas = self._ui_theme_list_alphas[index]
        self.ui_theme_update_all()

    def getCurrentThemeIndex(self):
        return self.current_theme_index

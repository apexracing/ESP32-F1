import lvgl as lv
from ui.resource_manager import ResourceManager
from ui.theme_manager import ThemeManager


class Screen:
    def __init__(self):
        self._ui_comp_table = {}
        self._ui_comp_prev = None
        self._ui_name_prev = None
        self._ui_child_prev = None
        self._ui_comp_table.clear()

        self.screen = lv.obj()
        self.resourceManager = ResourceManager()
        self.themeManager = ThemeManager()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)

    def src_load(self):
        lv.scr_load(self.screen)

    def src_load_anim(self, fademode=lv.SCR_LOAD_ANIM.OVER_TOP, auto_del=False, speed=100, delay=0):
        '''

        :param fademode: FADE_IN,FADE_OUT,MOVE_TOP
        :param speed:
        :param delay:
        :return:
        '''
        lv.scr_load_anim(self.screen, fademode, speed, delay, auto_del)
        return

    def SetFlag(self, obj, flag, value):
        if (value):
            obj.add_flag(flag)
        else:
            obj.clear_flag(flag)
        return

    def _ui_comp_del_event(self, e):
        target = e.get_target()
        self._ui_comp_table[id(target)].remove()

    def ui_comp_get_child(self, comp, child_name):
        return self._ui_comp_table[id(comp)][child_name]

    def ui_comp_get_root_from_child(self, child, compname):
        for component in self._ui_comp_table:
            if self._ui_comp_table[component]["_CompName"] == compname:
                for part in self._ui_comp_table[component]:
                    if id(self._ui_comp_table[component][part]) == id(child):
                        return self._ui_comp_table[component]
        return None

    def DeleteScreen(self, src):
        return

    def ModifyFlag(self, obj, flag, value):
        if (value == "TOGGLE"):
            if (obj.has_flag(flag)):
                obj.clear_flag(flag)
            else:
                obj.add_flag(flag)
            return

        if (value == "ADD"):
            obj.add_flag(flag)
        else:
            obj.clear_flag(flag)
        return

    def ModifyState(self, obj, state, value):
        if (value == "TOGGLE"):
            if (obj.has_state(state)):
                obj.clear_state(state)
            else:
                obj.add_state(state)
            return

        if (value == "ADD"):
            obj.add_state(state)
        else:
            obj.clear_state(state)
        return

    def set_opacity(self, obj, v):
        obj.set_style_opa(v, lv.STATE.DEFAULT | lv.PART.MAIN)
        return

    def Flash_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_ease_out)
        PropertyAnimation_0.set_time(1000)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_style_opa(v, 0))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(lv.ANIM_REPEAT.INFINITE)
        PropertyAnimation_0.set_repeat_delay(0)  # + 1000
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(1000)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(255, 100)
        lv.anim_t.start(PropertyAnimation_0)

        print("Flash_Animation called")
        return

    def left_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_overshoot)
        PropertyAnimation_0.set_time(500)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_x(v))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(0)
        PropertyAnimation_0.set_repeat_delay(0)  # + 500
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(0)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(-100, 0)
        PropertyAnimation_0.set_get_value_cb(lambda a: TargetObject.get_x_aligned())
        lv.anim_t.start(PropertyAnimation_0)
        PropertyAnimation_1 = lv.anim_t()
        PropertyAnimation_1.init()
        PropertyAnimation_1.set_path_cb(lv.anim_t.path_linear)
        PropertyAnimation_1.set_time(300)
        PropertyAnimation_1.set_var(TargetObject)
        PropertyAnimation_1.set_custom_exec_cb(lambda a, v: TargetObject.set_style_opa(v, 0))
        PropertyAnimation_1.set_delay(delay + 0)
        PropertyAnimation_1.set_repeat_count(0)
        PropertyAnimation_1.set_repeat_delay(0)  # + 500
        PropertyAnimation_1.set_playback_delay(0)
        PropertyAnimation_1.set_playback_time(0)
        PropertyAnimation_1.set_early_apply(False)
        PropertyAnimation_1.set_values(0, 255)
        PropertyAnimation_1.set_get_value_cb(lambda a: TargetObject.get_style_opa(0))
        lv.anim_t.start(PropertyAnimation_1)

        print("left_Animation called")
        return

    def right_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_overshoot)
        PropertyAnimation_0.set_time(500)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_x(v))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(0)
        PropertyAnimation_0.set_repeat_delay(0)  # + 500
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(0)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(150, 0)
        PropertyAnimation_0.set_get_value_cb(lambda a: TargetObject.get_x_aligned())
        lv.anim_t.start(PropertyAnimation_0)
        PropertyAnimation_1 = lv.anim_t()
        PropertyAnimation_1.init()
        PropertyAnimation_1.set_path_cb(lv.anim_t.path_linear)
        PropertyAnimation_1.set_time(300)
        PropertyAnimation_1.set_var(TargetObject)
        PropertyAnimation_1.set_custom_exec_cb(lambda a, v: TargetObject.set_style_opa(v, 0))
        PropertyAnimation_1.set_delay(delay + 0)
        PropertyAnimation_1.set_repeat_count(0)
        PropertyAnimation_1.set_repeat_delay(0)  # + 500
        PropertyAnimation_1.set_playback_delay(0)
        PropertyAnimation_1.set_playback_time(0)
        PropertyAnimation_1.set_early_apply(False)
        PropertyAnimation_1.set_values(0, 255)
        PropertyAnimation_1.set_get_value_cb(lambda a: TargetObject.get_style_opa(0))
        lv.anim_t.start(PropertyAnimation_1)

        print("right_Animation called")
        return

    def opa_on_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_linear)
        PropertyAnimation_0.set_time(500)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_style_opa(v, 0))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(0)
        PropertyAnimation_0.set_repeat_delay(0)  # + 500
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(0)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(0, 255)
        PropertyAnimation_0.set_get_value_cb(lambda a: TargetObject.get_style_opa(0))
        lv.anim_t.start(PropertyAnimation_0)

        print("opa_on_Animation called")
        return

    def top_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_overshoot)
        PropertyAnimation_0.set_time(400)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_y(v))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(0)
        PropertyAnimation_0.set_repeat_delay(0)  # + 400
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(0)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(-100, 0)
        PropertyAnimation_0.set_get_value_cb(lambda a: TargetObject.get_y_aligned())
        lv.anim_t.start(PropertyAnimation_0)

        print("top_Animation called")
        return

    def bottom_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_overshoot)
        PropertyAnimation_0.set_time(400)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_y(v))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(0)
        PropertyAnimation_0.set_repeat_delay(0)  # + 400
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(0)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(150, 0)
        PropertyAnimation_0.set_get_value_cb(lambda a: TargetObject.get_y_aligned())
        lv.anim_t.start(PropertyAnimation_0)

        print("bottom_Animation called")
        return

    def driver_left_Animation(self, TargetObject, delay):
        PropertyAnimation_0 = lv.anim_t()
        PropertyAnimation_0.init()
        PropertyAnimation_0.set_path_cb(lv.anim_t.path_linear)
        PropertyAnimation_0.set_time(300)
        PropertyAnimation_0.set_var(TargetObject)
        PropertyAnimation_0.set_custom_exec_cb(lambda a, v: TargetObject.set_x(v))
        PropertyAnimation_0.set_delay(delay + 0)
        PropertyAnimation_0.set_repeat_count(0)
        PropertyAnimation_0.set_repeat_delay(0)  # + 300
        PropertyAnimation_0.set_playback_delay(0)
        PropertyAnimation_0.set_playback_time(0)
        PropertyAnimation_0.set_early_apply(False)
        PropertyAnimation_0.set_values(100, 0)
        PropertyAnimation_0.set_get_value_cb(lambda a: TargetObject.get_x_aligned())
        lv.anim_t.start(PropertyAnimation_0)
        PropertyAnimation_1 = lv.anim_t()
        PropertyAnimation_1.init()
        PropertyAnimation_1.set_path_cb(lv.anim_t.path_linear)
        PropertyAnimation_1.set_time(300)
        PropertyAnimation_1.set_var(TargetObject)
        PropertyAnimation_1.set_custom_exec_cb(lambda a, v: TargetObject.set_style_opa(v, 0))
        PropertyAnimation_1.set_delay(delay + 0)
        PropertyAnimation_1.set_repeat_count(0)
        PropertyAnimation_1.set_repeat_delay(0)  # + 300
        PropertyAnimation_1.set_playback_delay(0)
        PropertyAnimation_1.set_playback_time(0)
        PropertyAnimation_1.set_early_apply(False)
        PropertyAnimation_1.set_values(0, 255)
        PropertyAnimation_1.set_get_value_cb(lambda a: TargetObject.get_style_opa(0))
        lv.anim_t.start(PropertyAnimation_1)

        print("driver_left_Animation called")
        return

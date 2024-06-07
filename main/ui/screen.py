import lvgl as lv
from common.resource_manager import ResourceManager

class Screen:
    def __init__(self):
        self._ui_comp_table = {}
        self._ui_comp_prev = None
        self._ui_name_prev = None
        self._ui_child_prev = None
        self._ui_comp_table.clear()
        dispp = lv.disp_get_default()
        theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
        dispp.set_theme(theme)
        self.screen=lv.obj()
        self.resourceManager=ResourceManager()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
    def src_load(self):
        lv.scr_load(self.screen)
    def src_load_anim(self, fademode=lv.SCR_LOAD_ANIM.OVER_TOP,auto_del=False, speed=100, delay=0):
        '''

        :param fademode: FADE_IN,FADE_OUT,MOVE_TOP
        :param speed:
        :param delay:
        :return:
        '''
        lv.scr_load_anim(self.screen, fademode, speed, delay, auto_del)
        return
    def SetFlag(self,obj, flag, value):
        if (value):
            obj.add_flag(flag)
        else:
            obj.clear_flag(flag)
        return

    def _ui_comp_del_event(self,e):
        target = e.get_target()
        self._ui_comp_table[id(target)].remove()

    def ui_comp_get_child(self,comp, child_name):
        return self._ui_comp_table[id(comp)][child_name]

    def ui_comp_get_root_from_child(self,child, compname):
        for component in self._ui_comp_table:
            if self._ui_comp_table[component]["_CompName"] == compname:
                for part in self._ui_comp_table[component]:
                    if id(self._ui_comp_table[component][part]) == id(child):
                        return self._ui_comp_table[component]
        return None

    def SetBarProperty(self,target, id, val):
        if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
        if id == 'Value': target.set_value(val, lv.ANIM.OFF)
        return

    def SetPanelProperty(self,target, id, val):
        if id == 'Position_X': target.set_x(val)
        if id == 'Position_Y': target.set_y(val)
        if id == 'Width': target.set_width(val)
        if id == 'Height': target.set_height(val)
        return

    def SetDropdownProperty(self,target, id, val):
        if id == 'Selected':
            target.set_selected(val)
        return

    def SetImageProperty(self,target, id, val, val2):
        if id == 'Image': target.set_src(val)
        if id == 'Angle': target.set_angle(val2)
        if id == 'Zoom': target.set_zoom(val2)
        return

    def SetLabelProperty(self,target, id, val):
        if id == 'Text': target.set_text(val)
        return

    def SetRollerProperty(self,target, id, val):
        if id == 'Selected':
            target.set_selected(val, lv.ANIM.OFF)
        if id == 'Selected_with_anim':
            target.set_selected(val, lv.ANIM.ON)
        return

    def SetSliderProperty(self,target, id, val):
        if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
        if id == 'Value': target.set_value(val, lv.ANIM.OFF)
        return



    def DeleteScreen(self,src):
        return

    def IncrementArc(self,trg, val):
        trg.set_value(trg.get_value() + val)
        lv.event_send(trg, lv.EVENT.VALUE_CHANGED, None)
        return

    def IncrementBar(self,trg, val, anim):
        trg.set_value(trg.get_value() + val, anim)
        return

    def IncrementSlider(self,trg, val, anim):
        trg.set_value(trg.get_value() + val, anim)
        lv.event_send(trg, lv.EVENT.VALUE_CHANGED, None)
        return

    def KeyboardSetTarget(self,keyboard, textarea):
        keyboard.set_textarea(textarea)
        return

    def ModifyFlag(self,obj, flag, value):
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

    def ModifyState(self,obj, state, value):
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

    def TextAreaMoveCursor(self,trg, val):
        if val == "UP": trg.cursor_up()
        if val == "RIGHT": trg.cursor_right()
        if val == "DOWN": trg.cursor_down()
        if val == "LEFT": trg.cursor_left()
        trg.add_state(lv.STATE.FOCUSED)
        return

    def set_opacity(self,obj, v):
        obj.set_style_opa(v, lv.STATE.DEFAULT | lv.PART.MAIN)
        return

    def SetTextValueArc(self,trg, src, prefix, postfix):
        trg.set_text(prefix + str(src.get_value()) + postfix)
        return

    def SetTextValueSlider(self,trg, src, prefix, postfix):
        trg.set_text(prefix + str(src.get_value()) + postfix)
        return

    def SetTextValueChecked(self,trg, src, txton, txtoff):
        if src.has_state(lv.STATE.CHECKED):
            trg.set_text(txton)
        else:
            trg.set_text(txtoff)
        return

    def StepSpinbox(self,trg, val):
        if val == 1: trg.increment()
        if val == -1: trg.decrement()
        lv.event_send(trg, lv.EVENT.VALUE_CHANGED, None)
        return
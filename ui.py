# This file was generated by SquareLine Studio
# SquareLine Studio version: SquareLine Studio 1.4.0
# LVGL version: 8.3.11
# Project name: SquareLine_Project

import lvgl as lv
import ui_images

dispp = lv.disp_get_default()
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
dispp.set_theme(theme)

def ui_theme_set(idx):
   return

def SetFlag( obj, flag, value):
    if (value):
        obj.add_flag(flag)
    else:
        obj.clear_flag(flag)
    return

_ui_comp_table = {}
_ui_comp_prev = None
_ui_name_prev = None
_ui_child_prev = None
_ui_comp_table.clear()

def _ui_comp_del_event(e):
    target = e.get_target()
    _ui_comp_table[id(target)].remove()

def ui_comp_get_child(comp, child_name):
    return _ui_comp_table[id(comp)][child_name]

def ui_comp_get_root_from_child(child, compname):
    for component in _ui_comp_table:
        if _ui_comp_table[component]["_CompName"]==compname:
            for part in _ui_comp_table[component]:
                if id(_ui_comp_table[component][part]) == id(child):
                    return _ui_comp_table[component]
    return None
def SetBarProperty(target, id, val):
   if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
   if id == 'Value': target.set_value(val, lv.ANIM.OFF)
   return

def SetPanelProperty(target, id, val):
   if id == 'Position_X': target.set_x(val)
   if id == 'Position_Y': target.set_y(val)
   if id == 'Width': target.set_width(val)
   if id == 'Height': target.set_height(val)
   return

def SetDropdownProperty(target, id, val):
   if id == 'Selected':
      target.set_selected(val)
   return

def SetImageProperty(target, id, val, val2):
   if id == 'Image': target.set_src(val)
   if id == 'Angle': target.set_angle(val2)
   if id == 'Zoom': target.set_zoom(val2)
   return

def SetLabelProperty(target, id, val):
   if id == 'Text': target.set_text(val)
   return

def SetRollerProperty(target, id, val):
   if id == 'Selected':
      target.set_selected(val, lv.ANIM.OFF)
   if id == 'Selected_with_anim':
      target.set_selected(val, lv.ANIM.ON)
   return

def SetSliderProperty(target, id, val):
   if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
   if id == 'Value': target.set_value(val, lv.ANIM.OFF)
   return

def ChangeScreen( src, fademode, speed, delay):
    lv.scr_load_anim(src, fademode, speed, delay, False)
    return

def DeleteScreen(src):
    return

def IncrementArc( trg, val):
    trg.set_value(trg.get_value()+val)
    lv.event_send(trg,lv.EVENT.VALUE_CHANGED, None)
    return

def IncrementBar( trg, val, anim):
    trg.set_value(trg.get_value()+val,anim)
    return

def IncrementSlider( trg, val, anim):
    trg.set_value(trg.get_value()+val,anim)
    lv.event_send(trg,lv.EVENT.VALUE_CHANGED, None)
    return

def KeyboardSetTarget( keyboard, textarea):
    keyboard.set_textarea(textarea)
    return

def ModifyFlag( obj, flag, value):
    if (value=="TOGGLE"):
        if ( obj.has_flag(flag) ):
            obj.clear_flag(flag)
        else:
            obj.add_flag(flag)
        return

    if (value=="ADD"):
        obj.add_flag(flag)
    else:
        obj.clear_flag(flag)
    return

def ModifyState( obj, state, value):
    if (value=="TOGGLE"):
        if ( obj.has_state(state) ):
            obj.clear_state(state)
        else:
            obj.add_state(state)
        return

    if (value=="ADD"):
        obj.add_state(state)
    else:
        obj.clear_state(state)
    return

def TextAreaMoveCursor( trg, val):
    if val=="UP" : trg.cursor_up()
    if val=="RIGHT" : trg.cursor_right()
    if val=="DOWN" : trg.cursor_down()
    if val=="LEFT" : trg.cursor_left()
    trg.add_state(lv.STATE.FOCUSED)
    return

def set_opacity(obj, v):
    obj.set_style_opa(v, lv.STATE.DEFAULT|lv.PART.MAIN)
    return

def SetTextValueArc( trg, src, prefix, postfix):
    trg.set_text(prefix+str(src.get_value())+postfix)
    return

def SetTextValueSlider( trg, src, prefix, postfix):
    trg.set_text(prefix+str(src.get_value())+postfix)
    return

def SetTextValueChecked( trg, src, txton, txtoff):
    if src.has_state(lv.STATE.CHECKED):
        trg.set_text(txton)
    else:
        trg.set_text(txtoff)
    return

def StepSpinbox( trg, val):
    if val==1 : trg.increment()
    if val==-1 : trg.decrement()
    lv.event_send(trg,lv.EVENT.VALUE_CHANGED, None)
    return

def SwitchTheme(val):
    ui_theme_set(val)
    return

# COMPONENTS
ui____initial_actions0 = lv.obj()

ui_Screen1 = lv.obj()
SetFlag(ui_Screen1, lv.obj.FLAG.SCROLLABLE, False)

ui_Label1 = lv.label(ui_Screen1)
ui_Label1.set_text("SPEED IMPRINT")
ui_Label1.set_width(lv.SIZE.CONTENT)	# 1
ui_Label1.set_height(lv.SIZE.CONTENT)   # 1
ui_Label1.set_x(1)
ui_Label1.set_y(-34)
ui_Label1.set_align( lv.ALIGN.CENTER)
ui_Label1.set_style_text_font( lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_Button1 = lv.btn(ui_Screen1)
ui_Button1.set_width(100)
ui_Button1.set_height(50)
ui_Button1.set_x(2)
ui_Button1.set_y(16)
ui_Button1.set_align( lv.ALIGN.CENTER)
SetFlag(ui_Button1, lv.obj.FLAG.SCROLLABLE, False)
SetFlag(ui_Button1, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
ui_Button1.set_style_bg_color(lv.color_hex(0x0627FF), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Button1.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

ui_Label3 = lv.label(ui_Button1)
ui_Label3.set_text("Button")
ui_Label3.set_width(lv.SIZE.CONTENT)	# 1
ui_Label3.set_height(lv.SIZE.CONTENT)   # 1
ui_Label3.set_align( lv.ALIGN.CENTER)

ui_Slider1 = lv.slider(ui_Screen1)
ui_Slider1.set_width(150)
ui_Slider1.set_height(10)
ui_Slider1.set_x(6)
ui_Slider1.set_y(64)
ui_Slider1.set_align( lv.ALIGN.CENTER)
ui_Slider1.set_value(0, lv.ANIM.OFF)  # need refresh: 0,100
if 'NORMAL' is 'RANGE': ui_Slider1.set_left_value(0, lv.ANIM.OFF)
ui_Slider1.set_style_bg_color(lv.color_hex(0x02FF5A), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_Slider1.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

lv.scr_load(ui_Screen1)

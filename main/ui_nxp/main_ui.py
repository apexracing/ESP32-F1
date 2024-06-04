import lvgl as lv
from ui_nxp.gui_guider import *
#将NXP GUI_Builder生成的代码粘到这里
# Create screen
screen = lv.obj()
screen.set_size(240, 240)
screen.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
# Set style for screen, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen.set_style_bg_color(lv.color_hex(0x000000), lv.PART.MAIN|lv.STATE.DEFAULT)
screen.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_label_1
screen_label_1 = lv.label(screen)
screen_label_1.set_text("SPEED IMPRINT")
screen_label_1.set_long_mode(lv.label.LONG.WRAP)
screen_label_1.set_width(lv.pct(100))
screen_label_1.set_pos(38, 40)
screen_label_1.set_size(160, 21)
# Set style for screen_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_font(test_font("F1_Regular", 14), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_letter_space(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_line_space(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_bg_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_pad_top(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_pad_right(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_pad_bottom(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_pad_left(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_slider_1
screen_slider_1 = lv.slider(screen)
screen_slider_1.set_range(0, 100)
screen_slider_1.set_mode(lv.slider.MODE.NORMAL)
screen_slider_1.set_value(50, lv.ANIM.OFF)
screen_slider_1.set_pos(40, 167)
screen_slider_1.set_size(160, 8)
# Set style for screen_slider_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_slider_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_slider_1.set_style_bg_color(lv.color_hex(0x393c41), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_slider_1.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_slider_1.set_style_radius(50, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_slider_1.set_style_outline_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_slider_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)

# Set style for screen_slider_1, Part: lv.PART.INDICATOR, State: lv.STATE.DEFAULT.
screen_slider_1.set_style_bg_opa(255, lv.PART.INDICATOR|lv.STATE.DEFAULT)
screen_slider_1.set_style_bg_color(lv.color_hex(0x00a1b5), lv.PART.INDICATOR|lv.STATE.DEFAULT)
screen_slider_1.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.INDICATOR|lv.STATE.DEFAULT)
screen_slider_1.set_style_radius(50, lv.PART.INDICATOR|lv.STATE.DEFAULT)

# Set style for screen_slider_1, Part: lv.PART.KNOB, State: lv.STATE.DEFAULT.
screen_slider_1.set_style_bg_opa(255, lv.PART.KNOB|lv.STATE.DEFAULT)
screen_slider_1.set_style_bg_color(lv.color_hex(0x2195f6), lv.PART.KNOB|lv.STATE.DEFAULT)
screen_slider_1.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.KNOB|lv.STATE.DEFAULT)
screen_slider_1.set_style_radius(50, lv.PART.KNOB|lv.STATE.DEFAULT)
screen_slider_1.set_size(160, 8)

with open('ui_nxp/assets/team.json','r') as f:
    lottie_data=f.read()
lottie1=lv.rlottie_create_from_raw(screen,160,50,lottie_data)
lottie1.set_pos(40,65)
lottie1.set_size(160, 50)

screen.update_layout()
# content from custom.py

# Load the default screen
lv.scr_load(screen)
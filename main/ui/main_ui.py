import lvgl as lv
from ui.gui_guider import *
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
screen_label_1.set_pos(35, 66)
screen_label_1.set_size(170, 26)
# Set style for screen_label_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_label_1.set_style_border_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_radius(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_label_1.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
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

# Create screen_btn_1
screen_btn_1 = lv.btn(screen)
screen_btn_1_label = lv.label(screen_btn_1)
screen_btn_1_label.set_text("Button")
screen_btn_1_label.set_long_mode(lv.label.LONG.WRAP)
screen_btn_1_label.set_width(lv.pct(100))
screen_btn_1_label.align(lv.ALIGN.CENTER, 0, 0)
screen_btn_1.set_style_pad_all(0, lv.STATE.DEFAULT)
screen_btn_1.set_pos(64, 98)
screen_btn_1.set_size(100, 50)
# Set style for screen_btn_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_btn_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_bg_color(lv.color_hex(0x0001ff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_border_width(2, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_border_opa(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_border_color(lv.color_hex(0x2195f6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_border_side(lv.BORDER_SIDE.FULL, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_radius(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_font(test_font("montserratMedium", 16), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_btn_1.set_style_text_align(lv.TEXT_ALIGN.CENTER, lv.PART.MAIN|lv.STATE.DEFAULT)

# Create screen_spinner_1
screen_spinner_1 = lv.spinner(screen, 1000, 60)
screen_spinner_1.set_pos(88, 10)
screen_spinner_1.set_size(58, 56)
# Set style for screen_spinner_1, Part: lv.PART.MAIN, State: lv.STATE.DEFAULT.
screen_spinner_1.set_style_pad_top(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_pad_bottom(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_pad_left(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_pad_right(5, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_bg_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_bg_color(lv.color_hex(0xeeeef6), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_bg_grad_dir(lv.GRAD_DIR.NONE, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_arc_width(12, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_arc_opa(255, lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_arc_color(lv.color_hex(0xd5d6de), lv.PART.MAIN|lv.STATE.DEFAULT)
screen_spinner_1.set_style_shadow_width(0, lv.PART.MAIN|lv.STATE.DEFAULT)
# Set style for screen_spinner_1, Part: lv.PART.INDICATOR, State: lv.STATE.DEFAULT.
screen_spinner_1.set_style_arc_width(12, lv.PART.INDICATOR|lv.STATE.DEFAULT)
screen_spinner_1.set_style_arc_opa(255, lv.PART.INDICATOR|lv.STATE.DEFAULT)
screen_spinner_1.set_style_arc_color(lv.color_hex(0x2195f6), lv.PART.INDICATOR|lv.STATE.DEFAULT)

screen.update_layout()

# content from custom.py

# Load the default screen
lv.scr_load(screen)
import lvgl as lv
from ui2 import ui_images
from ui2.ui import *
#将SquareLine生成的代码粘到这里

# COMPONENTS
ui____initial_actions0 = lv.obj()

ui_EmoilScreen = lv.obj()
SetFlag(ui_EmoilScreen, lv.obj.FLAG.SCROLLABLE, False)
ui_EmoilScreen.set_style_bg_color(lv.color_hex(0x0084CD), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_EmoilScreen.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
ui_EmoilScreen.set_style_bg_img_src( ui_images.ui_img_helmet_redbull_png, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_EmoilScreen_Container1 = lv.obj(ui_EmoilScreen)
ui_EmoilScreen_Container1.remove_style_all()
ui_EmoilScreen_Container1.set_width(120)
ui_EmoilScreen_Container1.set_height(80)
ui_EmoilScreen_Container1.set_x(0)
ui_EmoilScreen_Container1.set_y(20)
ui_EmoilScreen_Container1.set_align( lv.ALIGN.CENTER)
SetFlag(ui_EmoilScreen_Container1, lv.obj.FLAG.CLICKABLE, False)
SetFlag(ui_EmoilScreen_Container1, lv.obj.FLAG.SCROLLABLE, False)

with open('ui2/assets/e01.json','r') as f:
    lottie_data=f.read()
lottie1=lv.rlottie_create_from_raw(ui_EmoilScreen_Container1,120,80,lottie_data)
lottie1.set_width(lv.SIZE.CONTENT)	# 1
lottie1.set_height(lv.SIZE.CONTENT)   # 1
lottie1.set_align(lv.ALIGN.CENTER)

lv.scr_load(ui_EmoilScreen)

import lvgl as lv
from ui.screen import Screen
from ui.theme_manager import Themes, ThemeManager
from ui.resource_manager import ResourceManager
import math
import random
from lib.qmi_8658 import QMI8658
import gc

# 时间步长（秒）
dt = 0.016


class Tyre():
    # 定义物理属性
    gravity = 9.8 * 50  # 重力加速度（m/s^2）
    friction_coefficient = 0.01  # 摩擦系数
    bounce_coefficient = 0.95  # 碰撞后的弹性系数
    colors = [lv.color_hex(0xFFFFFF), lv.color_hex(0xCE0000), lv.color_hex(0xFFF807)]

    def __init__(self, scr, x, y):
        self.resourceManager = ResourceManager()
        self.themeManager = ThemeManager()
        self.radius = 75
        # 屏幕尺寸
        self.scr_width = scr.get_width()
        self.scr_height = scr.get_height()
        self.scr_radius = self.scr_width // 2
        self.center_x = self.scr_width // 2
        self.center_y = self.scr_height // 2
        self.ui_Tyre = lv.obj(scr)
        self.ui_Tyre.remove_style_all()
        self.ui_Tyre.set_width(self.radius * 2)  # 150
        self.ui_Tyre.set_height(self.radius * 2)  # 150
        self.SetFlag(self.ui_Tyre, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(self.ui_Tyre, lv.obj.FLAG.SCROLLABLE, False)
        self.ui_Tyre.set_style_radius(lv.RADIUS.CIRCLE, 0)

        ui_TyreRubber = lv.arc(self.ui_Tyre)
        ui_TyreRubber.set_width(150)
        ui_TyreRubber.set_height(150)
        ui_TyreRubber.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(ui_TyreRubber, lv.obj.FLAG.SCROLL_CHAIN, False)
        ui_TyreRubber.set_value(100)
        ui_TyreRubber.set_bg_angles(0, 360)
        ui_TyreRubber.set_style_arc_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TyreRubber.set_style_arc_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TyreRubber.set_style_arc_width(38, lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_TyreRubber.set_style_arc_color(lv.color_hex(0x000000), lv.PART.INDICATOR | lv.STATE.DEFAULT)
        ui_TyreRubber.set_style_arc_opa(255, lv.PART.INDICATOR | lv.STATE.DEFAULT)
        ui_TyreRubber.set_style_arc_width(38, lv.PART.INDICATOR | lv.STATE.DEFAULT)

        ui_TyreRubber.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        ui_TyreRubber.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)

        ui_TyreWheel = lv.label(self.ui_Tyre)
        ui_TyreWheel.set_text("")
        ui_TyreWheel.set_width(lv.SIZE.CONTENT)  # 1
        ui_TyreWheel.set_height(lv.SIZE.CONTENT)  # 1
        ui_TyreWheel.set_x(0)
        ui_TyreWheel.set_y(2)
        ui_TyreWheel.set_align(lv.ALIGN.CENTER)
        ui_TyreWheel.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TyreWheel.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        ui_TyreWheel.set_style_text_font(self.resourceManager.load_font("Tyre", 1), lv.PART.MAIN | lv.STATE.DEFAULT)

        self.ui_TyreLabel = lv.label(self.ui_Tyre)
        self.ui_TyreLabel.set_text("")
        self.ui_TyreLabel.set_width(lv.SIZE.CONTENT)  # 1
        self.ui_TyreLabel.set_height(lv.SIZE.CONTENT)  # 1
        self.ui_TyreLabel.set_align(lv.ALIGN.CENTER)
        self.current_color = random.choice(Tyre.colors)
        self.ui_TyreLabel.set_style_text_color(self.current_color, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_TyreLabel.set_style_text_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.ui_TyreLabel.set_style_text_font(self.resourceManager.load_font("Tyre", 1),
                                              lv.PART.MAIN | lv.STATE.DEFAULT)

        ui_TyreRim = lv.arc(self.ui_Tyre)
        ui_TyreRim.set_width(78)
        ui_TyreRim.set_height(78)
        ui_TyreRim.set_align(lv.ALIGN.CENTER)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.PRESS_LOCK, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.CLICK_FOCUSABLE, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.SNAPPABLE, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.SCROLLABLE, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.SCROLL_ELASTIC, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.SCROLL_MOMENTUM, False)
        self.SetFlag(ui_TyreRim, lv.obj.FLAG.SCROLL_CHAIN, False)
        ui_TyreRim.set_value(100)
        ui_TyreRim.set_bg_angles(0, 360)
        self.themeManager.ui_object_set_themeable_style_property(ui_TyreRim, lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.ARC_COLOR,
                                                                 Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(ui_TyreRim, lv.PART.MAIN | lv.STATE.DEFAULT,
                                                                 lv.STYLE.ARC_OPA,
                                                                 Themes.UI_THEME_COLOR_COLORTEAM)
        ui_TyreRim.set_style_arc_width(6, lv.PART.MAIN | lv.STATE.DEFAULT)

        self.themeManager.ui_object_set_themeable_style_property(ui_TyreRim, lv.PART.INDICATOR | lv.STATE.DEFAULT,
                                                                 lv.STYLE.ARC_COLOR,
                                                                 Themes.UI_THEME_COLOR_COLORTEAM)
        self.themeManager.ui_object_set_themeable_style_property(ui_TyreRim, lv.PART.INDICATOR | lv.STATE.DEFAULT,
                                                                 lv.STYLE.ARC_OPA,
                                                                 Themes.UI_THEME_COLOR_COLORTEAM)
        ui_TyreRim.set_style_arc_width(6, lv.PART.INDICATOR | lv.STATE.DEFAULT)

        ui_TyreRim.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.KNOB | lv.STATE.DEFAULT)
        ui_TyreRim.set_style_bg_opa(0, lv.PART.KNOB | lv.STATE.DEFAULT)
        #
        self.vx = random.uniform(-5, 5)  # 初始x方向速度  # 初始x方向速度
        self.vy = random.uniform(-5, 5)  # 初始x方向速度  # 初始y方向速度
        self.ax = 0  # x方向加速度
        self.ay = 0  # y方向加速度，由重力决定
        self.angle = 0  # 初始角度
        self.angular_velocity = 0  # 初始角速度
        self.set_pos(x, y)

    def changeColor(self):
        available_colors = [color for color in Tyre.colors if color.full != self.current_color.full]
        self.current_color = random.choice(available_colors)
        self.ui_TyreLabel.set_style_text_color(self.current_color, lv.PART.MAIN | lv.STATE.DEFAULT)

    def set_rotation(self, angle):
        self.angle = angle
        self.ui_Tyre.set_style_transform_pivot_x(self.radius, 0)
        self.ui_Tyre.set_style_transform_pivot_y(self.radius, 0)
        self.ui_Tyre.set_style_transform_angle(int(angle * 10), 0)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        # 将相对中心的坐标转换为屏幕坐标
        screen_x = self.center_x + x - self.radius
        screen_y = self.center_y + y - self.radius
        self.ui_Tyre.set_pos(int(screen_x), int(screen_y))

    def SetFlag(self, obj, flag, value):
        if (value):
            obj.add_flag(flag)
        else:
            obj.clear_flag(flag)
        return

    def update(self, ax, ay):
        self.ax = ax * Tyre.gravity
        self.ay = ay * Tyre.gravity
        self.vx += self.ax * dt
        self.vy += self.ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt
        distance_from_center = math.sqrt(self.x ** 2 + self.y ** 2)

        if distance_from_center + self.radius > self.scr_width / 2:
            # 碰撞点的法向量
            normal_x = self.x / distance_from_center
            normal_y = self.y / distance_from_center

            # 反射速度
            dot_product = self.vx * normal_x + self.vy * normal_y
            self.vx -= 2 * dot_product * normal_x
            self.vy -= 2 * dot_product * normal_y

            # 应用弹性系数
            self.vx *= Tyre.bounce_coefficient
            self.vy *= Tyre.bounce_coefficient

            # 确保球体在边界内
            self.x = (self.scr_radius - self.radius) * normal_x
            self.y = (self.scr_radius - self.radius) * normal_y

            # 碰撞时产生角速度
            # self.angular_velocity = (self.vx + self.vy) * 5  # 调整角速度系数
            # 更新角度和旋转
            # self.angle += self.angular_velocity * dt
            # self.set_rotation(self.angle)

        # 摩擦力减速
        self.vx *= (1 - Tyre.friction_coefficient)
        self.vy *= (1 - Tyre.friction_coefficient)
        self.set_pos(self.x, self.y)


class TyreScreen(Screen):
    def __init__(self):
        super().__init__()
        self.SetFlag(self.screen, lv.obj.FLAG.SCROLLABLE, False)
        self.screen.set_style_bg_color(lv.color_hex(0x550161), lv.PART.MAIN | lv.STATE.DEFAULT)


        self.tyre = Tyre(self.screen, 0, 0)
        self.qmi8658 = None
        self.checkmiuTimer = None
        self.screen.add_event_cb(self.TyreScreen_eventhandler, lv.EVENT.ALL, None)

    def TyreScreen_eventhandler(self, event_struct):
        event = event_struct.code
        if event == lv.EVENT.SCREEN_LOADED:
            self.qmi8658 = QMI8658()
            self.checkmiuTimer = lv.timer_create(self.timer_callback, int(dt * 1000), None)
        if event == lv.EVENT.SCREEN_UNLOADED:
            lv.timer_del(self.checkmiuTimer)
            self.qmi8658.Close()
        if event == lv.EVENT.LONG_PRESSED:
            self.tyre.changeColor()

    def timer_callback(self, timer):
        ay, ax, az, gyro_x, gyro_y, gyro_z = self.qmi8658.Read_XYZ()
        self.tyre.update(ax, -ay)
        lv.refr_now(None)

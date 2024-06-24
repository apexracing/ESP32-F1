import math
import random
from common.display_driver import DisplayDriver
import lvgl as lv
import time
from lib.qmi_8658 import QMI8658

# 初始化 LVGL
lv.init()

# 初始化显示驱动
display = DisplayDriver()
display.backlight_on()
qmi8658=QMI8658()

# 创建一个屏幕对象
scr = lv.obj()
scr.set_style_bg_color(lv.color_hex(0x000000), 0)  # 设置屏幕背景为黑色

# 屏幕尺寸
scr_width = scr.get_width()
scr_height = scr.get_height()
# 圆形屏幕中心点和半径
screen_center_x = scr_width // 2
screen_center_y = scr_height // 2
screen_radius = min(scr_width, scr_height) // 2
# 定义物理属性
gravity = 9.8*300  # 重力加速度（m/s^2）
friction_coefficient = 0.01  # 摩擦系数
bounce_coefficient = 0.95  # 碰撞后的弹性系数
angle_friction = 0.98  # 角速度摩擦系数
# 时间步长（秒）
dt = 0.02
class LowPassFilter:
    def __init__(self, alpha):
        self.alpha = alpha
        self.filtered_value = 0

    def apply(self, value):
        self.filtered_value = self.alpha * value + (1 - self.alpha) * self.filtered_value
        return self.filtered_value
class Circle:
    def __init__(self, screen, x, y, radius, mass):
        self.obj = lv.obj(screen)
        self.obj.set_size(radius * 2, radius * 2)
        self.obj.set_style_radius(lv.RADIUS.CIRCLE, 0)
        self.obj.set_style_bg_color(lv.color_hex(0xFF0000), 0)
        ui_CenterMsg = lv.label(self.obj)
        ui_CenterMsg.set_text("5")
        ui_CenterMsg.set_width(lv.SIZE.CONTENT)  # 1
        ui_CenterMsg.set_height(lv.SIZE.CONTENT)  # 1
        ui_CenterMsg.set_align(lv.ALIGN.CENTER)
        # 将相对中心的坐标转换为屏幕坐标
        self.center_x = scr_width // 2
        self.center_y = scr_height // 2
        self.radius = radius
        self.mass = mass
        self.vx =  random.uniform(-5, 5)  # 初始x方向速度  # 初始x方向速度
        self.vy =  random.uniform(-5, 5)  # 初始x方向速度  # 初始y方向速度
        self.ax = 0  # x方向加速度
        self.ay = 0  # y方向加速度，由重力决定
        self.angle = 0  # 初始角度
        self.angular_velocity = 0  # 初始角速度
        self.set_pos(x, y)
    def set_rotation(self, angle):
        self.angle = angle
        self.obj.set_style_transform_pivot_x(self.radius,0)
        self.obj.set_style_transform_pivot_y(self.radius,0)
        self.obj.set_style_transform_angle(int(angle * 10), 0)
    def set_pos(self, x, y):
        self.x = x
        self.y = y
        # 将相对中心的坐标转换为屏幕坐标
        screen_x = self.center_x + x - self.radius
        screen_y = self.center_y + y - self.radius
        self.obj.set_pos(int(screen_x), int(screen_y))

    def update(self,ax,ay):
        self.ax=ax*gravity
        self.ay=ay*gravity
        self.vx += self.ax * dt
        self.vy += self.ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        distance_from_center = math.sqrt(self.x ** 2 + self.y ** 2)

        if distance_from_center + self.radius > scr_width / 2:
            # 碰撞点的法向量
            normal_x = self.x / distance_from_center
            normal_y = self.y / distance_from_center

            # 反射速度
            dot_product = self.vx * normal_x + self.vy * normal_y
            self.vx -= 2 * dot_product * normal_x
            self.vy -= 2 * dot_product * normal_y

            # 应用弹性系数
            self.vx *= bounce_coefficient
            self.vy *= bounce_coefficient

            # 确保球体在边界内
            self.x = (screen_radius - self.radius) * normal_x
            self.y = (screen_radius - self.radius) * normal_y
            
            # 碰撞时产生角速度
            #self.angular_velocity = (self.vx + self.vy) * 5  # 调整角速度系数
            # 更新角度和旋转
            #self.angle += self.angular_velocity * dt
            #self.set_rotation(self.angle)

        # 摩擦力减速
        self.vx *= (1 - friction_coefficient)
        self.vy *= (1 - friction_coefficient)
        self.set_pos(self.x, self.y)

        
# 创建多个圆形对象
circle = Circle(scr, 0, 0, 75, 1)

# 更新位置并检测碰撞
def update(timer):
    ay, ax,az, gyro_x, gyro_y, gyro_z = qmi8658.Read_XYZ()
    circle.update(ax, -ay)


# 创建一个定时器，每 20 毫秒更新一次圆形位置
lv.timer_create(update, int(dt * 1000), None)

# 加载屏幕
lv.scr_load(scr)

# 主循环
while True:
    lv.task_handler()
    time.sleep(0.005)
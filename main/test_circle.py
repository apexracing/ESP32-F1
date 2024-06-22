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
gravity = 9.8*100  # 重力加速度（像素/s^2）
friction = 1 # 摩擦系数
elasticity = 0.8  # 弹性系数
air_resistance = 1  # 空气阻力系数
dt = 0.02  # 时间步长（秒）
acc_threshold = 0.02  # 加速度变化阈值
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
        self.angular_acceleration = 0  # 初始角加速度
        self.set_pos(x, y)
    def set_rotation(self, angle):
        self.angle = angle
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
        self.vx *= air_resistance * friction
        self.vy *= air_resistance * friction

        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt

        distance_from_center = math.sqrt(new_x ** 2 + new_y ** 2)

        if distance_from_center + self.radius > scr_width / 2:
            # 如果超出边界，调整位置和速度
            overlap = distance_from_center + self.radius - screen_radius
            angle = math.atan2(new_y, new_x)
            new_x -= overlap * math.cos(angle)
            new_y -= overlap * math.sin(angle)
            self.vx = -self.vx * elasticity
            self.vy = -self.vy * elasticity
            # 额外的加速度分量，模拟滚动到最低点
            self.ax += math.cos(distance_from_center) * gravity * dt
            self.ay += math.sin(distance_from_center) * gravity * dt
            # 计算力矩和角加速度
            torque = self.radius * (self.ax * math.sin(distance_from_center) - self.ay * math.cos(distance_from_center))
            moment_of_inertia = 0.5 * self.mass * self.radius ** 2  # 圆形的转动惯量
            self.angular_acceleration = torque / moment_of_inertia

        # 更新角速度和角度
        self.angular_velocity += self.angular_acceleration * dt
        self.angular_velocity *= air_resistance  # 模拟空气阻力对角速度的影响
        self.angle += self.angular_velocity * dt
        self.set_pos(new_x, new_y)
        #self.set_rotation(self.angle)

   

# 创建多个圆形对象
circle = Circle(scr, 0, 0, 50, 1)

# 更新位置并检测碰撞
def update(timer):
    ay, ax,az, gyro_x, gyro_y, gyro_z = qmi8658.Read_XYZ()
    if abs(ax)>1:
        print(f'ax={ax}')
    if abs(ay)>1:
        print(f'ay={ay}')
    if abs(az)>1:
        print(f'az={az}')
    circle.update(ax, -ay)


# 创建一个定时器，每 20 毫秒更新一次圆形位置
lv.timer_create(update, int(dt * 1000), None)

# 加载屏幕
lv.scr_load(scr)

# 主循环
while True:
    lv.task_handler()
    time.sleep(0.005)
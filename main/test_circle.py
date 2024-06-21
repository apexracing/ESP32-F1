import math
import random
from common.display_driver import DisplayDriver
import lvgl as lv
import time
# 初始化 LVGL
lv.init()

# 初始化显示驱动
display = DisplayDriver()
display.backlight_on()
# 创建一个屏幕对象
scr = lv.obj()
scr.set_style_bg_color(lv.color_hex(0x000000), 0)  # 设置屏幕背景为黑色

# 屏幕尺寸
scr_width = scr.get_width()
scr_height = scr.get_height()

# 定义物理属性
gravity = 9.8*100  # 重力加速度（像素/s^2）
friction = 0.98  # 摩擦系数
elasticity = 0.7  # 弹性系数
air_resistance = 0.99  # 空气阻力系数
dt = 0.02  # 时间步长（秒）
velocity_threshold = 0.1  # 速度阈值
collision_threshold = 0.5  # 碰撞后速度阈值

class Circle:
    def __init__(self, screen, x, y, radius, mass):
        self.obj = lv.obj(screen)
        self.obj.set_size(radius * 2, radius * 2)
        self.obj.set_style_radius(lv.RADIUS.CIRCLE, 0)
        self.obj.set_style_bg_color(lv.color_hex(0xFF0000), 0)
        # 将相对中心的坐标转换为屏幕坐标
        self.center_x = scr_width // 2
        self.center_y = scr_height // 2
        self.radius = radius
        self.mass = mass
        self.vx = 0  # 初始x方向速度
        self.vy = 0  # 初始y方向速度
        self.ax = 0  # x方向加速度
        self.ay = gravity  # y方向加速度，由重力决定
        self.set_pos(x, y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        # 将相对中心的坐标转换为屏幕坐标
        screen_x = self.center_x + x - self.radius
        screen_y = self.center_y + y - self.radius
        self.obj.set_pos(int(screen_x), int(screen_y))

    def update(self):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.vx *= air_resistance * friction
        self.vy *= air_resistance * friction

        # 如果速度低于阈值，则将速度设为0
        if abs(self.vx) < velocity_threshold:
            self.vx = 0
        if abs(self.vy) < velocity_threshold:
            self.vy = 0

        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt

        distance_from_center = math.sqrt(new_x ** 2 + new_y ** 2)

        if distance_from_center + self.radius > scr_width / 2:
            angle = math.atan2(new_y, new_x)
            self.vx = -self.vx * elasticity
            self.vy = -self.vy * elasticity
            new_x = (scr_width / 2 - self.radius) * math.cos(angle)
            new_y = (scr_width / 2 - self.radius) * math.sin(angle)

        self.set_pos(new_x, new_y)

    def collide_with(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < self.radius + other.radius:
            angle = math.atan2(dy, dx)
            total_mass = self.mass + other.mass

            overlap = 0.5 * (self.radius + other.radius - distance)
            self.set_pos(self.x + overlap * math.cos(angle), self.y + overlap * math.sin(angle))
            other.set_pos(other.x - overlap * math.cos(angle), other.y - overlap * math.sin(angle))

            normal_x = dx / distance
            normal_y = dy / distance

            relative_velocity_x = self.vx - other.vx
            relative_velocity_y = self.vy - other.vy

            dot_product = (relative_velocity_x * normal_x + relative_velocity_y * normal_y)

            self.vx -= (2 * other.mass / total_mass) * dot_product * normal_x * elasticity
            self.vy -= (2 * other.mass / total_mass) * dot_product * normal_y * elasticity

            other.vx += (2 * self.mass / total_mass) * dot_product * normal_x * elasticity
            other.vy += (2 * self.mass / total_mass) * dot_product * normal_y * elasticity

            # 引入随机角度调整
            angle_variation = math.radians(random.uniform(-5, 5))  # 随机角度在 -5 到 5 度之间
            cos_variation = math.cos(angle_variation)
            sin_variation = math.sin(angle_variation)

            self.vx = self.vx * cos_variation - self.vy * sin_variation
            self.vy = self.vx * sin_variation + self.vy * cos_variation

            other.vx = other.vx * cos_variation - other.vy * sin_variation
            other.vy = other.vx * sin_variation + other.vy * cos_variation

            # 如果碰撞后的速度低于阈值，则将速度设为0，避免抖动
            if abs(self.vx) < collision_threshold:
                self.vx = 0
            if abs(self.vy) < collision_threshold:
                self.vy = 0
            if abs(other.vx) < collision_threshold:
                other.vx = 0
            if abs(other.vy) < collision_threshold:
                other.vy = 0

# 创建多个圆形对象
circles = [Circle(scr, 0, 0, 30, 1.0),Circle(scr, 0, -70, 30, 1.0),Circle(scr, 70, 70, 30, 1.0)]
print("aaa")

# 更新位置并检测碰撞
def update(timer):
    for i, circle in enumerate(circles):
        circle.update()
        for j in range(i + 1, len(circles)):
            circle.collide_with(circles[j])

# 创建一个定时器，每 20 毫秒更新一次圆形位置
lv.timer_create(update, int(dt * 1000), None)

# 加载屏幕
lv.scr_load(scr)

# 主循环
while True:
    lv.task_handler()
    time.sleep(0.005)
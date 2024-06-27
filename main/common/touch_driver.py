import lvgl as lv
from lib import cst816

def singleton(cls):
    instance = None
    def getinstance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance
    return getinstance
@singleton
class TouchDriver:
	def __init__(self):
		self.cst816 = cst816.CST816()
		if self.cst816.who_am_i():
			print("CST816 触摸输入驱动已侦测.")
		else:
			print("CST816 未侦测.")
		indev_drv = lv.indev_drv_t()
		indev_drv.init()
		indev_drv.type=lv.INDEV_TYPE.POINTER
		indev_drv.read_cb = self.read_cb
		# 注册驱动
		indev_drv.register()


	def read_cb(self,drv, data):
		if self.cst816.get_touch():
			data.state=lv.INDEV_STATE.PRESSED
		else:
			data.state=lv.INDEV_STATE.RELEASED
		point = self.cst816.get_point()
		data.point.x = point.x_point
		data.point.y = point.y_point
		return False

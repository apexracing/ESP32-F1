import lvgl as lv
import cst816
class TouchDriver:
	def __init__(self):
		self.cst816 = cst816.CST816()
		if self.cst816.who_am_i():
		    print("CST816 detected.")
		else:
		    print("CST816 not detected.")
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

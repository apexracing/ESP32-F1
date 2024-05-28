import _thread

class ThreadQueue:
	def __init__(self):
		self.queue=[]
		self.lock=_thread.allocate_lock()

	def put(self,item):
		with self.lock:
			self.queue.append(item)
	def get(self)
		with self.lock:
			 if len(self.queue) == 0:
			 	return None
			 return self.queue.pop(0)

	def task_done(self):
		pass

	def join(self):
		pass
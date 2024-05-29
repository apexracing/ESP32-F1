import _thread
from time import sleep
from thread_queue import ThreadQueue
class ThreadPool:
	def __init__(self,num_thread):
		self.tasks=ThreadQueue()
		self.threads=[]
		self.num_thread=num_thread
		for _ in range(self.num_threads):
            t = _thread.start_new_thread(self.worker, ())
            self.threads.append(t)
	def add_task(self,func,*args,**kwargs):
		self.tasks.append((func,args,kwargs))

	def worker(self):
		while True:
			task=self.tasks.get()
			if task is None:
				time.sleep_ms(10)
				continue
			try:
				func,args,kwargs=task
				func(*args,**kwargs)
			except Exception as e:
				print("Thread error:",e)
			self.tasks.task_done()



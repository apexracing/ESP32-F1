from lib.qmi_8658 import QMI8658
import time
import gc
qmi8658=QMI8658()
del qmi8658
gc.collect()
while True:
    
    time.sleep(0.1)

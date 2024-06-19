from lib.qmi_8658 import QMI8658
import time
import gc
qmi8658=QMI8658()
qmi86582=QMI8658()
print(qmi86582)
while True:
    gc.collect()
    time.sleep(0.1)

from lib.qmi_8658 import QMI8658
import time
import gc
qmi8658=QMI8658()
del qmi8658
gc.collect()
while True:
    _, _, _, gyro_x, gyro_y, gyro_z = qmi8658.Read_Raw_XYZ()
    if abs(gyro_z) > 25000:
        if gyro_z > 0:
            print("右转")
        else:
            print("左转")
    if abs(gyro_y) > 25000:
        if gyro_y > 0:
            print("前滚")
        else:
            print("后滚")
    if abs(gyro_x) > 25000:
        if gyro_x > 0:
            print("左倾斜")
        else:
            print("右倾斜")
    time.sleep(0.1)

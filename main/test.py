from lib.qmi_8658 import QMI8658

qimi8658=QMI8658()
while True:
    data=qimi8658.Read_XYZ()
    print(data)

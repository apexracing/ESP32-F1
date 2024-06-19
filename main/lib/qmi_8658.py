from machine import Pin, I2C, SPI, PWM, Timer, ADC
I2C_SDA = 6
I2C_SDL = 7
I2C_INT = 17
I2C_RST = 16
class QMI8658(object):
    def __init__(self, address=0x6B):
        self._address = address
        self._bus = I2C(id=1, scl=Pin(I2C_SDL), sda=Pin(I2C_SDA), freq=400000,timeout=50000)
        bRet = self.WhoAmI()
        if bRet:
            self.Read_Revision()
        else:
            return NULL
        self.Config_apply()

    def _read_byte(self, cmd):
        rec = self._bus.readfrom_mem(int(self._address), int(cmd), 1)
        return rec[0]

    def _read_block(self, reg, length=1):
        rec = self._bus.readfrom_mem(int(self._address), int(reg), length)
        return rec

    def _read_u16(self, cmd):
        LSB = self._bus.readfrom_mem(int(self._address), int(cmd), 1)
        MSB = self._bus.readfrom_mem(int(self._address), int(cmd) + 1, 1)
        return (MSB[0] << 8) + LSB[0]

    def _write_byte(self, cmd, val):
        self._bus.writeto_mem(int(self._address), int(cmd), bytes([int(val)]))

    def WhoAmI(self):
        bRet = False
        if (0x05) == self._read_byte(0x00):
            bRet = True
        return bRet

    def Read_Revision(self):
        return self._read_byte(0x01)

    def Config_apply(self):
        # REG CTRL1
        self._write_byte(0x02, 0x60)
        # REG CTRL2 : QMI8658AccRange_8g  and QMI8658AccOdr_1000Hz
        self._write_byte(0x03, 0x20)
        # REG CTRL3 : QMI8658GyrRange_512dps and QMI8658GyrOdr_1000Hz
        self._write_byte(0x04, 0x50)
        # REG CTRL4 : No
        self._write_byte(0x05, 0x00)
        # REG CTRL5 : Enable Gyroscope And Accelerometer Low-Pass Filter
        self._write_byte(0x06, 0x11)
        # REG CTRL6 : AttitudeEngine ODR. 64hz MoD off
        self._write_byte(0x07, 0x06)
        # REG CTRL7 : Enable Gyroscope And Accelerometer/AttitudeEngine
        self._write_byte(0x08, 0x4B)

    def Read_Raw_Quat(self):
        print(" ")
        wxyz = [1, 0, 0, 0]
        self._write_byte(0x0A, 0x0C)
        raw_timestamp = self._read_block(0x30, 3)
        quat = self._read_block(0x45, 8)
        print("quat: ")
        print(quat)
        status = self._read_block(0x2F, 1)
        print("status: ")
        print(status)
        timestamp = (
            (raw_timestamp[2] << 16) | (raw_timestamp[1] << 8) | (raw_timestamp[0])
        )
        print("Timestamp: ")
        print(timestamp)
        #temp = self._read_byte(0x33)
        #print("temp")
        #print(temp)
        for i in range(3):
            wxyz[i] = (wxyz[(i) + 1]) | (wxyz[i])
        print(wxyz)
        return wxyz

    def Read_Raw_XYZ(self):
        xyz = [0, 0, 0, 0, 0, 0]
        raw_timestamp = self._read_block(0x30, 3)
        raw_acc_xyz = self._read_block(0x35, 6)
        raw_gyro_xyz = self._read_block(0x3B, 6)
        raw_xyz = self._read_block(0x35, 12)
        timestamp = (
            (raw_timestamp[2] << 16) | (raw_timestamp[1] << 8) | (raw_timestamp[0])
        )
        for i in range(6):
            # xyz[i]=(raw_acc_xyz[(i*2)+1]<<8)|(raw_acc_xyz[i*2])
            # xyz[i+3]=(raw_gyro_xyz[((i+3)*2)+1]<<8)|(raw_gyro_xyz[(i+3)*2])
            xyz[i] = (raw_xyz[(i * 2) + 1] << 8) | (raw_xyz[i * 2])
            if xyz[i] >= 32767:
                xyz[i] = xyz[i] - 65535
        return xyz

    def Read_XYZ(self):
        xyz = [0, 0, 0, 0, 0, 0]
        raw_xyz = self.Read_Raw_XYZ()
        # QMI8658AccRange_8g
        acc_lsb_div = 1 << 12
        # QMI8658GyrRange_512dps
        gyro_lsb_div = 64
        for i in range(3):
            xyz[i] = raw_xyz[i] / acc_lsb_div  # (acc_lsb_div/1000.0)
            xyz[i + 3] = raw_xyz[i + 3] * 1.0 / gyro_lsb_div
        return xyz


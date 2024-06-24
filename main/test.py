from common.wifi import *

if __name__ == '__main__':
    startAP(essid='F1-LiveTime', hostname="speedim.cn")
    while True:
        time.sleep(0.01)

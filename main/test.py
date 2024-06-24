from common.wifi import *

if __name__ == '__main__':
    if is_wifi_connect() is False and wifi_auto_connect() is False:
        # 开启配网模式
        start_ap(essid='F1-LiveTime', hostname="speedim.cn")
    while True:
        time.sleep(0.01)

import network
import time
import json
import espidf as esp32
import uasyncio as asyncio

wifi_data = {}
wifi = network.WLAN(network.STA_IF)
ap = None


def start_ap(essid="esp32", hostname=None, ip='192.168.1.1'):
    '''
    开启热点，默认网关地址:192.168.1.1;并启用一个域名解析地址
    :return:
    '''
    global ap
    ap = network.WLAN(network.AP_IF)  # create access-point interface
    ap.active(False)
    time.sleep(1)
    ap.active(True)  # activate the interface
    ap.config(essid=essid, password="12345678",authmode=network.AUTH_WPA_WPA2_PSK)  # set the SSID of the access point
    ap.ifconfig((ip, '255.255.255.0', ip, ip))
    print(f'开启WIFI热点:{ap.ifconfig()}')


async def connect_wifi(ssid: str, password: str, callback=None, try_num: int = 5):
    '''
    连接到WIFI
    :param ssid: wifi ssid
    :param password: 密码
    :param try_num 最多偿试几次
    :return:
    '''
    print('正在连接wifi')
    global wifi
    wifi.active(True)  # activate the interface
    wifi.disconnect()
    wifi.connect(ssid, password)  # connect to an AP
    # 等待几秒，要不然isconnected 一直是false
    num: int = 1
    while not wifi.isconnected() and num < try_num:
        wifi.active(True)
        wifi.disconnect()
        if callback is not None:
            callback(f"正在第{num}次尝试,连接到Wi-Fi:{ssid}", 0)
        wifi.connect(ssid, password)
        await asyncio.sleep_ms(3000)
        num += 1
    if wifi.isconnected():
        if callback is not None:
            callback(f"已成功连接到Wi-Fi:{ssid}", 1, ssid, password)
        print(f'已连接WIFI:{ssid},IPV4 地址:{wifi.ifconfig()}')  # get the interface's IP/netmask/gw/DNS addresses
    else:
        if callback is not None:
            callback(f"连接到Wi-Fi:{ssid},失败.", 2)
    return wifi.isconnected()


def wifi_cfg_flush():
    global wifi_data
    with open("wifi.cfg", "w+", encoding="utf-8") as f:
        f.write(json.dumps(wifi_data))
        print(f"保存Wifi密码{json.dumps(wifi_data)}")


def wifi_cfg_load():
    try:
        with open("wifi.cfg", "r+", encoding="UTF-8") as f:
            global wifi_data
            wifi_data = json.loads(f.read())
            print(f"加载Wifi密码{wifi_data}")

    except:
        wifi_cfg_flush()


def wifi_scan():
    wifi.active(True)
    wifi.disconnect()
    return wifi.scan()


async def wifi_auto_connect():
    global wifi
    '''
    从已保存的ssid,password中自动连接到一个可用的网络
    :return: 返回True or False
    '''
    result = False
    wifi_cfg_load()
    wifi.active(True)  # activate the interface
    wifi.disconnect()
    wifiList = wifi.scan()
    # 描述出来的结果已经是按信号强度排序过
    # sorted_networks = sorted(wifiList, key=lambda x: x[3], reverse=True)
    for (ssid, _, _, rssi, _, _) in wifiList:
        ssid = ssid.decode("UTF-8")
        if ssid in wifi_data:
            result = await connect_wifi(ssid, wifi_data[ssid])
            break
    return result


def is_wifi_connect():
    '''
    :return: 当前wifi连接状态
    '''
    global wifi
    if wifi is not None and wifi.isconnected():
        return True
    return False


def get_wifi_strength_level(rssi):
    '''
    返回wifi信号强度，wifi信号强度图标一般有3格
    :param rssi: wifi信号:dBm
    :return: 3:强，2: 中，1:弱
    '''
    if rssi > -50:
        return 3
    elif rssi > -70:
        return 2
    else:
        return 1


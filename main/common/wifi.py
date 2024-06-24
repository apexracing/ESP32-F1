import network
import time
import json

wifi_data = {}
wifi = None


def start_ap(essid="esp32", hostname=None):
    '''
    开启热点，默认网关地址:192.168.1.1;并启用一个域名解析地址
    :return:
    '''
    ap = network.WLAN(network.AP_IF)  # create access-point interface
    ap.active(False)
    time.sleep(1)
    ap.active(True)  # activate the interface
    ap.config(essid=essid, authmode=network.AUTH_OPEN)  # set the SSID of the access point
    ap.ifconfig(('192.168.1.1', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
    # 设置DNS服务器
    if hostname:
        ap.config(dhcp_hostname=hostname)  # 设置主机名
    print(f'开启WIFI热点:{ap.ifconfig()}')


def connect_wifi(ssid, password, try_num=5):
    '''
    连接到WIFI
    :param ssid: wifi ssid
    :param password: 密码
    :param try_num 最多偿试几次
    :return:
    '''
    global wifi
    wifi = network.WLAN(network.STA_IF)  # create station interface
    wifi.active(True)  # activate the interface
    wifi.disconnect()
    wifi.connect(ssid, password)  # connect to an AP
    # 等待几秒，要不然isconnected 一直是false
    while not wifi.isconnected() and try_num > 0:
        wifi.active(True)
        wifi.disconnect()
        wifi.connect(ssid, password)
        time.sleep(5)
        try_num -= 1
    if wifi.isconnected():
        print(f'已连接WIFI:{ssid},IPV4 地址:{wifi.ifconfig()}')  # get the interface's IP/netmask/gw/DNS addresses
    return wifi.isconnected()


def wifi_cfg_flush():
    with open("wifi.cfg", "w+", encoding="utf-8") as f:
        f.write(json.dumps(wifi_data))


def wifi_cfg_load():
    try:
        global wifi_data
        with open("wifi.cfg", "rw+", encoding="UTF-8") as f:
            wifi_data = json.loads(f.read())
    except:
        wifi_cfg_flush()


def wifi_auto_connect():
    global wifi
    '''
    从已保存的ssid,password中自动连接到一个可用的网络
    :return: 返回True or False
    '''
    result = False
    wifi_cfg_load()
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)  # activate the interface
    wifi.disconnect()
    wifiList = wifi.scan()
    # 描述出来的结果已经是按信号强度排序过
    # sorted_networks = sorted(wifiList, key=lambda x: x[3], reverse=True)
    for (ssid, _, _, rssi, _, _) in wifiList:
        ssid = ssid.decode("UTF-8")
        print(f"ssid->{ssid} 信号强度: {get_wifi_strength_level(rssi)}")
        if wifi_data.get(ssid) is not None:
            result = connect_wifi(ssid, wifi_data[ssid])
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

from lib.microdot import Microdot
import network
import time


def startAP(essid="esp32", hostname=None):
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


def connectWiFi(ssid, password):
    '''
    连接到WIFI
    :param ssid: wifi ssid
    :param password: 密码
    :return:
    '''
    wlan = network.WLAN(network.STA_IF)  # create station interface
    wlan.active(True)  # activate the interface
    wlan.disconnect()
    wlan.connect(ssid, password)  # connect to an AP
    time.sleep(5)  # 等待几秒，要不然isconnected 一直是false
    if wlan.isconnected():
        print(f'已连接WIFI:{ssid},IPV4 地址:{wlan.ifconfig()}')  # get the interface's IP/netmask/gw/DNS addresses
    return wlan.isconnected()

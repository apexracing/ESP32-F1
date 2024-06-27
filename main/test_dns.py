from lib.dns import DNSServer
import uasyncio as asyncio
from common.wifi import *
dns_records = {
    "speedim.cn": {
        "A": "192.168.1.1",
        "CNAME": "wifi.speedim.cn"
    },
    "wifi.speedim.cn": {
        "A": "192.168.1.1"
    },
    "*": {
        "A": "192.168.1.1"
    }
}
start_ap(essid='F1-LiveTime', hostname="speedim.cn")
dns = DNSServer(dns_records)
asyncio.run(dns.run())
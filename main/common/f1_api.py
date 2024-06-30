from lib import urequests
from common.time_driver import TimeDriver

F1_API_HOST_BASE = "https://gitee.com/apexracing/f1livetime/raw/master"

class F1Api:
    def __init__(self):
        self.timeDriver=TimeDriver()
    def get_events(self,year=None):
        '''

        :param year: 从2024年开始的事件
        :return:
        '''
        if year is None:

            year,*_=self.timeDriver.get_utc_time()
        try:
            response = urequests.get(f"{F1_API_HOST_BASE}/f1_{year}.json")
            events = response.json()
            response.close()
        except Exception as e:
            return []

        return events["races"]

    def get_eventing(self):
        '''
        :return: 尽可能返回当前进行中的事件，如果没有，返回下一个事件
        '''
        events = self.get_events()
        for event in events:
            sessions = event["sessions"]
            for session in sessions.keys():
                start_time = sessions[session]
        return None
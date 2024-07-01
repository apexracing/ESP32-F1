from lib import urequests as requests
from common.time_driver import TimeDriver
from common.singleton import singleton

F1_API_HOST_BASE = "https://gitee.com/apexracing/f1livetime/raw/master"
'''
根据FIA规则，比赛最长时间
Sprint 1小时,意外最长1.5小时
Race   2小时,意外最长3小时
其它按常规时间结束
'''
SESSION_PERIOD = {"Sprint": 5400, "Race": 10800, "Qualifying": 3600, "Sprint Qualifying": 2700, "Practice 1": 3600, "Practice 2": 3600, "Practice 3": 3600, }


@singleton
class F1Api:
    def __init__(self):
        print("F1 API inited!")
        self.timeDriver = TimeDriver()
        self.events = self.get_events()

    def update_events(self):
        self.events = self.get_events()

    def get_events(self, year=None):
        if year is None:
            year, *_ = self.timeDriver.get_utc_time()
        response = requests.get(f"https://gitee.com/apexracing/f1livetime/raw/master/f1_{year}.json")
        data = response.json()
        response.close()
        events = []
        rounds = sorted(data["round_number"].values())
        for _id in rounds:
            _id=str(_id)
            event = {"event_name": data["event_name"][_id], "event_date": data["event_date"][_id], "country": data["country"][_id], "location": data["location"][_id], "sessions": []}
            for key in sorted(data.keys()):
                if "session" in key and "date" not in key:
                    session_name = data[key][_id]
                    if session_name is not None:
                        session_date = data[key + "_date"][_id]
                        session_utc_second = self.timeDriver.iso8610_to_unixtime(session_date)
                        session_end_utc_second = session_utc_second + SESSION_PERIOD[session_name]
                        event["sessions"].append({"session_name": session_name, "session_date": session_date, "session_begin_utc": session_utc_second, "session_end_utc": session_end_utc_second})
            events.append(event)
        return events

    def get_eventing(self):
        '''
        返回当前正在进行的比赛，如果没有，返回下一场比赛
        :return:
        '''
        now_utc_second = self.timeDriver.get_unixtime()
        for event in self.events:
            for session in event["sessions"]:
                session_begin_second = session["session_begin_utc"]
                session_end_utc_second = session["session_end_utc"]
                if session_begin_second <= now_utc_second < session_end_utc_second:
                    return event["event_name"], session, "Racing"
                if now_utc_second < session_begin_second:
                    return event["event_name"], session, "UpComing"
        return None

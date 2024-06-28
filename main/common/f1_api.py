from lib import urequests
from time_driver import TimeDriver

F1_API_HOST_BASE = "https://gitee.com/apexracing/f1livetime/raw/master"


def get_f1_events(year):
    try:
        response = urequests.get(f"{F1_API_HOST_BASE}/f1_{year}.json")
        events = response.json()
        response.close()
    except Exception as e:
        return []

    return events["races"]


def get_f1_current_next_event():
    events = get_f1_events()
    for event in events:
        sessions=event["sessions"]
        for session in  sessions.keys():
            start_time=sessions[session]



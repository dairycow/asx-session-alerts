from datetime import datetime, time
from zoneinfo import ZoneInfo

from alerts import send_alert

CST = ZoneInfo("Asia/Shanghai")

ASIA_EVENTS = [
    {
        "time": time(9, 0),
        "label": "0900 China Futures market open",
        "context": "Watch: Iron Ore (DCE), Copper & Steel (SHFE), Lithium & Silicon (GFEX)",
    },
    {
        "time": time(9, 30),
        "label": "0930 HKEX & SSE market open",
        "context": "Watch: HSI, A-shares sentiment, China demand signals",
    },
    {
        "time": time(11, 30),
        "label": "1130 China Futures & SSE morning close",
        "context": "Morning commodity prices settling — Iron Ore, Copper, Lithium midday reference",
    },
    {
        "time": time(12, 0),
        "label": "1200 HKEX morning close",
        "context": "Hang Seng morning session done. Note any divergence from A-shares.",
    },
    {
        "time": time(13, 0),
        "label": "1300 HKEX & SSE afternoon open",
        "context": "Afternoon equity session resuming. Watch for momentum shifts from the morning.",
    },
    {
        "time": time(13, 30),
        "label": "1330 China Futures afternoon open",
        "context": "Afternoon commodity session — Iron Ore, Copper, Lithium resuming",
    },
    {
        "time": time(15, 0),
        "label": "1500 SSE & China Futures market closed",
        "context": "China equity and commodity markets closed for the day. Final prices set.",
    },
    {
        "time": time(16, 0),
        "label": "1600 HKEX market closed",
        "context": "Last major Asian market closed. Shift focus to US pre-market.",
    },
]


def get_active_event(now: datetime):
    for event in ASIA_EVENTS:
        if now.time() == event["time"]:
            return event
    return None


def tick():
    now = datetime.now(CST)
    if now.weekday() >= 5:
        return
    event = get_active_event(now)
    if event:
        message = f"**{event['label']}**\n> {event['context']}"
        send_alert(message)
        print(f"[{now} CST] Alert sent: {event['label']}")

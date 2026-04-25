import random
from datetime import datetime, time
from zoneinfo import ZoneInfo

from alerts import send_alert

AEST = ZoneInfo("Australia/Sydney")

SESSIONS = [
    {"name": "Morning A", "end": time(11, 30)},
    {"name": "Morning B", "end": time(12, 30)},
    {"name": "Lunchtime", "end": time(13, 30)},
    {"name": "Afternoon A", "end": time(15, 0)},
    {"name": "Afternoon B", "end": time(16, 0)},
]

JOURNAL_PROMPTS = [
    "Did you wait for the setup, or did you force an entry? Be honest.",
    "Was your thesis written before you entered, or did you justify after the fact?",
    "Did you cut at the stop — not near it, not past it — exactly at it?",
    "Score your process adherence this session out of 6: thesis written, checklist met, stop placed, stop not moved, exited at stop/target, size from stop calculation.",
    "What's your current phase, and did you only trade setups allowed in that phase?",
    "Did you hit your daily loss limit (2%)? If so, are you done for the day?",
    "Was there a FOMO entry? A stock already past your level that you chased anyway?",
    "After your last loss, did you wait 30 min before considering a new entry — or did revenge creep in?",
    "Did you calculate your numbers before the order — entry, stop, size, dollar risk, target?",
    "No trade is also a trade. If nothing triggered, did you sit on your hands or force something?",
    "What was your emotional state this session — calm, anxious, FOMO, revenge, bored, focused?",
    "Which playbook principle did you execute best this session?",
]

_last_alerted: dict[str, str] = {}


def tick():
    now = datetime.now(AEST)
    if now.weekday() >= 5:
        return
    key = now.strftime("%Y-%m-%d %H:%M")
    for session in SESSIONS:
        session_key = f"{key} {session['name']}"
        if session["end"].hour == now.hour and session["end"].minute == now.minute:
            if session_key not in _last_alerted:
                _last_alerted[session_key] = key
                prompt = random.choice(JOURNAL_PROMPTS)
                message = (
                    f"**{session['name']} session has ended!**\n\n"
                    f":pencil: *{prompt}*"
                )
                send_alert(message)
                print(f"[{now}] Alert sent for {session['name']}")

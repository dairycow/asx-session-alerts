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
    "Rate your trading so far. What went well? What didn't?",
    "Did you follow your trading plan this session?",
    "What was your best trade this session and why?",
    "What emotion did you feel most during this session?",
    "Did you manage your risk well? What would you change?",
    "Write one thing you learned from this session.",
    "How disciplined were you with your entry/exit rules?",
    "What setup are you watching for next session?",
    "Did you size your positions appropriately?",
    "What distracted you today and how did you handle it?",
    "Was your FOMO under control? Any revenge trades?",
    "What's one habit you want to improve for the next session?",
]


def get_session_ending(now: datetime):
    for session in SESSIONS:
        if now.time() == session["end"]:
            return session
    return None


def tick():
    now = datetime.now(AEST)
    if now.weekday() >= 5:
        return
    session = get_session_ending(now)
    if session:
        prompt = random.choice(JOURNAL_PROMPTS)
        message = (
            f"**{session['name']} session has ended!**\n\n"
            f":pencil: *{prompt}*"
        )
        send_alert(message)
        print(f"[{now}] Alert sent for {session['name']}")

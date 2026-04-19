from apscheduler.schedulers.blocking import BlockingScheduler

import asx_sessions
import asia_sessions


def main():
    scheduler = BlockingScheduler()

    scheduler.add_job(
        asx_sessions.tick, "interval", seconds=60, id="asx_tick"
    )
    scheduler.add_job(
        asia_sessions.tick, "interval", seconds=60, id="asia_tick"
    )

    print("Session alert scheduler started. Running every 60s.")
    print("\nASX sessions watched (AEST):")
    for s in asx_sessions.SESSIONS:
        print(f"  {s['name']} -> alert at {s['end']}")
    print("\nAsia market events watched (CST / UTC+8):")
    for e in asia_sessions.ASIA_EVENTS:
        print(f"  {e['time']} -> {e['label']}")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Shutting down.")


if __name__ == "__main__":
    main()

import datetime
import time
while True:
    now = datetime.datetime.now()
    actual_time = f"{chr(16)} {now.hour:02}:{now.minute:02}:{now.second:02} {chr(17)}"
    # actual_time = f"▶ {now.hour:02}:{now.minute:02}:{now.second:02} ◀"
    print(actual_time, end="\r", flush=True)
    time.sleep(0.5)
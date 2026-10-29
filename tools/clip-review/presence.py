"""Who has the review page open, held in memory only.

Each page checks in every few seconds with its name and the clip it is on. A name
not heard from for STALE_S seconds drops off. Nothing is written to disk: a restart
forgets everyone, and the next check-in brings them back.
"""
import threading
import time

STALE_S = 10
_seen = {}
_lock = threading.Lock()


def check_in(name, file, in_s):
    now = time.time()
    with _lock:
        _seen[name] = {"name": name, "file": file, "in_s": in_s, "at": now}
        return [v for v in _seen.values() if now - v["at"] <= STALE_S]

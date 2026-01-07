import threading
import time

def worker(thread_id):
    print(f"Thread {thread_id} started")
    while True:
        time.sleep(1)  # simulate ongoing work
        print(f"Thread {thread_id} still running")

thread_id = 0

while True:
    t = threading.Thread(target=worker, args=(thread_id,))
    t.start()
    thread_id += 1

    time.sleep(2)  # slow down creation to avoid instant overload

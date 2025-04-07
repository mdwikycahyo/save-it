import time
from huey.contrib.djhuey import task

@task()
def simulate_long_process():
    print("Starting simulated long process...")
    time.sleep(10)
    print("Simulated long process completed after 10 seconds!")
    return {"status": "completed", "duration": "10 seconds"}

# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
retries = 0
wait_time = 1

while retries < 5:
    print(f"Retryinf after {wait_time} seconds...")
    time.sleep(wait_time)
    retries +=1
    wait_time*= 2

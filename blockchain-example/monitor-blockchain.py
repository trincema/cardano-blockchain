import time
import subprocess

while True:
    with open('blockchain_monitor.txt', "a") as outfile:
        subprocess.run(["curl", "http://127.0.0.1:5000/chain"], stdout=outfile)
        subprocess.run(["curl", "http://127.0.0.1:5000/valid"], stdout=outfile)
        time.sleep(5)
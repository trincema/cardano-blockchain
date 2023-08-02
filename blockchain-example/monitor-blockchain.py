import time
import subprocess

while True:
    subprocess.run(["curl", "http://127.0.0.1:5000/chain"])
    time.sleep(5)
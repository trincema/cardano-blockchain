import time
import subprocess

while True:
    with open('miner1.txt', "a") as outfile:
        subprocess.run(["curl", "http://127.0.0.1:5000/mine_block"], stdout=outfile)
        time.sleep(20)
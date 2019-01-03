import subprocess
import time

from client.config import *
import requests

while True:
    subprocess.run(ADSL_BASH)
    sleep(2)
    requests.get(SERVER_URL)
    sleep(ADSL_CYCLE)
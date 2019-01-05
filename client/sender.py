import subprocess
import time
 
import requests
 
url = 'http://114.116.121.45:5000'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
 
while True:
    p = subprocess.Popen('pppoe-stop',shell = True)
    time.sleep(3)
    p = subprocess.Popen('pppoe-start',shell = True)
    time.sleep(200)
    r = requests.get(url,headers = headers)
    print(r)
    time.sleep(400)

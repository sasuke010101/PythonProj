# coding: utf-8

import re
import requests
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
text = requests.get(url, verify=False).text
stations = re.findall(r'([A-Z]+)\|([a-z]+)',text)
stations = dict(stations)
stations = dict(zip(stations.values(),stations.keys()))
pprint(stations, indent=4)

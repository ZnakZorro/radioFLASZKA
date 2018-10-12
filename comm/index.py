import requests
import json
from datetime import datetime
import sys
now = datetime.now()
teraz=(now.strftime( "%-d %b %Y %H:%M:%S.%f" ))
#http://82.145.73.169:8888/radio/3
url = "http://localhost:8888"
data = {'msg': 'Hi!!!','date':teraz}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)

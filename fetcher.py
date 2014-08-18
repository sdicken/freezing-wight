import urllib.request, urllib.error, urllib.parse
import os
import json
from postmark import PMMail

html_msg = ""
page = 1
params = urllib.parse.urlencode({'type': 1, 'page':1})
params = params.encode('utf-8')
url = 'http://www.legacy.com/obituaries/louisville/api/obituary/0?type=1&ln=&page=' + str(page)
request = urllib.request.Request(url)
request.add_header("Content-Type","application/json;charset=utf-8")
f = urllib.request.urlopen(request)
#print(f.read().decode('utf-8'))
response = f.read().decode('utf-8')
data = json.loads(response)
while(data["NumPageRemaining"] != 0):
    url = 'http://www.legacy.com/obituaries/louisville/api/obituary/0?type=1&ln=&page=' + str(page)
    request = urllib.request.Request(url)
    request.add_header("Content-Type","application/json;charset=utf-8")
    f = urllib.request.urlopen(request)
    response = f.read().decode('utf-8')
    data = json.loads(response)
    entries = data["Entries"]
    for entry in entries:
        html_msg += "<a href=\"" + str(entry["obitlink"]) + "\">" + str(entry["name"]) + "</a><br />"
        #print(entry["name"])
    page += 1
print(html_msg)
	
message = PMMail(api_key = os.environ['POSTMARK_API_KEY'],
				subject = "Daily Obits",
				sender = "sjdick04@louisville.edu",
				to = "kandjdicken@gmail.com",
				html_body = html_msg,
				tag = "none"
				)
message.send()

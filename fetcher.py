import urllib2
import os
from postmark import PMMail
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

html_msg = ""
page = 1
url = 'http://www.legacy.com/obituaries/louisville/obituary-browse.aspx?page=' + str(page) + '&recentdate=0&entriesperpage=25'
soup = BeautifulSoup(urllib2.urlopen(url).read())
while(soup.find(class_="obitName") != None):
    url = 'http://www.legacy.com/obituaries/louisville/obituary-browse.aspx?page=' + str(page) + '&recentdate=0&entriesperpage=10'
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    obitNames = soup.find_all(class_="obitName")
    for name in obitNames:
        html_msg += "<a href=\"" + name.a.get('href') + "\">" + name.a.get_text() + "</a><br />"
        #print(name.a.get_text())
        #print(name.a.get('href'))
    page += 1
#print(html_msg)
	
message = PMMail(api_key = os.environ['POSTMARK_API_KEY'],
				subject = "Daily Obits",
				sender = "sjdick04@louisville.edu",
				to = "kjdicken@twc.com",
				html_body = html_msg,
				tag = "none"
				)
message.send()
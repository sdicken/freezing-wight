import urllib.request
from bs4 import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

page = 1
url = 'http://www.legacy.com/obituaries/louisville/obituary-browse.aspx?page=' + str(page) + '&recentdate=0&entriesperpage=25'
soup = BeautifulSoup(urllib.request.urlopen(url).read())
while(soup.find(class_="obitName") != None):
    url = 'http://www.legacy.com/obituaries/louisville/obituary-browse.aspx?page=' + str(page) + '&recentdate=0&entriesperpage=10'
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    obitNames = soup.find_all(class_="obitName")
    for name in obitNames:
        print(name.a.get_text())
        print(name.a.get('href'))
    page += 1
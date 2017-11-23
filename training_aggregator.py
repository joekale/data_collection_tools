import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://www.google.com/search?tbm=isch&q=farmland+aerial&oq=farmland+aerial"
headers = {'User-Agent': user_agent,}

request = urllib.request.Request(url,None,headers)

page = urllib.request.urlopen(request)
soup = BeautifulSoup(page.read(), 'html.parser')

#images = soup.find_all('a', attrs={'jsname': 'hSRGPd'})

file = open('output.html', 'w')
file.write(soup.prettify())
file.close()



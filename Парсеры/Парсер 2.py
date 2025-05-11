# проект 2
from bs4 import BeautifulSoup
import requests
headers = {
"Accept": "Accept",
"User-Agent": "UserAgent"
}
url="https://store.steampowered.com/"
response=requests.get(url,headers=headers)
sql=response.text
soup=BeautifulSoup(sql,"lxml")
c=soup.find_all("div",class_="home_page_gutter_block")
print(c)
parser=soup.find_all("td",class_="RGBBlue-headersHTML white bgColor_5466796 RGBBlue-headersHTML")
for i in range(len(parser)):
    print(parser[i].text)
parser=soup.find_all("td",class_="RGBwhite bgColor_5466698 RGBwhite")
print(parser)

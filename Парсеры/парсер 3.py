import time
import requests
from bs4 import BeautifulSoup
k=0
list_href=[]
pust=[]
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
url="https://apexmed.ru/"
response=requests.get(url,headers=head)
src=response.text
soup=BeautifulSoup(src,"lxml")
time.sleep(0.5)
help=soup.find("li",class_="dropdown first").find("ul",class_="dropdown-menu").find("ul")
help=str(help)
help=help.split("\n")
for i in range(len(help)):
     if "href"  in help[i] :
        list_href.append(help[i])
time.sleep(0.5)
for j in range(len(list_href)):
    slesh=list_href[j].find("/")
    list_href[j]=list_href[j][slesh:]
time.sleep(0.5)
for n in range(len(list_href)):
    como=list_href[n].find('"')
    list_href[n]=list_href[n][0:como]
for htt in range(len(list_href)):
    list_href[htt]="https://apexmed.ru"+list_href[htt]





for i1 in range(len(list_href)):
    response_2=requests.get(list_href[i1])
    src_2=response_2.text
    soup_1=BeautifulSoup(src_2,"html.parser")
    #pomsh=soup_1.select(".etalage_thumb_image")
    pomsh=soup_1.select(".etalage_thumb_image")
    for j1 in range(len(pomsh)):
        perm=pomsh[j1].get("src")
        url="https://apexmed.ru"+perm
        print(url)
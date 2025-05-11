#Проект 1
from bs4 import BeautifulSoup
import requests
headers = {
"Accept": "Accept",
"User-Agent": "UserAgent"
}
url="https://www.wildberries.ru/catalog/0/search.aspx?search=джинсы%20женские"
response=requests.get(url,headers=headers)
response.encoding = response.apparent_encoding
sql=response.text
with open("5.html","w",encoding="utf-8") as file:
    file.write(sql)
f=open("7.html",encoding="utf-8").readlines()
f="".join(f)
soup=BeautifulSoup(sql,"lxml")
parser=soup.select("div.product-card__wrapper")
print(parser)
f=open("new.txt").readlines()
c=[]
v=[]
for i in range(len(f)):
    if "http" in f[i]:
        c.append(f[i])
for i in range(len(c)):
    v.append(c[i][:-1])
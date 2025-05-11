import requests
from bs4 import BeautifulSoup
gt=input("введите что хотите найти на авито: ")
count=int(input("введите сколько страниц хотите получить авиторучки: "))
url="https://www.avito.ru/moskva"
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Safari/537.36"}
for i in range(n+1):
    a=requests.get(url,params={"q":gt,"p":n},headers=head)
    s=a.text
    soup=BeautifulSoup(s,"lxml")
    avit=soup.find_all("a",class_="link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH")
    for i in range(len(avit)):
        sl=avit[i].get("href")
        ov="https://www.avito.ru/"+sl
        print(ov)
     
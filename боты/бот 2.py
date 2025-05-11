import time
import telebot
import requests
from bs4 import BeautifulSoup
bot=telebot.TeleBot("ВАШ КЛЮЧ")
def new():
    b=[]
    a=[] #тепрь этот список содержит список в списках то есть i[0]-это все сслыки, i[1]-это все заголовки ,i[2]-это текст, а если мы напишем i[0][1]-это мы вызовем первый спсок и из первого списка выводим заголовок 
    url="https://life.ru/s/novosti"# адрес ссылки то есть юрл
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Safari/537.36"}#это хедр он говорит сайту что мы не бот
    response=requests.get(url,headers=head)# собираем все данные с ссылки и помещаем сой юзер агент чтобы сайт понял , что я не бот
    s=response.text # метод текст из библеотеки рекуест дает нам все данные хтмл из того или иного адреса 
    soup=BeautifulSoup(s,"lxml")# теперь мы можем собирать данные с переменной s в которой храниться хтмл код и используем парсер "lxml"
    nov=soup.find("div",class_="styles_postsList__MBykd").find_all("a")# находим тег берем класс и ещем все теги а под тегом div
    for i in range(len(nov)):
        sl=nov[i].get("href")
        copy="https://life.ru"+sl# теперь переменная copy отвечает за ссылки конкретный новостей
        a.append(copy)
    for g in range(len(a)):
        if "https://life.ru/p/" in a[g]:
            b.append(a[g])
    pust=b[0]

    response_1=requests.get(pust,headers=head)
    s_1=response_1.text
    soup_1=BeautifulSoup(s_1,"lxml")
    nov_1=soup_1.find("h1")
    chit=soup_1.find_all("div",class_="indentRules_block__iwiZV styles_text__3IVkI") 
    for q in range(len(chit)):
        chit[q]=chit[q].text
    #borr=nov_1.text
    poor=chit[0]
    return poor
@bot.message_handler(content_types=["text"])
def sms(message): 
    l=new()
    while True:
        x=new()
        if x!=l:
            l=x
            print(l)
            time.sleep(60)
            if message.text.lower()=="Поехали":
                bot.send_message("@ВАШ КАНАЛ",l)

    
bot.polling(none_stop=True,interval=0)      
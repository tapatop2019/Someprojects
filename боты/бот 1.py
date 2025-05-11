import time
from re import L
import telebot
import requests
from bs4 import BeautifulSoup
bot=telebot.TeleBot("Ведите свой ключ")

def news():
    a=[] #тепрь этот список содержит список в списках то есть i[0]-это все сслыки, i[1]-это все заголовки ,i[2]-это текст, а если мы напишем i[0][1]-это мы вызовем первый спсок и из первого списка выводим заголовок 
    url="https://life.ru/s/novosti"# адрес ссылки то есть юрл
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Safari/537.36"}#это хедр он говорит сайту что мы не бот
    response=requests.get(url,headers=head)# собираем все данные с ссылки и помещаем сой юзер агент чтобы сайт понял , что я не бот
    s=response.text # метод текст из библеотеки рекуест дает нам все данные хтмл из того или иного адреса 
    soup=BeautifulSoup(s,"lxml")# теперь мы можем собирать данные с переменной s в которой храниться хтмл код и используем парсер "lxml"
    nov=soup.find("div",class_="styles_postsList__MBykd").find_all("a")# находим тег берем класс и ещем все теги а под тегом div
    for i in range(len(nov)):#проходимся циклом по списку 
        b=[]# теперь в этой переменной содержится и ссылка и текс и заголовок
        sl=nov[i].get("href")# берем класс "href"
        copy="https://life.ru"+sl# теперь переменная copy отвечает за ссылки конкретный новостей
        if "/p/" in copy :
            b.append(copy)#засовываем в список ссылки 
            #print(copy)#
            respons_1=requests.get(copy)#
            s_1=respons_1.text#
            soup_1=BeautifulSoup(s_1,"lxml")#
            nov_1=soup_1.find_all("h1")#находи все загаловки метод find_all находит определенные данные и констрирует из них список
            for j in range(len(nov_1)):#проходимся циклом по списку 
                b.append(nov_1[j].text+".")#засовываем в список заголовки
                #print(nov_1[j].text+".")   # и делаем каждей элемент строкой методом текст из беаутифулсупа 
            prod=soup_1.find("p",class_="styles_subtitle__3I1PB")
            b.append(prod.text)#засовываем в список текст
            #print(prod.text)    
            a.append(b)# в конце мы аппендим в а другие списки
    
    
    return a #втрая ссылка


@bot.message_handler()
def sms(message):
    l=news()[0]
    while True:
        x=news()[0]
        if x!=l:
            l=x
            print(l)
            time.sleep(60)
            if message.text.lower()=="поехали":
                bot.send_message("@ВАШ КАНАЛ",l[1]+"\n"+l[2])

    
bot.polling(none_stop=True,interval=0)


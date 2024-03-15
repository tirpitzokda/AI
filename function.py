import requests
from bs4 import BeautifulSoup

def news():
    response = requests.get('https://tengrinews.kz/news/')
    soup = BeautifulSoup(response.content,'html.parser')
    news_headlines = soup.find_all(class_='content_main_item_title')
    for headline in news_headlines:
        print(headline.text)

def articles():
    responce = requests.get('https://tengrinews.kz/article/')
    soup = BeautifulSoup(responce.content, 'html.parser')
    articles_headlines = soup.find_all(class_='content_main_item_title')
    for headline in articles_headlines:
        print(headline.text)

def economic():
    responce = requests.get('https://tengrinews.kz/economic/')
    soup = BeautifulSoup(responce.content, 'html.parser')
    articles_headlines = soup.find_all(class_='content_main_item_title')
    for headline in articles_headlines:
        print(headline.text)

def science():
    responce = requests.get('https://tengrinews.kz/science/')
    soup = BeautifulSoup(responce.content, 'html.parser')
    articles_headlines = soup.find_all(class_='content_main_item_title')
    for headline in articles_headlines:
        print(headline.text)

# pip install lxml
# scriping

import requests
from bs4 import BeautifulSoup


url = 'https://sport.ua/uk/rss/all'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'xml')
# soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all('item')
item = items[0]
print(item)

title = item.find('title').text
print(title)

link = item.find('link').text
print(link)

picture = item.find('enclosure').get('url')
print(picture)

description = item.find('description').text
print(description)

category_items = item.find_all('category')
category = []
for el in category_items:
    category.append(el.text)
print(category)

date = item.find('pubDate').text
print(date)

news = []

def get_info(item):
    title = item.find('title').text
    link = item.find('link').text
    date = item.find('pubDate').text
    description = item.find('description').text
    picture = item.find('enclosure').get('url')
    category_items = item.find_all('category')
    category = []
    for el in category_items:
        category.append(el.text)
    info = {
        'title': title,
        'link': link,
        'picture': picture,
        'description': description,
        'category': category,
        'date': date
    }
    return info



for item in items:
    # title = item.find('title').text
    # link = item.find('link').text
    # date = item.find('pubDate').text
    # description = item.find('description').text
    # picture = item.find('enclosure').get('url')
    # category_items = item.find_all('category')
    # category = []
    # for el in category_items:
    #     category.append(el.text)
    # info = {
    #     'title': title,
    #     'link': link,
    #     'picture': picture,
    #     'description': description,
    #     'category': category,
    #     'date': date
    # }
    info = get_info(item)
    news.append(info)

print(news)


import csv


with open('news-sport.csv', 'w', newline='') as file:
    fieldnames = ['title', 'link', 'picture', 'description', 'category', 'date']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(news)
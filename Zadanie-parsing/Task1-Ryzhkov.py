import requests
from bs4 import BeautifulSoup
import csv
import time


url = 'https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def get_content(url, table_name):
    res = []
    page = requests.get(url)
    print(page.status_code)
    soup = BS(page.text, "html.parser")
    news_line = soup.find(id='newsline')
    allNews = news_line.findAll('div', 'item')
    fav = input('Input your favorite sport in Ukrainian or "всі": ')
    for data in allNews:
        time_pub = data.find('span', attrs={'class': 'item-date'})
        time_pub = time_pub.text.replace('\n', '').strip()

        sport = data.find('span', attrs={'class': 'item-sport'})
        sport = sport.text.replace('\n', '').strip()

        title = data.a.text.replace('\n', '').strip()

        href = data.a['href']

        if fav.lower() == sport.lower() or fav.lower() == 'всі':
            print(time_pub)
            print(sport)
            print(title)
            print(href)
            print('=' * 60)
            res.append({table_name[0]: sport, table_name[1]: title, table_name[2]: time_pub, table_name[3]: href})
    return res


def write_content(content, table_name):
    csv_title = table_name
    # print(csv_title)
    # with open('sport.csv', 'w', encoding='utf8') as f:
    with open('sport.csv', 'w') as f:
        wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        wr.writeheader()
        wr.writerows(content)



table_name = ['sport', 'title', 'time of publication', 'url']
url = 'https://new.sport.ua/uk'
# # # url = 'https://new.sport.ua'
news = get_content(url, table_name)
write_content(news, table_name)

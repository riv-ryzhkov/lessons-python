import requests
from bs4 import BeautifulSoup
import csv


def get_content(url):
    # getting of content from user's URL
    result = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find('div', class_='item-grid')
    all_products = soup.find_all('div', class_='item-box')
    for el in all_products:
        if not el.find('label', class_='ribbon-image-text'):
            availability = 'Товар на цей час відсутній'
        else:
            availability = el.find('label', class_='ribbon-image-text').text
        title_full = el.find('div', class_='details').a.text
        title = title_full.split(', ')[0]
        article = title_full.split(', ')[1]
        price_str = el.find('span', class_='price actual-price').text
        price = [i for i in price_str if i.isdigit()]
        price = int(''.join(price))/100
        image = el.find('div', class_='picture')
        image = image.a.img['data-lazyloadsrc']
        result.append({
            'title': title,
            'article': article,
            'availability': availability,
            'price text': price_str,
            'price': price,
            'image': image
        })
    return result


def output_availability(content):
    # printing results on user's screen
    print('=' * 80)
    for el in content:
        for key, vol in el.items():
            print(key, ':', vol)
        print('-'*80)


def write_content(content):
    # writing to the file as a table
    csv_title = ['title', 'article', 'availability', 'price text', 'price', 'image']
    with open('price.csv', 'w', encoding='utf8') as file:
        wr = csv.DictWriter(file, fieldnames=csv_title, delimiter=';')
        wr.writeheader()
        wr.writerows(content)


url = 'https://home-club.com.ua/ua/%D0%93%D0%B5%D0%B8%D0%BC%D0%B5%D1%80%D1%81%D1%8C%D0%BA%D1%96-%D0%BA%D1%80%D1%96%D1%81%D0%BB%D0%B0'
content = get_content(url)
write_content(content)
output_availability(content)

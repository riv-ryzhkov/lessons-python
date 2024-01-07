import requests
from bs4 import BeautifulSoup


def get_content(url):
    # getting of content from user's URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find('div', class_='additional-details')
    availability = soup.find_all('span', class_='value')
    return {'article': availability}


def output_availability(content):
    # printing results on user's screen
    article = content['article'][0].text.strip()
    availability_for_delivery = content['article'][1].text.strip()
    availability_forecast_in_Poland = content['article'][2].text.strip()
    availability_in_Lviv = content['article'][4].text.strip()
    print('article :\t\t\t\t\t\t ', article)
    print('availability for delivery :\t\t ', availability_for_delivery)
    print('availability forecast in Poland :', availability_forecast_in_Poland)
    print('availability in Lviv :\t\t\t ', availability_in_Lviv)


def write_content(content):
    # writing results to file with .txt
    with open('article-'+content['article'][0].text.strip()+'.txt', 'w') as file:
        for i in 0, 1, 2, 4:
            file.write(content['article'][i].text.strip()+'\n')


url = 'https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE'
content = get_content(url)
write_content(content)
output_availability(content)

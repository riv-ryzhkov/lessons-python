# ua.korrespondent.net
from bs4 import BeautifulSoup as BS
import requests


url = 'https://ua.korrespondent.net/'

page = requests.get(url)
# print(page.status_code)
soup = BS(page.text, "html.parser")

article = soup.find_all('div', class_='article')
# print(*article, sep='\n')
for i in range(10):
    el = article[i]
    print('-'*50)
    # print(el)
    print(i+1, ':')
    time = el.div.text
    ref = el.a['href']
    img = el.a.img['src']
    print('Article :', time.replace('\n', ''))
    print('Link    :', ref)
    print('Image   :', img)
print('='*50)
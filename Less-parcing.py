# pip install bs4
# https://beautiful-soup-4.readthedocs.io/en/latest/


import requests
from bs4 import BeautifulSoup as BS
import csv
import time


################################################

import requests
from bs4 import BeautifulSoup


url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)

# print(response.text)
# print(type(response.text))

soup = BeautifulSoup(response.text, 'html.parser')
print(type(soup))
# print(soup)


# print(*dir(soup), sep='\n')



# ##################### start info #############

# print(soup.div.prettify())  # tags <div>


# o = soup.div.prettify()
# o = soup.div
# print(type(o))    # tags <div>
# print(o)  # tags <div>



# print(soup.div.a)     # tags <div><a>    </a></div>


# print(soup.find('div').find('a'))   # tags <div><a>    </a></div>



# print(soup.find('head'))   # tag <head>


# print(soup.find('head').find_all('link')[1])  # tags <head><link> [1]  </link></head>
# print(soup.find('head').find_all('link')[1]['href'])  # tags <head><link> [1]<href=" ">  </link></head>


# print(soup.div.a)  # tags <div><a>    </a></div>
# print(soup.div.a.svg['xmlns']) # tags <div><a><svg xmlns=" "></svg></a></div>



# print(soup.h4)  # tags <h4>


# tag = soup.li
# tag = soup.li.text
# tag = soup.li.a['href']
# tag = soup.li.a['target']
# print(soup.li)
# print(tag)
# print(type(tag))




# tag = soup.body
# # print(*dir(tag), sep='\n')
# # print(tag)
#
# # print(tag.a)
# print(tag.span)
# print(tag.span['class'])






# print(soup.head.link)
# print(soup.head.link['href'])
# print(soup.head.link['rel'])
# print(soup.head.link['type'])




# print(soup)
# print(soup.text)
# print(type(soup))
# print(type(soup.text))
# print('.'*80)
#
# print(soup.text.replace('\n\n', ''))


# ...................................

# print(soup.prettify())
# print(type(soup.prettify()))



# print(soup.link)
# print(type(soup.link))





# print(soup.find_all('link'))
# print(type(soup.find_all('link')))
#
#
# print(*dir(soup.find_all('link')), sep='\n')  # close to list!!!!!






# print(*soup.find_all('link'), sep='\n')


# for el in soup.find_all('link'):
#     # print(el['href'])
#     if el['href'].startswith('/'):
#         print('https://scrapingclub.com'+el['href'])
#     else:
#         print(el['href'])



# .........................

# print(*soup.find_all(['p']), sep='\n')
# print(*soup.find_all(['a', 'h4']), sep='\n\n')




# res = soup.find_all(['p', 'a'])
# print(type(res))
# print(*res, sep='\n\n')




# res = soup.find_all(['p', 'a'], limit=5)
# for el in range(len(res)):
#     print()
#     print(el+1, ':')
#     print(res[el])
#     print('.'*60)



# ......................................................


# print(soup.find(id="banner"))
# print('len id = ', len(soup.find_all(id="banner")))


# print('len id=True :', len(soup.find_all(id=True)))
# print(*soup.find_all(id=True), sep='\n' + '.'*150 + '\n\n')


# .......................................................


# print(soup.find_all(class_="container"))

# print(*soup.find_all(class_="nav-link"), sep='\n')

# print(soup.find_all('h4'))


# print(soup.find_all('div', class_="alert"))
# print(soup.find_all('div', class_="alert-success"))

# print(soup.find_all('div', role="alert"))




# print(soup.find_all('div', class_='px-4 mb-6 w-full sm:w-1/3 md:w-1/4 lg:w-4/12'))
# print(soup.find_all('div', class_='px-4 mb-6 w-full sm:w-1/3 md:w-1/4'))
# print(soup.find_all('div', class_='w-full px-4 mb-6 sm:w-1/3 md:w-1/4 lg:w-4/12'))

# print(soup.select('div.w-full.px-4.mb-6'))   # вільна послідовність
# print(soup.select('div.px-4.mb-6.w-full'))   # вільна послідовність






# print(soup.a)
# print(soup.find('a'))




# print(soup('a'))
# print(soup.find_all('a'))





# res = soup(['p', 'a'], limit=10)
# for el in res:
#     print(el)
#     print('.'*40)
#
#


##########################################
# parsing
###############################
# items = soup.find_all('div', class_='w-full rounded border')
#
# print(type(items))
# print(*dir(items), sep='\n')


# print(items)
#
# print(type(items[0]))
#
# # print(*dir(items[0]), sep='\n')
#
#
# print(items[0].prettify())
#
# link = 'https://scrapingclub.com' + items[0].a['href']
# print(link)
# title = items[0].h4.text
# print(title)
# price = items[0].h5.text
# print(price)
#
#
#
# # for i in items:
# for n, i in enumerate(items, start=1):
# #     # print(i)
# # #     # breakpoint()
#     image = i.img['src']
#     name = i.find('h4').text.strip()
#     price = i.find('h5').text
#     price = '$' + str(float(price[1:]) + 1)
#     print(f'{n}:  {price} за {name} https://scrapingclub.com{image}')


###################### pages ######################

# def parsing(url):
#     # url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     items = soup.find_all('div', class_='w-full rounded border')
#     for n, i in enumerate(items, start=1):
#         image = i.img['src']
#         name = i.find('h4').text.strip()
#         price = i.find('h5').text
#         price = '$' + str(float(price[1:]) + 1)
#         print(f'{n}:  {price} за {name} https://scrapingclub.com{image}')
#
#
# for i in range(5):
#     url = f'https://scrapingclub.com/exercise/list_basic/?page={i}'
#     print(f'###### PAGE {i+1} ' + '#' * 40)
#     parsing(url)
#     print('=' * 80)




###################################################################################
url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# # # print(response.text)
# soup = BS(response.text, 'html.parser')
# # # print(type(soup))
# # # print(soup)
# #
# #
# quotes = soup.find_all('span', class_='text')
# # print(quotes)
# for n, el in enumerate(quotes, start=1):
#     print(n, ':', el.text)
#
#
#
# authors = soup.find_all('small', class_='author')
# for n, el in enumerate(authors, start=1):
#     print(n, ':', el.text)
#
#
# tags = soup.find_all('div', class_='tags')
# for n, el in enumerate(tags, start=1):
#     # print(n, ':', el)
#     print(n, ':')
#     tags = el.find_all('a')
#     for i in tags:
#         print(i.text, end=' ')
#     print()
#     print('-'*80)

# ############# PAGES ####################
#
# for i in range(1, 10):
#     print('-'*80)
#     print('Page #:', i)
#     # url = 'https://quotes.toscrape.com/page/{}'.format(i)
#     url = f'https://quotes.toscrape.com/page/{i}'
#     response = requests.get(url)
#     soup = BS(response.text, 'html.parser')
#     quotes = soup.find_all('span', class_='text')
#     authors = soup.find_all('small', class_='author')
#     tags = soup.find_all('div', class_='tags')
#     print('=' * 80)
#     for i in range(len(quotes)):
#         print(quotes[i].text)
#         print('Author: \t' + authors[i].text)
#         tags_for_quote = tags[i].find_all('a', class_='tag')
#         print('tags:  \t\t#', end='')
#         for tag in tags_for_quote:
#             print(tag.text, end=' #')
#         print()
#         print('=' * 80)



############################################################################
################ BBC.COM    #####################################
############################################################################

# url = 'https://www.bbc.com/ukrainian'
#
# page = requests.get(url)
# print(page.status_code)
# soup = BS(page.text, "html.parser")
#
# soup = soup.find('section', attrs={'aria-labelledby': 'Головне'})
# allNews = soup.find_all('li')
# print('allNews :', allNews)
# for el in allNews:
#     img = el.img['src']
#     title = el.a.text
#     # time = el.time['datetime'] + '>>' + el.time.text
#     time = el.time.text
#     text = el.p.text
#     link = el.a['href']
#
#     print('time :', time)
#     print('.' * 80)
#     print('title :', title)
#     print('.' * 80)
#     print('short text :', text)
#     print('.' * 80)
#     print('picture :', img)
#     print('.' * 80)
#     print('link :', link)
#     print('=' * 80)


################################################################################
#### NEWS ######################################################################
###############################################################################

# url = 'http://mignews.com/mobile'
# # url = 'https://www.pravda.com.ua'
# # # # #
# page = requests.get(url)
# print(page.status_code)
# #
# soup = BS(page.text, "html.parser")
# # # # # print(soup)
# allNews = soup.findAll('div', class_='text-color-dark')
# # allNews = soup.findAll('div', class_="article_header")
# # print(allNews[0].text.strip())
# # print('https://mignews.com' + allNews[0].a['href'])
# # #
# #
# # #     1st  way
# # #====================================
# for data in allNews:
#     # print(data.text)
#     print(data.text.strip())
#     print('https://mignews.com' + data.a['href'])
#
#
#     # print('http://mignews.com/mobile'+data.a['href'])
#     # print('https://www.pravda.com.ua/'+data.a['href'])
#     print('='*60)



#
# #     2nd  way
# #====================================
# filteredNews = {}
# for data in allNews:
#     filteredNews[data.text.strip()] = data.a['href']
# print('=' * 80)
# # print(filteredNews)
# # breakpoint()
# for key, vol in filteredNews.items():
#     print(key)
#     if vol.startswith('/'):
#         # print('http://mignews.com'+vol)
#         # print('https://www.pravda.com.ua'+vol)
#         print(url+vol)
#     else:
#         print(vol)
#     print('=' * 80)


#############################################


# url = 'https://www.pravda.com.ua/'
#
# page = requests.get(url)
# print(page.status_code)
# filteredNews = {}
# soup = BS(page.text, "html.parser")
# allNews = soup.findAll('div', class_="article_header")
# # print(allNews[2].prettify())
# for data in allNews:
#     filteredNews[data.text.strip()] = data.a['href']
# print('=' * 80)
# for key, vol in filteredNews.items():
#     print(key)
#     if vol.startswith('/'):
#         print('https://www.pravda.com.ua'+vol)
#     else:
#         print(vol)
#     print('=' * 80)


#################################################
############### SPORT.UA ########################
#################################################

# url ='https://sport.ua/uk'
#
# page = requests.get(url)
# print(page.status_code)
# soup = BS(page.text, "html.parser")
# soup = soup.find(id='most_popular_news')
# news_list = soup.findAll('div', class_="item")
# # print(news_list[2].prettify())
# # breakpoint()
# for el in news_list:
#     news = el.find('div', class_="item-row")
#     # print(news.prettify())
#     # breakpoint()
#     print('='*80)
#     print(news.span.text)
#     print(news.find('span', class_='item-date').text.strip())
#     news = el.find('div', class_="item-title item-title--b")
#     # print(news.prettify())
#     # breakpoint()
#     # print(news.img['alt'])
#     print(news.a.text)
#     print(news.img['data-src'])
#     print(news.a['href'])
#     print('='*80)


###################################################################
############# SPORT.UA (розширений)   ############
#
# def get_content(url, table_name):
# # def get_content(url):
#     res = []
#     page = requests.get(url)
#     print(page.status_code)
#     soup = BS(page.text, "html.parser")
#     news_line = soup.find(id='newsline')
#     # news_line = soup.find(id='most_popular_news')
#     allNews = news_line.findAll('div', 'item')
#     # allNews = news_line.findAll('div', 'item-row')
#     fav = input('Input your favorite sport in Ukrainian or "всі": ')
#     for data in allNews:
#         time_pub = data.find('span', attrs={'class': 'item-date'})
#         time_pub = time_pub.text.strip()
#
#         sport = data.find('span', attrs={'class': 'item-sport'})
#         sport = sport.text.strip()
#
#         title = data.a.text.strip()
#
#         href = data.a['href']
#
#         if fav.lower() == sport.lower() or fav.lower() == 'всі':
#             print(time_pub)
#             print(sport)
#             print(title)
#             print(href)
#             print('=' * 60)
#             # res.append({'sport': sport, 'title': title, 'time_pub': time_pub, 'link': href})
#             res.append({table_name[0]: sport, table_name[1]: title, table_name[2]: time_pub, table_name[3]: href})
#     return res
#
#
# def write_content(content, table_name):
# # def write_content(content):
# #     csv_title = ['sport', 'title', 'time_pub', 'link']
#     csv_title = table_name
#     # print(csv_title)
#     # with open('sport.csv', 'w', encoding='utf8') as f:
#     with open('sport.csv', 'w') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
# #
# #
# #
# table_name = ['sport', 'title', 'time', 'link']
# url = 'https://new.sport.ua/uk'
# # # url = 'https://new.sport.ua'
# news = get_content(url, table_name)
# # news = get_content(url)
# write_content(news, table_name)
# # write_content(news)



######################################################
############# LINKS    ###############################
######################################################
# import requests
# from bs4 import BeautifulSoup as BS
#
#
# url = 'https://bottlepy.org/docs/dev'
# result = requests.get(url)
# soup = BS(result.text, features='html.parser')
# r = soup.find_all('a')
# print(*r, sep='\n')
# # # breakpoint()
# r = soup.find_all('a')[5]['href']
# print(r)
#
#
#
# # .........................................................
#
# def get_links(url):
#     result = requests.get(url)
#     soup = BS(result.text, features='html.parser')
#     links = [url+str(element.get('href')) for element in soup.find_all('a') if not str(element.get('href')).startswith('http')]
#     links1 = [element.get('href') for element in soup.find_all('a') if str(element.get('href')).startswith('http')]
#     return links+links1
#
#
#
# urls = ['https://bottlepy.org/docs/dev/',
#         'https://bottlepy.org/docs/dev/development.html#git-workflow-examples',
#         'https://price.ua/ua/catc371t2.html',
#         'https://sport.ua/uk',
#         'https://bbc.com',
#         'https://beautiful-soup-4.readthedocs.io/en/latest/',
#         'https://cnn.com']
#
#
# for url in urls:
#     print('Links in', url)
#     for num, link in enumerate(get_links(url), start=1):
#         print(num, ':', link)
#     print('='*80)



#############################################################################
############## PRICE.UA ХОЛОДИЛЬНИКИ / ПЛАНШЕТЫ #############################

def get_content(url, name):
    resp = requests.get(url)
    print(resp.status_code)
    result = []
    # session = requests.session()
    if resp.status_code == 200:
        page = BS(resp.text, 'html.parser')
        product = page.find(id='fluid-grid')
        # print(product.prettify())
        # breakpoint()
        # list_products = product.find_all('div', attrs={'class': 'product-block type2 ga_container black-link-style split-4-cards is-model'})
        list_products = product.find_all('div', attrs={'class': 'product-block'})
        # print(*list_products, sep='\n')
        # breakpoint()
        for div in list_products:
            prod = div.find('div', attrs={'class': 'white-wrap'})
            title = prod.a['title']
            href = prod.a['href']
            pic = 'https:' + prod.img['src']

            price_wrap = div.find('div', attrs={'class': 'price-wrap'})

            price_str = price_wrap.text
            # print(price_str)
            # breakpoint()
            price = [el for el in price_str if el.isdigit()]
            price = int(''.join(price))*1.01
            # tmp = {'title': title, 'price_str': price_str, 'price': price, 'pic': pic, 'url': href}
            tmp = {name[0]: title, name[1]: price_str, name[2]: price, name[3]: pic, name[4]: href}
            result.append(tmp)
        return result


def write_content(content, name):
    # csv_title = ['title', 'price_str', 'price', 'pic', 'url']
    csv_title = name
    # print(csv_title)
    # with open('price.csv', 'w', encoding='utf8') as f:
    with open('price.csv', 'w') as f:
        wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        wr.writeheader()
        wr.writerows(content)

#
# url = 'https://price.ua/ua/catc371t2/page{}.html'
# # url = 'https://price.ua/ua/catc1081t2/page{}.html'
# url = 'https://price.ua/ua/catc52t2/page{}.html'
# url = 'https://price.ua/ua/catc52t2'
# url = 'https://price.ua/ua/catc52t2/page{}.html'
url = 'https://price.ua/ua/catc6399t2.html'
# url = 'https://price.ua/ua/catc6399t2/page{}.html'
csv_title = ['title', 'price_str', 'my_price', 'pic', 'url']
res = []
for i in range(1, 3):
    time.sleep(1)
    res += get_content(url.format(i), csv_title)
for i in res:
    for key, val in i.items():
        print(key, ':', val, sep='\t')
    print('-' * 60)
write_content(res, csv_title)


###################################################################
####################  MON #############################
#########################################################

#
# url ='https://mon.gov.ua/'
#
#
#
#
#
# # session = requests.session()
# page = requests.get(url)
# print(page.status_code)
#
# soup = BS(page.text, "html.parser")
#
# # soup = soup.find('div', class_='news-block')
# #
# # articles = soup.find_all('article')
# # # print(articles[0])
# #
# # for el in articles:
# #     print(el.div.text)
# #     print(el.span.text)
# #     print(el.a['href'])
# #     print('='*80)
# #
#
# # ........................................
# all = soup.find_all('a')
# for n, i in enumerate(all):
#     if i.has_attr('href') and i['href'] != '#':
#         print('.' * 80)
#         print(n, ':', i.text.strip().replace('\n', ''))
#         if i['href'].startswith('http'):
#             print(i['href'])
#         else:
#             print(f"https://mon.gov.ua/{i['href']}")



# ################################# olx ###################################
# def get_content(url):
#     resp = requests.get(url)
#     print(resp.status_code)
#     rows = []
#     # session = requests.session()
#     if resp.status_code == 200:
#         page = BS(resp.text, 'html.parser')
#         # print(page)
#         # breakpoint()
#         # table = page.find(id='offers_table')
#         table = page.find(id='listContainer')
#         # print('listContainer :', table)
#         # breakpoint()
#         tr_list = table.find_all('tr', attrs={'class': 'wrap'})
#         # print('class: wrap :', tr_list)
#         # breakpoint()
#         for tr in tr_list:
#             title_cell = tr.find('td', attrs={'class': 'title-cell'})
#             # print('class: title-cell', title_cell)
#             title = title_cell.find('h3')
#             # print(title)
#
#             title_text = title.text
#             title_text = title_text.replace('\n', '')
#             # print('title_text :', title_text)
#             href = title.a['href']
#             href = title.a['href'].replace(';promoted', '')
#             # print('ref: ', href)
#             # breakpoint()
#             td_price = tr.find('td', attrs={'class': 'td-price'})
#             price_str = td_price.text.replace('\n', '')
#             # print('price_str :', price_str)
#             price_temp = ''.join(c for c in price_str if c.isdigit())
#             if price_temp:
#                 price = int(price_temp)
#             else:
#                 price = 'договорная'
#             tmp = {'title': title_text, 'price_str': price_str, 'price': price, 'url': href}
#             # tmp = {'title': title_text, 'price': price, 'url': href}
#             rows.append(tmp)
#         return rows
#
#
# def parse_content(content):
#     csv_title = ['title', 'price_str', 'price', 'url']
#     print(csv_title)
#     with open('olx.csv', 'w', encoding='utf8') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
#
#
# url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/'
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/?page={}'
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/materinskie-platy/?page={}'
# # url = 'https://m.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/?page={}'
#
# res = []
# for i in range(1, 2):
#     time.sleep(2)
#     res += get_content(url.format(i))
# for i in res:
#     for key, val in i.items():
#         print(key, val, sep='\t')
#     print('-' * 80)
# parse_content(res)
#
#




##########################################


################################## END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###############   DZ  Домашнє завдання ################################
########################################################################


# # DZ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # ua.korrespondent.net
#
# url = 'https://ua.korrespondent.net/'
#
# page = requests.get(url)
# print(page.status_code)
# soup = BS(page.text, "html.parser")
#
# article = soup.find_all('div', class_='article')
# # print(*article, sep='\n')
# for i in range(10):
#     el = article[i]
#     print('-'*50)
#     # print(el)
#     print(i+1, ':')
#     time = el.text
#     ref = el.a['href']
#     img = el.a.img['src']
#     print('Article :', time.replace('\n', ''))
#     print('Link    :', ref)
#     print('Image   :', img)
# print('='*50)







##################################################
########### ROZETKA 403  !!!!!!!!!!! #############
##################################################
#
# url = 'https://rozetka.com.ua/ua/notebooks/c80004/'
#
# def parsing(url, name):
# # # def parsing(url):
#     resp = requests.get(url)
#     print(resp.status_code, url)
#     # breakpoint()
#     rows = []
#     if resp.status_code == 200:
#         page = BS(resp.text, 'html.parser')
#         # print(page)
#         # breakpoint()
#         table = page.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
#         # print(table[2])
#         # breakpoint()
#         for el in table:
#             title = el.find('span', class_='goods-tile__title').text
#             # print(title)
#             # breakpoint()
#             price_val = el.find('span', class_='goods-tile__price-value').text
#             price_val = [i for i in price_val if i.isdigit()]
#             # print(price_val)
#             # breakpoint()
#             price_val = int(''.join(price_val))
#             # print(price_val)
#             # breakpoint()
#             my_price = price_val * 1.01
#             # print(price_val)
#             # breakpoint()
#             currency = el.find('span', class_='goods-tile__price-currency').text
#             if currency == '₴':
#                 currency = 'грн.'
#             # print(title)
#             # print(price_val, currency)
#             # breakpoint()
#             # print('.'*80)
#             # rows.append({'title': title, 'price': price_val, 'my price': my_price, 'currency': currency})
#             tmp = {name[0]: title, name[1]: price_val, name[2]: my_price, name[3]: currency}
#             rows.append(tmp)
#     return rows
#
#
# def write_content(content, name):
#     csv_title = name
#     with open('rozetka.csv', 'w') as f:
#     # with open('rozetka.csv', 'w', errors='ignore') as f:
#     # with open('rozetka.csv', 'w', encoding='utf8') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
# #
# #
# # # result = parsing(url, )
# # # write_content(result)
# #
# #
# # # url = 'https://rozetka.com.ua/ua/notebooks/c80004/page={}/'
# # # url = 'https://hard.rozetka.com.ua/ua/processors/c80083/page={}/'
# #
# urls = [
#     # 'https://rozetka.com.ua/ua/notebooks/c80004/page={}/',
#     # 'https://rozetka.com.ua/ua/care_lamps/c278086/page={}/',
#     # 'https://hard.rozetka.com.ua/ua/processors/c80083/page={}/',
#     # 'https://rozetka.com.ua/ua/mobile-phones/c80003/page={}/',
#     # 'https://bt.rozetka.com.ua/ua/microwaves/c80162/page={}/',
#     # 'https://rozetka.com.ua/ua/elektrosamokati/c4657382/page={}/'
# ]
# #
# csv_title = ['title of product', 'old price', 'new price', 'currency']
# # # res = parsing(url, csv_title)
# # # parse_content(res, csv_title)
# # #
# res = []
#
# for url in urls:
#     for i in range(1, 2):
#         time.sleep(0.5)
#         res += parsing(url.format(i), csv_title)
#
# for i in res:
#     for key, val in i.items():
#         print(key, ':', val, sep='\t')
#     print('-' * 80)
# write_content(res, csv_title)


############################################ END


# import http.client
#
#
# host = "rozetka.com.ua"
# conn = http.client.HTTPSConnection(host)
# conn.request("GET", '/ua/notebooks/c80004', headers={"Host": host})
# response = conn.getresponse()
# print(response.status, response.reason)


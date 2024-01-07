import requests

def get_currencies_information_pb(url, bank_name):
  response = requests.get(url)
  print('-------------------------------')
  if response.status_code == 200:
    print(f"{bank_name} CURRENCY EXCHANGE COURSE")
    search_list = ['USD', 'EUR']
    key = 'ccy'
    filtered_collection = [sub for sub in response.json() if sub[key] in search_list]
    for currency in filtered_collection:
      print(f"{currency['ccy']}/{currency['base_ccy']}  buy: {currency['buy']} / sell: {currency['sale']}")
  else:
    print(f"{url} cannot be loaded {response.status_code}")

  print('-------------------------------')

def get_currencies_information_mono(url, bank_name):
  response = requests.get(url)

  print('-------------------------------')
  if response.status_code == 200:
    print(f"{bank_name} CURRENCY EXCHANGE COURSE")
    currencies_names = { 840: 'USD', 978: 'EUR', 980: 'UAH'}
    search_list_a = [840, 978]
    search_list_b = [980]
    key_a = 'currencyCodeA'
    key_b = 'currencyCodeB'
    filtered_collection = [sub for sub in response.json() if sub[key_a] in search_list_a and sub[key_b] in search_list_b ]

    for currency in filtered_collection:
      print(f"{currencies_names[currency[key_a]]}/{currencies_names[currency[key_b]]}  buy: {currency['rateBuy']} / sell: {currency['rateSell']}")
  else:
    print(f"{url} cannot be loaded {response.status_code}")
  print('-------------------------------')

privat_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
monobank_url = 'https://api.monobank.ua/bank/currency'
get_currencies_information_pb(privat_url, 'PRIVAT')
get_currencies_information_mono(monobank_url, 'MONO')










# a = '33'
# b = '55'
#
#
# print(a + b)


# a = 'Hello, world!'
# print(type(a))
# print(*dir(a), sep='\n')

# for key, vol in enumerate(a, start=1):
#     print(key, '->', vol)


# print(a.strip())
# print(a)
# b = a
# a += 'hi!'
# print(id(a), a)
# print(id(b), b)













# a = 55
# b = 56
# print(f'{a} більше {a} ніж {b}! hjgjlglkj kjkljlk {b}')

# a = 4
# b = 5
# print(type(a), a)
# print(type(b), b)
# c = a ** (1/2)
# print(type(c), c)



# print(round(4.5))





# import requests
# from bs4 import BeautifulSoup as BS
#
#
# url = 'https://mon.gov.ua/ua'
# page = requests.get(url)
# print(page.status_code)
#
# soup = BS(page.text, 'html.parser')
# # soup = soup.find('div', class_='news-block')
# # print(soup.prettify())
# # articles = soup.find_all('article')
# # # print(articles[1])
# # for el in articles:
# #     print(el.div.text)
# #     print(el.span.text)
# #     print(el.a['href'])
# #     print('='*80)
#
#
# all = soup.find_all('a')
# for n, i in enumerate(all, start=1):
#     print('.'*80)
#     print(n, ':')
#     if i['href'].startswith('/'):
#         print(i[url+'href'])
#     else:
#         print(i['href'])






# def prn(x: list):
#     ###### print of matrix #######
#     for row in x:
#         print(*row, sep='\t')





# n, m = 4, 5
# # a = [[0] * m] * n
# a = [[0] * m for i in range(n)]
# prn(a)
# print()
# a[1][1] = 9
# prn(a)

# print()

# prn([[i * j for j in range(1, 11)] for i in range(1, 11)])





# a = 'abc'
# print(a)
# print(id(a))
# a = list(a)
# print(a)
#
# # a.pop(1)
# c = a.pop(1)
# print(a)
# print(c)


# a = [1, 2, 3]
# b = [5, 6, 7]
# print(id(a))
# # print(a+b)
# a.append(b)
# a.extend(b)
# # a += b
# print(a)
# print(id(a))









# a = 5
# b = 5
# c = 5
# print(id(a))
# print(id(b))
# print(id(c))











# a = 'aaabbbccc'
# print(id(a))
# a.replace('b', 'f')
# a = a.replace('b', 'f')
# print(id(a))
# # print(id(b))
# print(a)
# # print(b)
# a, b = 9, 0
# print(id(a))
# print(id(b))
# a, b = 6, 6
# print(id(a))
# print(id(b))
#



# a = [1, 2, 3, 4]
# # a.append([666, 888, 999])
# # a.extend([666, 888, 999])
# a += [666, 888, 999]
# a = 0
# b = 5
# print(a, b)
# a, b = 777, 'jgjk'
# print(a, b)









# from userfunc import foo as F
#
#
# l = [-1, -2, 3, -4]
#
# l1 = list(map(F, l))
# l2 = list(zip(l, l1))
# print(l)
# print(l1)
# print(l2)




# a = 'aacdef'
# a.replace('a', 'R')
# print(a)
#
# l = [1, 2, 3, 4]
# l.append(7)
# print(l)








# import json
#
# d = {'a': 123, '5': 989, 7: 890}
#
# t = json.dumps(d)
# print(d)
# print(t)

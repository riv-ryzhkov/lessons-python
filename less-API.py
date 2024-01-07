
# GET - получение
# POST - создание(получение авторизированной информации)
# PUT - обновление
# DELETE - удаление

#       pip install requests
#
import requests
import json


# response = requests.get('http://127.0.0.1:8000/api/url/')
# response = requests.get('http://127.0.0.1:8000/users/')
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Rome&units=metric&APPID=b18eeec4ac22e23cfd6a45375dd0cf90')

# print(response.text)
print(response.json())
text = json.dumps(response.json(), indent=4)
# text = json.dumps(response.json())
print(text)
print('=' * 80)
print(response.json()['weather'])
print(response.json()['weather'][0]['main'])
print(response.json()['weather'][0]['description'])
print(response.json()['main']["feels_like"])

# for i in response.json():
#     w = json.dumps(i, indent=4)
#     print(w)


# print(*dir(response), sep='\n')
# inx = response.url.find('/', 8)
# print(inx)
# host_url = response.url[:inx+1]
# short_url = response.url[inx+1:]
# print(host_url)
# print(short_url)
# breakpoint()


# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Rome&units=metric&APPID=b18eeec4ac22e23cfd6a45375dd0cf90', timeout=3)
# #
# # print(r)
# #
# # # print(*dir(r))
# # # print(*dir(r), sep='\n')
# print(r.url)
# # print(r.status_code)
# print('status :', r.status_code)
# print(r.text)
# # print(type(r))
# print(type(r.text))
# # print(r.text[68:73])
# # # print(type(r.text))
# # # print(r.text[90:99])
# print(type(r.json()), r.json())
# print(r.json()['weather'][0]['main'])
# print(r.json()['weather'][0]['description'])

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# r = requests.get('https://api.github.com/events', timeout=3)
# print('status :', r.status_code)
# print('headers :', r.headers)
# print('type-headers :', type(r.headers))
# # print(*dir(r.headers), sep='\n')
# print('Server :', r.headers['Server'])
# print('Date', r.headers['Date'])
#
# for key, val in r.headers.items():
#     print(key, ':', val)


# for key, val in r.headers.items():
#     print(key, ':', val)

# print(*dir(r), sep='\n')
# print(type(r.text))
# print(r.text)
# print(r.text[54:62])

# print('get_text :', r.text[8:19]) # 19255650776
# print(type(r.json()))

# print('get_json :', type(r.json()), *r.json(), sep='\n')
# print('get_json :', type(r.json()[3]), r.json()[3])
#
# d1 = r.json()[5]

# print(type(d1))
# print(d1)
# print(*d1)
# print('keys', d1.keys())
# t = tuple(d1.keys())
# print(type(t))
# print(t[0])
# print('keys', *dir(d1.keys()), sep='\n')
# print('values', d1.values())
# print('items', d1.items())

# for key, vol in d1.items():
#     print(key, ':', vol)


# w = json.dumps(r.json()[3], indent=4)
# print(w)


# for key, val in r.json()[3].items():
#     print(key, ':', val)

# print('get_json :', r.json())
# print('get_json :', r.json()[0])
# print(r.json()[0]['type'])
# print('get_json :', r.json()[0]['id'])
# print('get_json :', r.json()[0]['type'])



# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
#
# r = requests.get('https://httpbin.org/get', params=payload)

# print(isinstance(r.json(), dict))
# print(type(r.json())==dict)

# print(r.url)

# r = requests.get("https://httpbin.org/get?key1=value1&key2=value2&key2=value3")
# print('url :', r.url)
# print(type(r.json()))
# print(type(r.text))
# print(r.text)
#
# # print(*dir(r.text), sep='\n')
# print(r.text[27:33])
# print(r.json()['args']['key2'])
# print('='*80)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r = requests.get('https://api.github.com/events')
# # print(type(r))
# print(*dir(r), sep='\n')
# print('encodind :', r.encoding)
# print('content :', r.content)
# print(type(r.json()))
# print(r.json())
# print('json :', type(r.json()[0]), r.json()[0])
# for key, vol in r.json()[0].items():
#     print(key, ':', vol)
# print(*dir(r), sep='\n')

# r = requests.get('https://api.github.com/events')
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
# print(r.raw.read(7))

# !!!!!!!!!!!!!!!!!!!!!!!!!

# response = requests.get("https://httpbin.org/get?key1=value1&key2=value2")

# response = requests.get('https://api.github.com/events')
# print(response.text)
# print('type :', type(response.json()))
# print(*dir(response.json()), sep='\n')
# print('type-headers :', type(response.headers))
# # print(dir(response.headers))
# print(response.headers)
# # print(*dir(response), sep='\n')
# for key, value in response.headers.items():
#     print(key, ':', value)


# print('type-text :', type(response.text))
# print('text :', response.text)
# print(isinstance(response.text, str))
# print(type(response.text)== str)
# print(type(response.text))
# for i in range(len(response.json())-1):
#     print(i+1, ': type-json :', type(response.json()[i]))
#     print('json :', response.json()[i])
# print('json :', response.json()[i].get('args'))
# print(isinstance(response.json(), list))
# print(*dir(response.headers), sep='\n')
# print(*dir(response.json()), sep='\n')
# print(*dir(response.text), sep='\n')
# print(response.json()[0])
# print(isinstance(response.json()[0], dict))
#
# print(*dir(response.json()[0]), sep='\n')




# ======================== POST ===================
# data = {'key': 'value', 'key1': 'value1'}
# # # r = requests.post('https://httpbin.org/post', data=data)
# r = requests.post('https://httpbin.org/post?page=page1', data=data)
# # #
# print(r.url)
# print('type :', type(r.text))
# print('post_text :', r.text)
# #
# print('type-json', type(r.json()))
# print('json', r.json())
# print(json.dumps(r.json(), indent=4))
# # # #
# # #
# print('get_json :', r.json())
# # print('type :', type(r.json()))
# # print('inst :', isinstance(response.json(), dict))
# print('get_json_form :', r.json()['form'])
# print('get_json_headers :', r.json()['headers'])
# print('get_json_headers_Accept :', r.json()['headers']['Accept-Encoding'])



# ==================== PUT =========================
# d = {'key': 'value', 'key1': 'value2'}
# # r = requests.put('https://httpbin.org/put', data=d)
# r = requests.put('https://httpbin.org/put?page=page1', data={'key': 'value', 'key1': 'value2'})
# # print('put_text :', r.text)
# print(json.dumps(r.json(), indent=4))
# print('url :', r.url)
# print('get_json :', r.json())
# print('get_json_form :', r.json()['form'])

# ==================== DELETE ===================
# r = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete?page=page1', data={'key': 'value'})
# print('delete_text :', r.text)
# print('url :', r.url)
# print(r.json())

# breakpoint()

# params = {
#     'key': "u2JnV5UpCmumAYaETsLxLUc7ctHM84bjazoehWO8HiwM"
# }

####################################################################
#### OIL PRICE #####################################################
####################################################################

import requests
import json
#
#
# url = 'https://api.oilpriceapi.com/v1/prices/latest'
# headers = {
#   'Authorization': 'Token 96b90c2a2bf598680d40989ab38d54ea',
#   'Content-Type': 'application/json'
# }
#
# response = requests.get(url=url, headers=headers)
# print('url :', response.url)
# # print(*dir(response), sep='\n')
# # print('type-headers :', type(response.headers))
# # for key, vol in response.headers.items():
# #     print(key, ':', vol)
# # print('.'*80)
# print('type-json :', type(response.json()))
# # print('json :', response.json())
# res = response.json()
# print(json.dumps(res, indent=4))
# print('Price of oil is :', res['data']['price']*1.02, '$USA')

# #

# # ####################### MONOBANK ###################
import requests
import datetime


# url = 'https://api.monobank.ua/bank/currency'

# response = requests.get(url)
# # # response = requests.get('https://api.monobank.ua/bank/currency')
# res = response.json()
# print(json.dumps(res, indent=4))
# print(response.json())

# currencyCodeA	980  гривня
# currencyCodeB	840  долл США
# currencyCodeA	978  євро



# response = requests.get(url)
# print(response.json())
#
# r = requests.get(url)
# print(r.json())
# print('продаж доллар США:', r.json()[0]['rateSell'])
# print('купівля доллар США:', r.json()[0]['rateBuy'])
# print('продаж EURO:', r.json()[1]['rateSell'])
# print('купівля EURO:', r.json()[1]['rateBuy'])
#
#
# res = r.json()
# for i in range(len(res)):
#     for key, vol in res[i].items():
#         print(key, ':', vol)
#     print('.'*80)
#
# #
# response = requests.get(url)
# # print(*dir(response), sep='\n')
# print(response.text)
#
# print(response.status_code)
# print(response.json())
# print('response.text      : ', type(response.text))
# print('response.json()[0] : ', type(response.json()[0]))
# for i in response.json():
#     for key, value in i.items():
#         if key == 'date':
#             print(key, datetime.datetime.fromtimestamp(value), sep='\t')
#         else:
#             print(key, value, sep='\t')
#         # print(key, value, sep='\t')
#     print('-' * 80)


#!!!!!!!!!!!!!!!!!!!!!!
##########################################################
################### PRIVAT BANK#####################
##########################################################
# import requests
#
#
# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
#
# response = requests.get(url)
#
# print(response.status_code)
# res = response.json()
# print(type(res))
# print(res)
# print(res[0]['sale'])
# for i in res:
#     print(json.dumps(i, indent=4))
# for i in res:
#     print('.'*80)
#     for key, vol in i.items():
#         print(key, ':', vol)
# print('='*80)

########################################################
#                             NBU
# url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
########################################################


#######################################################
################## open-weather #######################
#######################################################
# import requests
# import json
# from datetime import datetime
#
#
# url = 'https://api.openweathermap.org/data/2.5/weather'
# params = {"id": "524901",
#           "appid": "fdd717a05cc211b145bfadd1e754f749",
#           "q": input('Input city and country with "," : '),
#           }
#
# response = requests.get(url, params=params)
# print(response.url)
# print(response.status_code)
# print(response.json())
# res = response.json()
# print('.'*80)
# # for key, vol in res.items():
# #     print(key, '\t:', vol)
# print(f"The weather in {res['name']} :")
# w = res['weather'][0]
# t = res['main']
# print('main        :', w['main'])
# print('temperature :', int((t['temp']-273.15)*100)/100)
# print('feels_like  :', int((t['feels_like']-273.15)*100)/100)
# print('temp_min    :', int((t['temp_min']-273.15)*100)/100)
# print('temp_max    :', int((t['temp_max']-273.15)*100)/100)
# print('pressure    :', t['pressure'], 'MPa')
# print('description :', w['description'])
# print('visibility  :', str(res['visibility']/100) + '%')
# print('clouds      :', res['clouds']['all'], '%')
# print('wind :')
# print('\t', 'speed :', res['wind']['speed'])
# print('\t', 'deg   :', res['wind']['deg'])
# print('time   :', datetime.fromtimestamp(res['dt']))
#

################################################################
# import requests
#
# url = "https://aerisweather1.p.rapidapi.com/sunmoon/dnipro,ua"
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "aerisweather1.p.rapidapi.com"
# }
# r = 'GET'
# response = requests.request(r, url, headers=headers)
#
# # print(*dir(requests), sep='\n')
# res = response.json()
# print(json.dumps(res, indent=4))

####################################
#
# import requests
#
# url = "https://footapi7.p.rapidapi.com/api/search/champions"
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "footapi7.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.json())
# res = response.json()
# print(json.dumps(res, indent=4))



###### COVID ##########################
#######################################
#
# import requests
# import json
#
# url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
#
# country = input('Input country : ')
# querystring = {"country": country}
#
# headers = {
# 	"X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com",
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.text)
#
#
# result = response.json()
# print(result)
# print(result['data'])
# for key, val in result['data'].items():
#     print(key, ':', val)

#########################################
#######################################
#### SPORT ############################
# #######################################
# import requests
# import json
#
# url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
#
# querystring = {"page": "1"}
#
# headers = {
#     'x-rapidapi-host': "sportscore1.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.json())
#
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)

#######################################
#### BOOKING  #########################
#######################################
#
# import requests
# import json
#
#
# url = "https://booking-com.p.rapidapi.com/v1/hotels/room-list"
#
# querystring = {"locale": "en-gb", "checkin_date": input('checkin_date (YYYY-MM-DD) = '), "checkout_date": input('checkout_date (YYYY-MM-DD) = '), "currency": "USD", "hotel_id": "1676161", "adults_number_by_rooms": "3,1", "units": "metric", "children_number_by_rooms": "2,1", "children_ages": "5,0,9"}
#
# headers = {
#     'x-rapidapi-host': "booking-com.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.text)
# # print(response.json())
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)



#######################################
### POPULATION ########################
#######################################
#
# import requests
# import json
#
#
# url = "https://world-population.p.rapidapi.com/population"
#
# country = input('Input name of country : ')
# querystring = {"country_name": country}
#
# headers = {
#     'x-rapidapi-host': "world-population.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
# #
# # url1 = '?country_name=' + country
# # response = requests.request("GET", url, headers=headers, params=querystring)
# response = requests.get(url, headers=headers, params=querystring)
# # response = requests.get(url+url1, headers=headers)
# #
# print(response.url)
# #
# # print(response.text)
# print(response.json())
# # resp_print = json.dumps(response.json(), indent=4)
# # print('resp_print : ', type(resp_print))
# # print(resp_print)
# # print('The population in', country, 'is', response.json()['body']['population'], '!')
# # # #




#######################################
######### NEWS ######################
#######################################

# import requests
# import json
#
#
# url = 'https://newsapi.org/v2/everything'
#
# param = {'q': 'Ukraine',
#        'from': '2023-11-24',
#        'sortBy': 'popularity',
#        'apiKey': 'ae21841592fd475d808076dda8f49d29'}
#
# i = input('Введіть те, що вас цікавить :')
# if i:
#     param['q'] = i
#
# response = requests.get(url, params=param)
#
# print(response.url)
#
# # print(*dir(response), sep='\n')
# # print(response.status_code)
# # print(response.text)
# # print(response.url)
# resp_json = response.json()
# # print(json.dumps(resp_json, indent=4))
# # print('resp_json : ', type(resp_json))
# # # # # #
# # resp_print = json.dumps(response.json(), indent=4)
# # # # # # # print('resp_print : ', type(resp_print))
# # # print(resp_print)
# for i in range(10): #
#     print()
#     print(str(i+1), 'article :')
#     print('.' * 80)
#     print('author   :', resp_json['articles'][i]['author'])
#     print('title    :', resp_json['articles'][i]['title'])
#     print('descrip  :', resp_json['articles'][i]['description'])
#     print('date publ:', resp_json['articles'][i]['publishedAt'])
#     print('url      :', resp_json['articles'][i]['url'])
#     print('=' * 80)
#




####################################################################
#################### ПРИМЕР (случайные данные) #################
# import requests
# import json
#
#
# response = requests.get("https://randomuser.me/api/")
#
# # # print(response.text)
# # # print(response.json())
# # # print(type(response.json()))
# resp_json = json.dumps(response.json(), indent=4)
# # #
# # print('response.json() : ', type(response.json()))
# # print('      resp_json : ', type(resp_json))
# # print(resp_json)
# # #
# # #
# # # print(response.json()['results'][0]['name'])
# print('=' * 60)
# print('     title : ', dict(response.json()['results'][0]['name'])['title'])
# print('first name : ', dict(response.json()['results'][0]['name'])['first'])
# print(' last name : ', dict(response.json()['results'][0]['name'])['last'])
# print(' country   : ', dict(response.json()['results'][0]['location'])['country'])
# print('       age : ', dict(response.json()['results'][0]['dob'])['age'])
# print('Date of bth: ', dict(response.json()['results'][0]['dob'])['date'])
# print('     email : ', dict(response.json()['results'][0])['email'])
# print('     photo : ', dict(response.json()['results'][0])['picture']['large'])
# print('=' * 60)


################################################################
########## GOOGLE - TRANSLATOR #########################
################################################################

import requests


# # print(*dir(requests), sep='\n')
# #
# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
# #
# payload = "q=Hello%2C%20world!&target=fr&source=en"
#
# source = input('Choose source language (for example: en, fr, es ...) : ')
# target = input('Choose target language (for example: ru, en, fr, es ...) : ')
# payload = 'q={}&target={}&source={}'.format(input('Input text : '), target, source)
# headers = {
#     'content-type': "application/x-www-form-urlencoded",
#     'accept-encoding': "application/gzip",
#     'x-rapidapi-host': "google-translate1.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
#
# response = requests.request("POST", url, data=payload, headers=headers)
# # response = requests.post(url, data=payload, headers=headers)
# #
# translate_res = response.json()
# # print(json.dumps(translate_res, indent=4))
# translated_text = translate_res["data"]["translations"][0]["translatedText"]
# #
# # # print(response.text)
# # # translated_text = response.text[44:len(response.text)-5]
# # # #
# print(translated_text)


################################################################
######### WEB-CAM ##################################
################################################################
# import requests
# import json
#
#
# url = "https://webcamstravel.p.rapidapi.com/webcams/list/nearby=%7Blat%7D,%7Blng%7D,%7Bradius%7D"
#
# querystring = {"lang": "en", "show": "webcams:image,location"}
#
# headers = {
#     'x-rapidapi-host': "webcamstravel.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.url)
# # print(response.text)
# # resp_json = json.dumps(response.json(), indent=4)
# # print(resp_json)
# res = response.json()
# # print(json.dumps(res, indent=4))
# for i in range(10):
#     if res['result']['webcams'][i]['location']['country'] != 'Russia':
#         print(i+1, ':', res['result']['webcams'][i]['image']['current']['preview'])
#         print(res['result']['webcams'][i]['location']['country'])

################################################################
############# PYTHONANYWHERE ###############################
################################################################
# import requests
# import json
#
#
# res = ''
# # url = "http://127.0.0.1:8000/api/v3/book/20/"
# for i in range(1, 5):
#     url = f"http://riv2.pythonanywhere.com/api/v3/book/?page={i}"
#
#     # headers = {
#     # 'Authorization': "Token f21dba2f6a67055deaa3e9b6859964abe124fa4f"
#     # }
#     response = requests.request("GET", url)
#     # response = requests.request("GET", url, headers=headers)
#     resp_print = json.dumps(response.json(), ensure_ascii=False, indent=4)
#     res += resp_print
#
# print(res)

##########################################
############ coordinats ##################
##########################################
# import requests
#
#
# response = requests.get('https://ipinfo.io/json')
#
# # print(response.text)
# #
# data = response.json()
# latitude = data['loc'].split(',')[0]
# longitude = data['loc'].split(',')[1]
# print('longitude :', longitude)
# print('latitude  :', latitude)
# print('city      :', data['city'])













# ???????????????????????????????????????????????????????
################### ВАЛЮТЫ С САЙТА www.cbr.ru #################33
# import requests
# import pandas as pd
# import xml.etree.ElementTree as et
# #
# v_date = '17.11.2021'
# # # Адрес api метода для запроса get
# url = 'https://www.cbr.ru/scripts/XML_daily.asp'
# params = {
#     'date_req': v_date
# }
# # # Отправляем get request (запрос GET)
# response = requests.get(url, params)
# print(list(response))
# tree = et.ElementTree(et.fromstring(response.text))
# root = tree.getroot()
# df_cols = ["date", "numcode", "charcode", "nominal", "name", "value"]
# rows = []
# for node in root:
#     s_numcode = node.find("NumCode").text if node is not None else None
#     s_charcode = node.find("CharCode").text if node is not None else None
#     s_nominal = node.find("Nominal").text if node is not None else None
#     s_name = node.find("Name").text if node is not None else None
#     s_value = node.find("Value").text if node is not None else None
#
#     rows.append({"date": v_date, "numcode": s_numcode,
#                  "charcode": s_charcode, "nominal": s_nominal,
#                  "name": s_name, "value": s_value})
# df = pd.DataFrame(rows, columns=df_cols)
# print(df.head())

############### НЕ РАБОТАЕТ (нужен логин и пароль) ###########
#######################################################################
# # Импортируем библиотеку requests
# import requests
#
# # Адрес api метода для запроса get
# url_param = "https://api-metrika.yandex.net/stat/v1/data"
# # Задаем параметры для API
# api_param = {
#     "ids": "5251515",
#     "metrics": "ym:s:users,ym:s:visits,ym:s:pageviews,ym:s:bounceRate,ym:s:pageDepth,ym:s:avgVisitDurationSeconds",
#     "dimensions": "ym:s:date,ym:s:<attribution>TrafficSource,ym:s:<attribution>SourceEngine,ym:s:gender",
#     "date1": "10daysAgo",
#     "date2": "yesterday",
#     "sort": "ym:s:date",
#     "accuracy": "full",
#     "limit": 5
# }
# header_params = {
#     'GET': '/management/v1/counters HTTP/1.1',
#     'Host': 'api-metrika.yandex.net',
#     'Authorization': 'OAuth AgAAlkjlkjKAa976ZB-rXh-t-ookfJJcMP979ZU0',
#     'Content-Type': 'application/x-yametrika+json'
# }
# # Отправляем get request (запрос GET)
# response = requests.get(
#     url_param,
#     params=api_param,
#     headers=header_params
# )
# result = response.json()
# print(result)
# query = result['query']
# data = result['data']
# print(query)
# print('======================')
# print(data)
#########################################################################

##########################################################################


################## INF ##############
# # Адрес api метода для запроса get
# API_KEY = '5ad2ecb53d794e6885f8de4bfe6f855d'
# url = 'https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely'
# url = 'https://api.weatherbit.io/v2.0/current?key=API_KEY'


#
# import requests
#
#
# r = requests.get('https://riv2.pythonanywhere.com/api/v1/booklist/', timeout=3)
#
# print('status :', r.status_code)
#
# for key, val in r.headers.items():
#     print(key, ':', val)
# print('='*80)
# d1 = json.dumps(r.json(), indent=4)
# print(d1)
# print('='*80)
# print('get_json :', type(r.json()), *r.json(), sep='\n')
# print('get_json :', type(r.json()[0]), r.json()[0])
# for key, val in r.json()[1].items():
#     print(key, ':', val)
#=======================================================


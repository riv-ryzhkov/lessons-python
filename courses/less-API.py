import requests
import json

# # ####################### MONOBANK ###################
# import requests
# import datetime
#
#
# url = 'https://api.monobank.ua/bank/currency'
#
# r = requests.get(url)
# print('продаж доллар США: ', r.json()[0]['rateSell'])
# print('купівля доллар США:', r.json()[0]['rateBuy'])
# print('продаж EURO:       ', r.json()[1]['rateSell'])
# print('купівля EURO:      ', r.json()[1]['rateBuy'])
#
#
##########################################################
################### PRIVAT BANK#####################
##########################################################
# import requests
#
#
# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# # NBU
# # url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
# response = requests.get(url)
#
# res = response.json()
# for i in res:
#     print('.'*80)
#     for key, vol in i.items():
#         print(key, '\t:', vol)
# print('='*80)

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
# res = response.json()
# print('.'*80)
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


################################################################
########## GOOGLE - TRANSLATOR #########################
################################################################

# import requests
#
#
# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
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
# translate_res = response.json()
# translated_text = translate_res["data"]["translations"][0]["translatedText"]
# print(translated_text)

#################################################################












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


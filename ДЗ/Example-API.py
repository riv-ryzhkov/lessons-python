
# GET - получение
# POST - создание(получение авторизированной информации)
# PUT - обновление
# DELETE - удаление

#
import requests


# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=ЗДЕСЬ НЕОБХОДИМО ВСТАВИТЬ ВАШ APPID ПОЛУЧЕННЫЙ ПОСЛЕ РЕГИСТРАЦИИ НА САЙТЕ', timeout=3)
# print('status :', r.status_code)
# print(*dir(r), sep='\n')

# r = requests.get('https://api.github.com/events', timeout=3)
# print('status :', r.status_code)
# print('headers :', r.headers)
# print('Server :', r.headers['Server'])
# print('Date :', r.headers['Date'])
# for key, val in r.headers.items():
#     print(key, ':', val)
# print(type(r.text), r.text)
# print('get_text :', r.text[8:19]) # 19255650776
# print('get_json :', type(r.json()), *r.json(), sep='\n')
# print('get_json :', type(r.json()[0]), r.json()[0])
# for key, val in r.json()[1].items():
#     print(key, ':', val)

# print('get_json :', r.json())
# print('get_json :', r.json()[0])
# print(r.json()[0]['type'])
# print('get_json :', r.json()[0]['id'])
# print('get_json :', r.json()[0]['type'])



# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('https://httpbin.org/get', params=payload)
# print('url :', r.url)
# print(r.text)
# print(r.text[5:9])
# print('='*80)


# r = requests.get('https://api.github.com/events')
# print('encodind :', r.encoding)
# print('content :', r.content)
# print('json :', type(r.json()[0]), r.json()[0])
# print(*dir(r), sep='\n')

# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
# print(r.raw.read(55))




# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(r.url)
# print('type :', type(r.text))
# print('post_text :', r.text)
#
#
# print('get_json :', r.json())
# print('type :', type(r.json()))
# print('get_json :', r.json()['form'])
# print('get_json :', r.json()['headers'])
# print('get_json :', r.json()['headers']['Accept-Encoding'])


#
#


# r = requests.put('https://httpbin.org/put', data={'key': 'value', 'key1': 'value2'})
# # print('put_text :', r.text)
# print('url :', r.url)
# print('get_json :', r.json())
# print('get_json :', r.json()['form'])
#
# r = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
# print('delete_text :', r.text)
# print('url :', r.url)
#


####################################################################
#### OIL PRICE #####################################################
####################################################################

import requests
import json


# url = 'https://api.oilpriceapi.com/v1/prices/latest'
# headers = {
#   'Authorization': 'ЗДЕСЬ НУЖНО ВСТАВИТЬ СВОЙ Token ПОЛУЧЕННЫЙ ПОСЛЕ РЕГИСТРАЦИИ НА САЙТЕ',
#   'Content-Type': 'application/json'
# }
#
# response = requests.get(url=url, headers=headers)
# print(response.url)
# print(response.headers)
# print(response.json())
# res = response.json()
# print(json.dumps(res, indent=4))
# print('Price of oil is :', res['data']['price']*1.02, '$USA')


# ####################### MONOBANK ###################
# import requests
# import datetime
#
#
# url = 'https://api.monobank.ua/bank/currency'
#
# response = requests.get(url)
# # print(*dir(response), sep='\n')
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
#     print('-' * 80)



#######################################################
################## open-weather #######################
# import requests
# import json
#
#
# url = "https://community-open-weather-map.p.rapidapi.com/weather"
#
# city = input('City : ')
# # querystring = {"q":"London,uk", "lat":"0", "lon":"0", "callback": "test", "id":"2172797","lang":"null","units":"imperial","mode":"xml"}
# querystring = {"q": city, "lat":"0", "lon":"0", "callback": "test", "id":"2172797","lang":"null","units":"imperial","mode":"xml"}
#
# headers = {
#     'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
#
# # print(response.text)
#
# resp = response.text[5:len(response.text)-1]
# # # print(resp.json())
# # print(type(resp), resp)
# pr_json = json.loads(resp)
# print('Weather is :', pr_json['weather'][0]['main'])
# print(type(pr_json), pr_json)
# for key, val in pr_json.items():
#     print(key, ' :', val)


############################################
# import requests
# import json
#
# url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
#
# querystring = {"lon": "38.5", "lat": "-78.5"}
#
# headers = {
#     'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# # print(response.text)
# print_response = response.json()
# print(json.dumps(print_response, indent=4))
#
#



#######################################################
# import requests
# import json
#
# url = "https://community-open-weather-map.p.rapidapi.com/weather"
#
# # querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}
# # querystring = {"q":"Kiev,ua","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}
# # querystring = {"q":"Dnipro,ua","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"json"}
# querystring = {"q": input('Input city and country with "," : '),"lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial"}
#
# headers = {
#     'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
# # print('response.text : ', type(response.text))
# text = response.text[5:len(response.text)-1]
# # print(text)
# resp_json = json.loads(text)
# print(resp_json)
# # print('resp_json : ', type(resp_json))
# # #
# resp_print = json.dumps(resp_json, indent=4)
# # print('resp_print : ', type(resp_print))
# # print(resp_print)
# print('The weather is <', resp_json['weather'][0]['main'], '>')
# # #
# #
# #
# #

###### COVID ##########################
#######################################
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
# 	"X-RapidAPI-Key": "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# # print(response.text)
# result = response.json()
# # print(result['data'])
# for key, val in result['data'].items():
#     print(key, ':', val)

#########################################
#
# import requests
# import json
#
# # print(*dir(requests), sep='\n')
# url = "https://covid-19-data.p.rapidapi.com/country/code"
#
# querystring = {"code": "ua"}
# querystring = {"code": input('Code of country : ')}
#
# headers = {
#     'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.status_code)
# # print(response.url)
# # print('  response.text : ', type(response.text))
# # print('text :', response.text)
# # print()
# print('response.json() : ', type(response.json()))
# print('json :', type(response.json()), response.json())
# # print()
# # # text = response.text[1:len(response.text)-1]
# # # resp_json = json.loads(text)
# resp_json = response.json()[0]
# print(resp_json)
# print('resp_json : ', type(resp_json))
# # #
# resp_print = json.dumps(resp_json, indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)


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
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# # print(response.json())
#
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)

#######################################
#### BOOKING  #########################
#######################################

# import requests
# import json
#
#
# url = "https://booking-com.p.rapidapi.com/v1/hotels/room-list"
#
# querystring = {"locale":"en-gb","checkout_date":"2022-06-10","currency":"AED","hotel_id":"1676161","adults_number_by_rooms":"3,1","checkin_date":"2022-06-09","units":"metric","children_number_by_rooms":"2,1","children_ages":"5,0,9"}
#
# headers = {
#     'x-rapidapi-host': "booking-com.p.rapidapi.com",
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
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
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# # print(response.text)
# # print(response.json())
# resp_print = json.dumps(response.json(), indent=4)
# # print('resp_print : ', type(resp_print))
# # print(resp_print)
# print('The population in', country, 'is', response.json()['body']['population'], '!')
# # #
#



#######################################
######### NEWS ######################
#######################################
#
# import requests
# import json
#
#
# url = ('https://newsapi.org/v2/everything?'
#        'q=Ukraine&'
#        'from=2022-05-29&'
#        'sortBy=popularity&'
#        'apiKey=ВАШ ПЕРСОНАЛЬНЫЙ КЛЮЧ ПОСЛЕ РЕГИСТРАЦИИ НА САЙТЕ')
#
# response = requests.get(url)
#
# # print(dir(response))
# # print(response.status_code)
# # print(response.url)
# resp_json = response.json()
# # print(resp_json)
# # print('resp_json : ', type(resp_json))
# #
# # resp_print = json.dumps(resp_json, indent=4)
# # # print('resp_print : ', type(resp_print))
# # # print(resp_print)
# for i in range(10):
#     print()
#     print(str(i+1), 'article :')
#     print('.' * 80)
#     print('author   :', resp_json['articles'][i]['author'])
#     print('title    :', resp_json['articles'][i]['title'])
#     print('descrip  :', resp_json['articles'][i]['description'])
#     print('date publ:', resp_json['articles'][i]['publishedAt'])
#     print('url      :', resp_json['articles'][i]['url'])
#     print('=' * 80)





####################################################################
#################### ПРИМЕР (случайные данные) #################
# import requests
# import json
#
#
# response = requests.get("https://randomuser.me/api/")
#
# resp_json = json.dumps(response.json(), indent=4)
#
# # print('response.json() : ', type(response.json()))
# # print('      resp_json : ', type(resp_json))
# print(resp_json)
#
#
# print(response.json()['results'][0]['name'])
# print('=' * 60)
# print('     title : ', dict(response.json()['results'][0]['name'])['title'])
# print('first name : ', dict(response.json()['results'][0]['name'])['first'])
# print(' last name : ', dict(response.json()['results'][0]['name'])['last'])
# print('       age : ', dict(response.json()['results'][0]['dob'])['age'])
# print('Date of b  : ', dict(response.json()['results'][0]['dob'])['date'])
# print('     email : ', dict(response.json()['results'][0])['email'])
# print('     photo : ', dict(response.json()['results'][0])['picture']['large'])
# print('=' * 60)






################################################################
########## GOOGLE - TRANSLATOR #########################
################################################################
# import requests
#
# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
#
# # payload = "q=Hello%2C%20world!&target=ru&source=en"
#
# source = input('Choose source language (for example: en, fr, es ...) : ')
# target = input('Choose target language (for example: ru, en, fr, es ...) : ')
# payload = 'q={}&target={}&source={}'.format(input('Input text : '), target, source)
# headers = {
#     'content-type': "application/x-www-form-urlencoded",
#     'accept-encoding': "application/gzip",
#     'x-rapidapi-host': "google-translate1.p.rapidapi.com",
#     'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# # translate_res = dict(response.json())
# translate_res = response.json()
# # print(response.json())
# translated_text = translate_res["data"]["translations"][0]["translatedText"]
# #
# # print(response.text)
# # translate_text = response.text[44:len(response.text)-5]
# # #
# print(translated_text)


################################################################
######### WEB-CAM ##################################
################################################################
import requests
import json


url = "https://webcamstravel.p.rapidapi.com/webcams/list/nearby=%7Blat%7D,%7Blng%7D,%7Bradius%7D"

querystring = {"lang": "en", "show": "webcams:image,location"}

headers = {
    'x-rapidapi-host': "webcamstravel.p.rapidapi.com",
    'x-rapidapi-key': "ЗДЕСЬ АВТОМАТИЧЕСКИ ВСТАВИТСЯ ВАШ Token ПОЛУЧЕННЫЙ НА САЙТЕ"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
resp_json = json.dumps(response.json(), indent=4)
# print(resp_json)
# for i in range(10):
# 	if response.json()['result']['webcams'][i]['location']['country'] == 'Norway':
# 		print(i, ':', response.json()['result']['webcams'][i]['image']['current']['preview'])

################################################################

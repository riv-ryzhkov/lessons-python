# import requests
# import json
#
#
# url = 'https://riv2.pythonanywhere.com/api/v1/'
# response = requests.get(url)
# print(json.dumps(response.json(), indent=4))
#
#
#
# data = {
#     'login': 'admin',
#     'password': 'admin'
#     # 'host_url': 'https://www.figma.com/file/example107',
#     # # 'short_url': 'https://www.figma.com/12345',
#     # 'length': 15,
#     # # 'list_of_symbols': 'qwerty1234567890',
# }
#
# url = 'https://riv2.pythonanywhere.com/api/v1/'
# response = requests.get(url)
# print(json.dumps(response.json(), indent=4))
#
# url = 'https://riv2.pythonanywhere.com/api/v3/book/'
# response = requests.post(url, data=data)
#
# print(json.dumps(response.json(), indent=4))
#


import requests
import json


res = ''
# url = "http://127.0.0.1:8000/api/v3/book/20/"
for i in range(1, 5):
    url = f"http://riv2.pythonanywhere.com/api/v3/book/?page={i}"

    # headers = {
    # 'Authorization': "Token f21dba2f6a67055deaa3e9b6859964abe124fa4f"
    # }
    response = requests.request("GET", url)
    # response = requests.request("GET", url, headers=headers)
    resp_print = json.dumps(response.json(), ensure_ascii=False, indent=4)
    res += resp_print

print(res)
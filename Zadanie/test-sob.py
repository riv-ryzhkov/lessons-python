# transitions = [
#     ("A", "B"),
#     ("B", "C"),
#     ("C", "D"),
#     ("A", "E"),
#     ("C", "F"),
#     ("E", "C"),
#     ("C", "D"),
#     ("G", "H"),
#     ("D", "H")]
#
# starts = [el[0] for el in transitions]
# result = set()
#
#
# def search_for_destination(starting_dot):
#     for i in transitions:
#         if i[0] == starting_dot and i[1] not in starts:
#             result.add(i[1])
#         elif i[0] == starting_dot:
#             search_for_destination(i[1])
#
#
# search_for_destination("A")
# print(result)


import json
import requests


def post_clear_request(url, data):
    res = requests.delete('http://127.0.0.1:8000/api/')
    for el in data:
        response = requests.post(url, data=el)
    return response.json()

url = 'http://127.0.0.1:8000/api/'
data = [
    {
        'host_url': 'https://www.figma.com/file/example51',
        'short_url': 'https://www.figma.com/abcd51'
    },
    {
        'host_url': 'https://www.figma.com/file/example52',
        'short_url': 'https://www.figma.com/abcd52'
    },
    {
        'host_url': 'https://www.figma.com/file/example53',
        'short_url': 'https://www.figma.com/abcd53'
    },
]
post_clear_request(url, data)


# data = {
#     'host_url': 'https://www.figma.com/file/example40',
#     'short_url': 'https://www.figma.com/12345',
#     'length': '15gjk',
#     'list_of_symbols': 'qwerty1234567890',
# }
# # response = requests.post('https://httpbin.org/post', data=data)
# # response = requests.post('http://127.0.0.1:8000/api/', data=data)
response = requests.get('http://127.0.0.1:8000/api/urls/')
# res = requests.delete('http://127.0.0.1:8000/api/')
# response = requests.post('http://127.0.0.1:8000/api/', data=data)
# for i in range(10):
#     data = {
#         'host_url': f'https://www.figma.com/file/example{i}',
#         # 'short_url': 'https://www.figma.com/11111666',
#         'length': 15,
#         # 'list_of_symbols': 'qwerty12345',
#     }
#     response = requests.post('http://127.0.0.1:8000/api/', data=data)


# print(response.text)
print(response.json())
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
import requests
import csv
import json


def get_urls(get_url):
    response = requests.get(get_url)
    fields = ['host_url', 'short_url']
    my_dict = response.json()
    with open('tableurl.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields, delimiter=';')
        writer.writeheader()
        writer.writerows(my_dict)

def shorting_url(post_url):
    host_url = input('Input full URL for shorting, please. \n(for example, https://www.google.com) :')
    short_url = input('You can try to use your special short URL \n(input here) or press ENTER :')
    list_of_symbols = input('If you want to use special list of symbols for shorting, \ninput them here.'
                            '\nDefault list consists of latin letters and digits.'
                            '\nFor using default list press ENTER. :')
    length = input('Input length of coding part in short URL \nor press ENTER (default length = 8) :')
    data = {}
    if host_url:
        data['host_url'] = host_url
    if short_url:
        data['short_url'] = short_url
    if length:
        data['length'] = length
    if list_of_symbols:
        data['list_of_symbols'] = list_of_symbols
    response = requests.post(post_url, data)
    print(json.dumps(response.json(), indent=4))



post_url = 'https://rivcor.pythonanywhere.com/api/'
# post_url = 'http://127.0.0.1:8000/api/'
get_url = 'https://rivcor.pythonanywhere.com/api/urls/'
# get_url = 'http://127.0.0.1:8000/api/urls/'
todo = ''
while todo != '1' and todo != '2' and todo.lower() != 'n':
    print()
    todo = input('If you want to receive all table of the "host URL" and "short URL", input 1.\n'
                 'If you want to make shorting of your "host URL", input 2.\n'
                 'Input your choice, please! (1 or 2) : ')

    if todo == '1':
        print('All table of the "host URL" and "short URL" you can find in the file "tableURL.csv".')
        input('Input ENTER to start writing process...')
        get_urls(get_url)
    else:
        shorting_url(post_url)
    print('Done!...')
    print()
    todo = input('Would you like to continue? ("y" - Yes, "n" - NO)')






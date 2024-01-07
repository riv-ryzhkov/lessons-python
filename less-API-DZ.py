import requests


url_pr = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
url_mono = 'https://api.monobank.ua/bank/currency'

privat = requests.get(url_pr)
mono = requests.get(url_mono)

print('-'*50)
print('|                | PRIVAT   \t| MONOBANK \t|')
print('-'*50)
print('| DOLL USA  sale |', privat.json()[0]['sale'], '\t|', mono.json()[0]['rateSell'], '\t|')
print('| DOLL USA  buy  |', privat.json()[0]['buy'], '\t|', mono.json()[0]['rateBuy'], '\t|')
print('| EURO      sale |', privat.json()[1]['sale'], '\t|', mono.json()[1]['rateSell'], '\t|')
print('| EURO      buy  |', privat.json()[1]['buy'], '\t|', mono.json()[1]['rateBuy'], '\t|')
print('-'*50)




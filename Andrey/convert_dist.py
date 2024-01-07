import json


def conv_to_mm(index, value):
    res = value * index
    return res

def conv_to_index(index, value):
    res = value / index
    return res


coef = {
    'mm': 1,
    'm' : 100,
    'km' : 100000,
    'dm' : 10,
    'ft' : 304.8,
    'yd' : 914.399999999998,
    'inch' : 25.4
}


with open('data_dist.json', 'r') as file:
    data = json.load(file)

value = data['distance']['value']
index = data['distance']['unit']

distance = conv_to_mm(coef[index], value)
# print(data)
# print(distance, 'mm')
print(value, index, '->', end=' ')

index = data['convert_to']
result = conv_to_index(coef[index], distance)
print(result, index)
res = {'unit': index, 'value': value}

with open('data_conv.json', 'w') as file:
    json.dump(res, file)
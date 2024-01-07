import json


def func_sort(data_list, sort_by='', exclude_field='disabled', exclude_val=False):
    data_list = list(filter(lambda x: x[exclude_field] != exclude_val, data_list))
    print(data_list)
    data_list.sort(key=lambda x: x[sort_by])
    return data_list


with open('data_sort.json', 'r') as file:
    data = json.load(file)


print(type(data), data)
d1 = data['data']
d2 = data['condition']['sort_by'][0]
d3 = data['condition']['exclude'][0]
d33 = list(d3)[0]
d4 = d3[d33]
res = func_sort(d1, d2, d33, d4)
print(type(res), res)

result = {'result': res}
# print(result)

with open('data_sort_result.json', 'w') as file:
    json.dump(result, file)






def flatten_list(array):
    x = 0
    for i in arrey:
        if type(i) == list:
            i == flatten_list(i)
            x = 1
    if x == 0:
        return array



assert flatten_list([1, 2, 3, 4]) == [1, 2, 3, 4]
assert flatten_list([[1], [2, [3]], 4]) == [1, 2, 3, 4]
assert flatten_list([[1, [4, [5]]]]) == [1, 4, 5]


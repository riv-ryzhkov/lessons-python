b = '11111111111111'

def bin_to_dec(b='0'):
    if not all(char in "01" for char in b):
        print('Error text!')
    res = 0
    for i in range(-1, -len(b)-1, -1):
        k = i * -1
        res += int(b[i]) * 2**(k-1)
    return res


def dec_to_hex(d=0):
    if type(d) != int:
        print('Error')
    res = []
    hex_dict = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }
    while d:
        symbol = str(d%16)
        res += hex_dict[symbol]
        d //= 16
    return res


def dec_to_oct(d=0):
    if type(d) != int:
        print('Error')
    res = []
    oct_dict = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
    }
    while d:
        symbol = str(d%8)
        res += oct_dict[symbol]
        d //= 8
    return res


print('bin=', b)
d = bin_to_dec(b)
print('dec=', d)
h = dec_to_hex(d)
h = ''.join(h)
print('hex=', h)
o = dec_to_oct(d)
o = ''.join(o)
print('oct=', o)

# f = open('test.txt', 'w')      # w - write, r - read, a - append, b - binary
# f = open(input('Inp name of file : '), 'w')  # w -write, r - read, a - append, b - binary
# try:
#     f.write('''Line 1: Start of writing...\n''')
#     f.write('Line 2: Hello, Vasya!\n')
#     f.write('line 3: Text of the file\n')
#     f.write('line 4: Text of the file\n')
#     f.write('line 5: End of writing...\n')
#
#     # f.writelines([
#     #     'Line 1: Start of writing!!!!!!!!!!!!!!!!!!!...',
#     #     'Line 2: Hello, World!!!!!!!!!!!!!!\n',
#     #     'line 3: Text of the file!!!!!!!!!!!!!!\n',
#     #     'line 4: Text of the file!!!!!!!!!!!!!',
#     #     'line 5: End of writing!!!!!!!!!!!!!...'
#     # ])
#
#
# finally:
#     f.close()




# f = open('test.txt', 'r')
#
# try:
#     p1 = f.read(10)
#     p2 = f.read(10)
#     p3 = f.readline()
#     p4 = f.readline()
#     p5 = f.readlines()
#     p6 = f.readlines()
#     print(type(p1), p1)
#     print(type(p2), p2)
#     print(type(p3), p3)
#     print(type(p4), p4)
#     print(type(p5), p5)
#     print(type(p6), p6)
# finally:
#     f.close()




# # with open('test.txt', 'w') as f:
# with open(input('input name of file : '), 'w') as f:
#     f.write('''Line 1: +++++Start of writing...\n''')
#     f.write('Line 2: Hello, World!\n')
#     f.write('line 3: Text of the file\n')
#     f.write('line 4: +++++Text of the file\n')
#     f.write('line 5: End of writing...\n')





#
# with open('test.txt', 'r') as f2:
#     f0 = f2.read(2)
#     print(f0)
#     print(f2.read(3))
#     print('+' * 30)
#     print(f2.readline())
#     print('=' * 30)
#     print(f2.read())

###################################################

import json   # JavaScript Object Notation


data = {'name': 'Ivan', 'surname': 'Popov', 'age': 28, 777: 'Casino'}

# with open('test.json', 'w') as f:
#     # json.dump(data, f)
#     json.dump(data, f, indent=4)

# print(data)
#
# d1 = json.dumps(data, indent=4)
# print(type(d1), d1)

# d1 = json.dumps(data, indent=4)
# print(type(d1))
# print(d1)
# # # #
# # # #     print('\nWarning! 777 != "777" !!!!!!!!!\n')
# # # #


# with open('test.json', 'r') as file1:
#     k = json.load(file1) # file1 : test.json --> dict
#
#     print('k :', type(k), k)


# k1 = json.loads(d1)  # d1 type-str : k1 --> dict
# print('k1 :', type(k1), k1)

################################################

import pickle


data = {'Alice': 89, 'Bob': '5', 'Charly': 32, 777: 'Casino'}


# print('======== dumps ===========')
# print('Dictionary data : ', data)
#
#
# serial_data = pickle.dumps(data)
#
# print('serial_data :', type(serial_data))
# print(serial_data)
#
# received_data = pickle.loads(serial_data)
# print('received_data :')
# print(received_data, type(received_data))
# print('=' * 40)



# print()
# print('======== dump ===========')
# with open('test.pickle', 'wb') as file:
#     pickle.dump(data, file)
# # #
# with open('test.pickle', 'rb') as file:
#     pr = pickle.load(file)
#     print(pr, type(pr))


#######################################################################
import csv


# with open('test.csv', 'w', newline='') as file:
#
#     wr = csv.writer(file, delimiter=',')
#
#     wr.writerow(['Name', 'Surname', 'Age'])
#     wr.writerow(['Ivan', 'Petrov', 18])
#     wr.writerow(['Anton', 'Pupkin', 22])
#     wr.writerow(['Serge', 'Nikonov', '35'])
#     wr.writerow(['Serge1', 'Nikonovich', '55'])
#     wr.writerow(['Petr', 'Koval', '77'])

# ..................................................


#
# with open('test.csv', 'r') as file:
#
#     reader = csv.reader(file)
#
#     print('reader :', reader, type(reader))
#
#     for i in reader:
#         print(*i, sep='\t\t')
#         # print(i)

# ..................................................


# with open('test.csv', 'r') as file:
#
#     reader = csv.DictReader(file)
#
#     print('reader', reader, type(reader))
#
#     # for i in range(2):
#     #     print(i, ':', next(reader))
#     # print('******************')
#
#     for i in reader:
#         print('line :', i, type(i))


# ##########################################
# field1 = 'My_Name'
# field2 = 'Surname'
# field3 = 'My_Age'
#
#
# # fields = ['Name', 'Surname', 'Age']
#
#
# fields = [field1, field2, field3]
#
# my_dict = [
#     # {'Name': 'Oleg', 'Surname': 'Ivanov', 'Age': 22},
#     # {'Name': 'Ira1', 'Surname': 'Kozlov', 'Age': 34},
#     # {'Name': 'Sasha', 'Surname': 'Pupkin', 'Age': 56},
#     # {'Name': 'Pasha', 'Surname': 'Sidorov', 'Age': 78},
#
#     {field1: 'Ivan', field2: 'Petrov', field3: 18},
#     {field1: 'Ivan1', field2: 'Petrov1', field3: 19},
#     {field1: 'Ivan2', field2: 'Petrov2', field3: 60},
#     {field1: 'Ivan33', field2: 'Petrov33', field3: 48},
# ]
#
#
#
# # #
# with open('test1.csv', 'w', newline='') as file:
#
#     writer = csv.DictWriter(file, fieldnames=fields, delimiter=';')
#
#     writer.writeheader()
#     writer.writerows(my_dict)



# #
# # # #!!!!!!!!!!!!!!!!!!!! delimiter= ';' for Excel, but ',' for dict !!!!
# with open('test2.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fields, delimiter=',')
#     writer.writeheader()
#     writer.writerows(my_dict)
# #
# # #
# with open('test2.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     print('reader', reader, type(reader))
#     # print(next(reader))
#     # print(next(reader))
#     # res = list(reader)
#     for i in reader:
#         print(i)





    # for i in reader:
    #     print('Dictionary : ', i, type(i))

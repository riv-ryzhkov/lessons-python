import numpy as np
import pandas as pd
import json
import datetime


def si_code(db_list):
# function for create field "siCode"

    if db_list[0] == 1:
        if db_list[1] == 'AP' or db_list[1] == 'AH':
            return 'A'
        elif db_list[1] == 'PRD':
            return 'B'
        elif db_list[1] == 'YLD':
            return 'BpA'
        else:
            return None
    else:
        if db_list[1] == 'AP' or db_list[1] == 'AH':
            return 'H'
        elif db_list[1] == 'PRD':
            return 'T'
        elif db_list[1] == 'YLD':
            return 'TpH'
        else:
            return None

# convertor for data of field "code2"
dic_fields = {
    'W': 'W/WIN',
    'S': 'S/1',
    'C': 'C'
}

def main():
    # input user's requests from file "inp-request.json" for checking the program
    with open('inp-request.json', 'r') as file:
        inp_request = json.load(file)


    start = datetime.datetime.now()  # start checking time of the program's working

    db = pd.read_csv("db_table.csv") # read data from the file

    # add field "bitCode"
    db.loc[:,'bitCode'] =  np.array(map(int, db['source'] == 'S1'))


    # add field "siCode"
    db.loc[:,'siCode'] =  np.array(map(si_code, list(zip(db['bitCode'], db['code3']))))

    # run program for 9 user's requests
    for i in range(len(inp_request)):
        # makes copy of DB
        db1 = db.copy()

        # makes slices of field "code1"
        el1 = inp_request[i]['code1'][2:]

        # convert data of field "code2"
        el2 = dic_fields[inp_request[i]['code2']]

        #  filter of DB
        db1 =  db1[db1['code1'].str.contains(el1[2:]) & db1['code2'].str.contains(el2)]

        # creating the answer for the 1st question (full version)
        dic_res = {(
            inp_request[i]['code1'],
            inp_request[i]['code2']
        ):
            list(db1['source'])
        }

        # creating the answer for the 1st question (short version)
        dic_res_set = {(
            inp_request[i]['code1'],
            inp_request[i]['code2']
        ):
            list(set(db1['source']))
        }

        # create the answer for the 2nd question
        for elem in dic_res_set[(inp_request[i]['code1'], inp_request[i]['code2'])]:

            dic_res_2 = {(
                inp_request[i]['code1'],
                inp_request[i]['code2'],
                elem
            ):
                db1[db1['source'] == elem].to_numpy()
            }

            db3 = db1[db1['source'] == elem]
            print('8'*80)
            print(db3.head(len(db3)))




        # printing the results
        print('.' * 80)
        print('The answer for 1st question (full version, some results are the same) :')
        print(dic_res)
        print('.' * 80)
        print('The answer for 1st question (short version, no results are the same) :')
        print(dic_res_set)
        print('.' * 80)
        print('The answer for 2nd question (full version) :')
        print(dic_res_2)
        print('.' * 80, '\n' * 3)
    print()
    print('+' * 80)
    # printig the time of the program's working
    end = datetime.datetime.now()
    print("The time of the program's working = ", end - start)


if __name__ == '__main__':
    main()
import json
import time


def time_table(x):
    with open('time_table.json') as f:
        data = json.load(f)

    monday = data['monday']
    tuesday = data['tuesday']
    wednesday = data['wednesday']
    thursday = data['thursday']
    friday = data['friday']
    saturday = data['saturday']

    map_ = {'1': monday,
            '2': tuesday,
            '3': wednesday,
            '4': thursday,
            '5': friday,
            '6': saturday,
            '0': monday
            }

    return map_[str(x)]


def rep_msg(msg):
    lst = ['chủ nhật', 'thứ 2', 'thứ 3', 'thứ 4', 'thứ 5', 'thứ 6', 'thứ 7']
    time_table_rt = None
    lst_wn = [('t2', 'thứ 2'),
            ('t3', 'thứ 3'),
            ('t4', 'thứ 4'),
            ('t5', 'thứ 5'),
            ('t6', 'thứ 6'),
            ('t7', 'thứ 7'),
            ('cn', 'chủ nhật')]

    elememts = []

    if msg == 'tkb' or msg == 'thời khóa biểu':
        time_table_rt = time_table(int(time.strftime(format('%w'))))
    else:
        for t in lst_wn:
            for el in t:
                if el in msg:
                    time_table_rt = time_table(lst_wn.index(t))

    for e in time_table_rt:
        time_ = list(e.keys())[0]
        subject = e[time_]
        elememts.append('{} : {}'.format(time_, subject))

    return '\n'.join(elememts)

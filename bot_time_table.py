import time

import Time_table


def rep_message(message, has_been_returned=False):
    lst_t2 = ['thứ 2', 't2']
    lst_t3 = ['thứ 3', 't3']
    lst_t4 = ['thứ 4', 't4']
    lst_t5 = ['thứ 5', 't5']
    lst_t6 = ['thứ 6', 't6']
    lst_t7 = ['thứ 7', 't7']
    lst_cn = ['chủ nhật', 'cn']

    for i in lst_t2 + lst_cn:
        if i in message:
            time_table = Time_table.time_table(1)
            has_been_returned = True
            break

    for i in lst_t3:
        if i in message:
            time_table = Time_table.time_table(2)
            has_been_returned = True
            break

    for i in lst_t4:
        if i in message:
            time_table = Time_table.time_table(3)
            has_been_returned = True
            break

    for i in lst_t5:
        if i in message:
            time_table = Time_table.time_table(4)
            has_been_returned = True
            break

    for i in lst_t6:
        if i in message:
            time_table = Time_table.time_table(5)
            has_been_returned = True
            break

    for i in lst_t7:
        if i in message:
            time_table = Time_table.time_table(6)
            has_been_returned = True
            break

    if has_been_returned is False:
        if int(time.strftime(format('%H'))) >= 18:
            time_table = Time_table.time_table(
                int(time.strftime(format('%w'))) + 1)
        elif int(time.strftime(format('%H'))) < 18:
            time_table = Time_table.time_table(
                int(time.strftime(format('%w'))))

    rep = ''
    for i in time_table:
        rep += '{} : {} \n'.format(i[0], i[1])

    return rep

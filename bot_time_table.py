import time


def time_table(x):
    monday = [('7h-7h45', 'Chào cờ'),
              ('7h55-8h40', 'Anh'),
              ('8h45-9h30', 'Anh'),
              ('9h35-10h20', 'Lý'),
              ('10h25-11h10', 'Sử'),
              ('11h15-12h', 'Tin'),
              ('14h-15h30', 'Lý tăng cường'),
              ('15h45-17h15', 'Hóa tăng cường')
              ]

    tuesday = [('7h-7h45', 'Tin'),
               ('7h55-8h40', 'Toán'),
               ('8h45-9h30', 'Toán'),
               ('9h35-10h20', 'Hóa'),
               ('10h25-11h10', 'GDCD'),
               ('14h-15h30', 'Toán tăng cường'),
               ('15h30-17h', 'Văn tăng cường')
               ]

    wednesday = [('7h-7h45', 'Hóa'),
                 ('7h55-8h40', 'Quốc phòng'),
                 ('8h45-9h30', 'Lý')
                 ]

    thursday = [('7h-7h45', 'Văn'),
                ('7h55-8h40', 'Văn'),
                ('8h45-9h30', 'Thể dục'),
                ('9h35-10h20', 'Địa'),
                ('10h25-11h10', 'Anh'),
                ('14h-15h30', 'Lý tăng cường'),
                ('15h45-17h15', 'Hóa tăng cường')
                ]

    friday = [('7h-7h45', 'Toán'),
              ('7h55-8h40', 'Công nghệ'),
              ('8h45-9h30', 'Tiếng anh TC'),
              ('9h35-10h20', 'Văn'),
              ('14h-15h30', 'Toán tăng cường'),
              ('15h30-17h', 'Tiếng Anh tăng cường')
              ]

    saturday = [('7h-7h45', 'Thể dục'),
                ('7h55-8h40', 'Sinh'),
                ('8h45-9h30', 'Lý'),
                ('9h35-10h20', 'Toán'),
                ('10h25-11h10', 'Văn'),
                ('11h15-12h', 'Sinh hoạt'),
                ('13h30-15h', 'Học nghề')
                ]

    if x == 1:
        return monday

    elif x == 2:
        return tuesday

    elif x == 3:
        return wednesday

    elif x == 4:
        return thursday

    elif x == 5:
        return friday

    elif x == 6:
        return saturday

    elif x == 7:
        return monday


def rep_message(message):
    has_been_returned = False

    lst_t2 = ['thứ 2', 't2']
    lst_t3 = ['thứ 3', 't3']
    lst_t4 = ['thứ 4', 't4']
    lst_t5 = ['thứ 5', 't5']
    lst_t6 = ['thứ 6', 't6']
    lst_t7 = ['thứ 7', 't7']

    for i in lst_t2:
        if i in message:
            time_table_ = time_table(1)
            has_been_returned = True
            break

    if has_been_returned is False:
        for i in lst_t3:
            if i in message:
                time_table_ = time_table(2)
                has_been_returned = True
                break

    if has_been_returned is False:
        for i in lst_t4:
            if i in message:
                time_table_ = time_table(3)
                has_been_returned = True
                break

    if has_been_returned is False:
        for i in lst_t5:
            if i in message:
                time_table_ == time_table(4)
                has_been_returned = True
                break

    if has_been_returned is False:
        for i in lst_t6:
            if i in message:
                time_table_ = time_table(5)
                has_been_returned = True
                break

    if has_been_returned is False:
        for i in lst_t7:
            if i in message:
                time_table_ = time_table(6)
                has_been_returned = True
                break

    if has_been_returned is False:
        if int(time.strftime(format('%H'))) >= 18:
            time_table_ = time_table(int(time.strftime(format('%w'))) + 1)
        elif int(time.strftime(format('%H'))) < 18:
            time_table_ = time_table(int(time.strftime(format('%w'))))

    rep = ''
    for i in time_table_:
        time_ = i[0]
        lesson = i[1]
        rep += '{} : {} \n'.format(time_, lesson)

    return rep

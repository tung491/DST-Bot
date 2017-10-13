def time_table():
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

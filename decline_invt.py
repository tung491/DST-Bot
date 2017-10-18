import random


def rep_msg(message):
    lst_regiustea = ['regiustea', 'regius', 'rì', 'zớt', 'rớt']

    for i in lst_regiustea:
        if i in message:
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Ví t nhẹ lắm r :)',
                       'M đừng tận thu tiền của t nữa :)',
                       'Tí tuổi đầu lấy đâu 50k mà suốt ngày uống rì rớt :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)'
                       ]
            return random.choice(msg_rep)
            break

    lst_boba_place = ['boba', 'bobapop', 'tea', 'bubble', 'ts',
                      'ding', 'dingtea', 'royaltea', 'hefkcaa', 'heekcaa',
                      'koi', 'taster\'s', 'citea', 'goky', 'house of cha',
                      'khai trương', 'trà sữa', 'wang', 'xing', 'gong cha',
                      'chago'
                      ]

    for i in lst_boba_place:
        if i in message:
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Bm còng lưng đi làm. Uống cái gì ??? :)',
                       'Tôi còn 10k :)',
                       'Ví t nhẹ lắm r :)',
                       'Tí tuổi đầu lấy đâu 50k mà suốt ngày uống ts :)',
                       'M đừng tận thu tiền của t nữa :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)'
                       ]

            return random.choice(msg_rep)
            break

    lst_orther_drink_place = ['coffee', 'starbuck', 'sb', 'gemini',
                              'highland', 'highlands', 'passio', 'cafe',
                              'trà', 'uống', 'bia', 'rượu', 'sữa'
                              ]
    for i in lst_orther_drink_place:
        if i in message:
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Ví t nhẹ lắm r :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)',
                       'Bm còng lưng đi làm. Uống cái gì ??? :)'
                       ]

            return random.choice(msg_rep)
            break

    lst_food_place = ['đi ăn', 'thịt', 'bánh', 'spaghetti', 'steak', 'pizza',
                      'kem', 'lotte', 'lotteria', 'joilibee', 'popeyes',
                      'kfc', 'bít tết', 'gà', 'xôi', 'mì', 'buffet',
                      'tôm', 'ngô', 'cơm', 'lẩu', 'khoai', 'sushi',
                      'chè', 'cháo', 'bún', 'chiên', 'xào', 'nướng', 'rán',
                      'chiên', 'súp', 'nem', 'xúc xích', 'hotdog',
                      'phô mai', 'pho mai'
                      ]

    for i in lst_food_place:
        if i in message:
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Bm còng lưng đi làm. Ăn cái gì ??? :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)'
                       ]

            return random.choice(msg_rep)
            break

    lst_quay_place = ['xp', 'rạp', 'cgv', 'bhd', '1900',
                      'pub', 'bar', 'quẩy', 'xem phim', 'xphim'
                      ]

    for i in lst_quay_place:
        if i in message:
            msg_rep = ['Học bài chưa thế cháu :)',
                       'Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)',
                       'Bm còng lưng đi làm. Quẩy cái gì ??? :)'
                       ]

            return random.choice(msg_rep)
            break

    lst_net_n_game = ['cz', 'fifa', 'pubg', 'net',
                      'battlefield', 'game', 'battle', 'làm ván'
                      ]
    for i in lst_net_n_game:
        if i in message:
            return 'Học đi mà làm nguời. Suốt ngày game giếc :)'
            break

    if message == '😇 or 😈?':
        return 'Địt con mẹ mày, mời cái lồn'
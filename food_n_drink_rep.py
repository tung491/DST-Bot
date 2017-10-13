import food_n_drink_place

def rep(message)
    for i in lst_regiustea:
        if i in message.lower():
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Ví t nhẹ lắm r :)',
                       'M đừng tận thu tiền của t nữa :)',
                       'Tí tuổi đầu lấy đâu 50k mà suốt ngày uống rì rớt :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)'
                       ]
            return random.choice(msg_rep)
            break

    for i in lst_boba_place:
        if i in message.lower():
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

    for i in lst_orther_drink_place:
        if i in message.lower():
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Ví t nhẹ lắm r :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)',
                       'Bm còng lưng đi làm. Uống cái gì ??? :)'
                       ]
            return random.choice(msg_rep)
            break

    for i in lst_food_place:
        if i in message.lower():
            msg_rep = ['Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Bm còng lưng đi làm. Ăn cái gì ??? :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)'
                       ]
            return random.choice(msg_rep)
            break

    for i in lst_hang_loose_place:
        if i in message.lower():
            msg_rep = ['Học bài chưa thế cháu :)',
                       'Bao thì đi :)', 'Nhà mình nghèo lắm :)',
                       'Tôi còn 10k :) \n và m đừng bảo t là 10k đủ r :)',
                       'Bm còng lưng đi làm. Quẩy cái gì ??? :)'
                       ]
            return random.choice(msg_rep)
            break

    for i in lst_net_n_game:
        if i in message.lower():
            return 'Học đi mà làm nguời. Suốt ngày game giếc :)'
            break

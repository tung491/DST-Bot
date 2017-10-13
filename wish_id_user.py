def wish_id_user():
    """
        Change the keys and the vaules == the id and the
        name of Facebook user who you want wish
    """
    team_regiustea = {'100003752803370': 'Phạm Trà Myy',
                      '100020962254247': 'Đào Xuân Thắng',
                      '100002907474039': 'Hoàng Sơn',
                      '100006117664625': 'Dung Dinh',
                      '100001300342349': 'Thuỷ Tiên'
                      }

    team_pymi = {'1350061339': 'Nguyễn Việt Hưng',
                 '100004012855036': 'Quang Pham',
                 '100003101554132': 'Bùi Yếnmf',
                 '100002878461842': 'Huy Pham',
                 '100002753383127': 'Duc Nguyen',
                 '100003697142684': 'Nguyễn Đắc Toàn',
                 '100004213744329': 'Phan Hoàng'
                 }

    team_11A5 = {'100004182042728': 'Đỗ Thanh Tùng',
                 '100007870421580': 'Nguyễn Tuấn Mạnh',
                 '100001652886761': 'Phạm Minh Đức',
                 '100003251835572': 'Hoàng Đức Khiêm',
                 '100007160290831': 'Việt Anh',
                 '100012476928878': 'Lê Tuấn',
                 '100005921132675': 'Thắng Nguyễn',
                 '100005099347669': 'Quang Anh',
                 '100004146587309': 'Minh Tuân',
                 '100007175294356': 'Thạch Nguyễn',
                 '100011463381374': 'Nguyen Hoang Viet Anh',
                 '100007845378603': 'Phạm Dương',
                 '100005850930512': 'Danh Hưng',
                 '100021766503810': 'Hoang Anh',
                 '100006436750545': 'Thành Hoàng',
                 '1816636852': 'Sỹ Hd',
                 '100011463381374': 'Nguyen Hoang Viet Anh',
                 '100012573636304': 'Đào Hùng Lữ',
                 '100009494456827': 'Triệu An Nhiên',
                 '100005466755731': 'Đức Minh'
                 }

    team_9c = {'100009463507727': 'Nghĩa Trọng',
               '100006552784591': 'Hoàng Quốc Thịnh',
               '100005551656027': 'Anh Quang Nguyễn',
               '100005179563149': 'Quỳnh Anh',
               '100006297854600': 'Đanh Vũ',
               '100005836782922': 'Thu Trang',
               '100008655883966': 'Nhat Chu Quang',
               '100008397073621': 'Đàm Quân',
               '100006530978709': 'Nguyễn Thành Công',
               '100004010484055': 'Anh Bin Anh'
               }

    team_GHC = {'100006463726982': 'Duy Đức',
                '100000149884733': 'Trường Nguyễn',
                '100004219033277': 'Nguyễn Nhật Huy',
                '100004698400465': 'Nguyễn Thanh Bình',
                '100005983260455': 'Vũ Trần',
                '100004549363785': 'Hoàng Long Dương',
                '100009482989771': 'Đức Minh',
                '100005547168815': 'Nguyễn Linh',
                '100007779193411': 'Duy Khương',
                '100005499785143': 'Duy Hiếu Lê',
                '100005920413349': 'Chu Duy Khánh',
                '100006853446909': 'Viet Nguyen Khoi Nguyen'
                }

    return (team_regiustea, team_pymi, team_11A5, team_9c, team_GHC)


def choose_wish():
    input_data = wish_id_user()
    return_data = []

    for id in input_data[0].keys():
        msg = '''Cảm ơn team Regiustea đã pha những cốc trà ngon cho mọi người
                 Chúc ngủ ngon, {} ^^ <3'''.format(input_data[0][id])
        return_data.append((id, msg))

    for id in input_data[1].keys():
        msg = '''Chúc mọi người trong team PYMI ngủ ngon, {}.
                 Con bot này được viết bằng Python ^^ <3
              '''.format(input_data[1][id])
        return_data.append((id, msg))

    for id in input_data[2].keys():
        msg = 'Chúc anh em trong 11A5 ngủ ngon,{} <3'.format(input_data[2][id])
        return_data.append((id, msg))

    for id in input_data[3].keys():
        msg = 'Chúc anh em trong team 9c ngủ ngon,{}'.format(input_data[3][id])
        return_data.append((id, msg))

    for id in input_data[4].keys():
        msg = 'Chúc các bro trong GHC ngủ ngon, {}'.format(input_data[4][id])
        return_data.append((id, msg))

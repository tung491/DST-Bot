import yaml


def wish_id_user():
    f = open('config.yaml', 'r')
    document = f.read()
    f.close()

    data = yaml.load(document)
    keys = list(data)

    group1 = data[keys[0]]
    group2 = data[keys[1]]
    group3 = data[keys[2]]
    group4 = data[keys[3]]
    group5 = data[keys[4]]
    # .......
    # group-n = data[key[n - 1]]

    return group1, group2, group3, group4, group5  # ...,group-n


def choose_wish():
    return_data = []

    group1, group2, group3, group4, group5 = wish_id_user()

    for id in group1.keys():
        msg = '''Cảm ơn team Regiustea đã pha những cốc trà ngon cho mọi người
                 Chúc ngủ ngon, {} ^^ <3
              '''.format(group1[id])

        return_data.append((id, msg))

    for id in group2.keys():
        msg = '''Chúc mọi người trong team PYMI ngủ ngon, {}.
                 Con bot này được viết bằng Python ^^ <3
              '''.format(group2[id])

        return_data.append((id, msg))

    for id in group3.keys():
        msg = 'Chúc anh em trong 11A5 ngủ ngon,{} <3'.format(group3[id])

        return_data.append((id, msg))

    for id in group4.keys():
        msg = 'Chúc anh em trong team 9c ngủ ngon,{}'.format(group4[id])

        return_data.append((id, msg))

    for id in group5.keys():
        msg = 'Chúc các bro trong GHC ngủ ngon, {}'.format(group5[id])
        return_data.append((id, msg))

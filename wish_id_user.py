import yaml


def wish_id_user():
    f = open('config.yaml', 'r')
    document = f.read()
    f.close()

    data = yaml.load(document)
    keys = list(data)

    group1 = (data[keys[0]], data[keys[1]])
    group2 = (data[keys[2]], data[keys[3]])
    group3 = (data[keys[4]], data[keys[5]])
    group4 = (data[keys[6]], data[keys[7]])
    group5 = (data[keys[8]], data[keys[9]])

    # .......
    # group-n = data[key[n - 1]]

    return group1, group2, group3, group4, group5  # ...,group-n


def choose_wish():
    return_data = []

    group1, group2, group3, group4, group5 = wish_id_user()

    for id in group1[0].keys():
        msg = group1[1].format(group1[0][id])

        return_data.append((id, msg))

    for id in group2[0].keys():
        msg = group2[1].format(group2[0][id])

        return_data.append((id, msg))

    for id in group3[0].keys():
        msg = group3[1].format(group3[0][id])

        return_data.append((id, msg))

    for id in group4[0].keys():
        msg = group4[1].format(group4[0][id])

        return_data.append((id, msg))

    for id in group5[0].keys():
        msg = group5[1].format(group5[0][id])
        return_data.append((id, msg))

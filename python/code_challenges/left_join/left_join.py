def join_letf(ht1, ht2):
    return_list = []
    ht1_list = ht1._buckets
    for i in range(len(ht1_list)):
        if ht1_list[i] is not None:
            temp_list = []
            temp_list.append(ht1_list[i].data[0])
            temp_list.append(ht1_list[i].data[1])

            if ht2.contains(ht1_list[i].data[0]):
                value = ht2.get(ht1_list[i].data[0])
                temp_list.append(value)
            else:
                temp_list.append(None)

        return_list.append(temp_list)

    return return_list

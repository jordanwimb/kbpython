for x in list1:
    count = 0
    count2 = 1
    newlist = list1[count] - list1[count2]
    count += 1
    count2 += 1
print(newlist)


testlist = [118211, 118223, 118235, 118247, 118260, 135956, 135968, 135980, 135992, 136005]

def get_count_values(value_list):
    newlist = []
    count = 1
    count2 = 0
    while count <= 12:
        newlist.append(value_list[count] - value_list[count2])
        count += 1
        count2 += 1
    return(newlist)

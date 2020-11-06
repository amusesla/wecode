num_list = []

def get_even_num():
    for i in range(1, 51):
        if i % 2 == 0:
            num_list.append(i)
    return num_list

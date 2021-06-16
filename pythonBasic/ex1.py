def get_len_list(arr):
    len_list = []
    for item in arr:
        if item != None:
            len_list.append(len(item))
        else:
            len_list.append(0)
    return len_list

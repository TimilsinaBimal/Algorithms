def linear_search(data, search_item):
    for idx, item in enumerate(data):
        if item == search_item:
            return idx
    return -1

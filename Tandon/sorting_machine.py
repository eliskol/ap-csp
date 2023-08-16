total_count = {"aluminum": 135, "plastic": 102, "paper": 213}

def sort_items(item_string):
    sorting_dict = {"A": "aluminum", "P": "plastic", "R": "paper"}
    for item in item_string:
        total_count[sorting_dict[item]] += 1

sort_items("AAPAARRRRPAAPPRRP")
print(total_count)
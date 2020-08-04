# 9th day challenge


def get_set_number(arr, total):
    return get_subset_number(arr, total, len(arr)-1)


def get_subset_number(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif arr[i] > total:
        return get_subset_number(arr, total, i-1)
    else:
        return get_subset_number(arr, total, i-1) + get_subset_number(arr, total - arr[i], i-1)



my_list = [2, 4, 6, 10]
print(get_set_number(my_list, 16))
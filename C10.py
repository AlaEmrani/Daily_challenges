# 10th day challenge


# write a function that returns the largest sum of non-adjacent numbers.
def get_maximum_non_adjacent_sum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    resul1 = get_maximum_non_adjacent_sum(arr[1:])
    resul2 = arr[0] + get_maximum_non_adjacent_sum(arr[2:])
    return max(resul1, resul2)


test_list = [5, 1, 1, 5]
print(get_maximum_non_adjacent_sum(test_list))
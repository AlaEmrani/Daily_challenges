# 7th day of challenge
import numpy as np


# Function to find the maximum contiguous subarray
def get_max_sum_subarray(arr):
    max_sum = 0
    max_sum_glob = -float('inf')
    for item in arr:
        max_sum+=item
        if max_sum_glob < max_sum:
            max_sum_glob = max_sum
        if max_sum < 0:
            max_sum = 0
    return max_sum_glob

my_list = [-2, -3, -4, -1, -6, -1, -5, -3]
print(get_max_sum_subarray(my_list))


def rand_reorder(arr):
    np.random.seed(11)
    for i in range(len(arr)-1, 0, -1):
        pick_index = int(np.floor(np.random.rand()*i))
        tmp = arr[i]
        arr[i] = arr[pick_index]
        arr[pick_index] = tmp
    return arr

print(rand_reorder(my_list))
# fifth day challenge
import numpy as np


def get_negative_numbers(mat):
    total = 0
    i, j = 0, mat.shape[1] - 1
    while i < mat.shape[0] and j>=0:
        print(i, j)
        if mat[i, j] < 0:
            total += j+1
            i +=1
        else:
            j -=1
    return total

sample_mat = np.array([[-4, -2, 1], [-3, 0, 1], [8, 0, 1], [4, 0, 1]])
# print(get_negative_numbers(sample_mat))
################

def get_all_subsets(my_set):
    print(len(my_set))
    if len(my_set) == 1:
        return [[], my_set]
    result = [i + [my_set[-1]] for i in get_all_subsets(my_set[:-1])]
    result += get_all_subsets(my_set[:-1])
    return result

ans = get_all_subsets([1,2, 3, 4])
ans.sort(key=len)
print(len(ans))

# third day challenge
# consider list as a number and add one to it
# a recursive approach

test_list = [9, 9, 9, 9, 9]


def add_one(my_list):
    if len(my_list) == 1:
        if my_list[0] <9:
            my_list[0] = my_list[0] + 1
            return my_list
        else:
            return [1, 0]
    if my_list[-1] == 9:
        return add_one(my_list[:-1]) + [0]
    my_list[-1] = my_list[-1] + 1
    return my_list


print(add_one(test_list))



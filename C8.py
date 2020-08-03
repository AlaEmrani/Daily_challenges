# 8th day of challenge


def get_longest_consecutive(my_str):
    all_chars_dict = dict.fromkeys(set(my_str), 0)
    count = 1
    prev_char = my_str[0]
    for i in my_str[1:]:
        new_char = i
        if new_char == prev_char:
            count +=1
            if all_chars_dict[new_char] < count:
                all_chars_dict[new_char] = count
        else:
            if all_chars_dict[prev_char] < count:
                all_chars_dict[prev_char] = count
            prev_char = new_char
            count = 1
    return all_chars_dict


sample_str = 'aaabbccdeee'
print(get_longest_consecutive(sample_str))

####################

def is_hoppable(my_list):
    if len(my_list) == 1:
        if my_list[0] != 0:
            return True
        else:
            return False
    if my_list[0] >= len(my_list):
        return True
    current_jump = my_list[0]
    i = 1
    while i <= current_jump:
        if my_list[i] + i > current_jump:
            current_jump = my_list[i] + i
        if current_jump >= len(my_list):
            return True
        i+=1
    return False

print(is_hoppable([2,3,0,0, 2,0]))












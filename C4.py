# 4th day challenge
import numpy as np


def get_distance(coordinate):
    return ((coordinate[0])**2 + (coordinate[1])**2)**.5


def get_k_closest_points(points, k):
    distances = [get_distance(p) for p in points]
    idxs = np.argpartition(distances, k)[:k]
    print(idxs)
    return [points[i] for i in idxs]


sample_points = [(5,2), (2, 2), (3, 3)]
print(get_k_closest_points(sample_points, 1))

####################################################


def get_first_recurrent_character(phrase):
    seen_characters = []
    for i in range(len(phrase)):
        if phrase[i] in seen_characters:
            return phrase[i]
        else:
            seen_characters.append(phrase[i])
    return None


print(get_first_recurrent_character('ABCAB'))


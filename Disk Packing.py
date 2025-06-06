from math import sqrt
from itertools import permutations

radii = [3, 4, 7, 9.5, 12]

def get_width(radii):
    width = radii[0]

    for index, radius in enumerate(radii):
        if index == len(radii) - 1:
            break
        else:
            dist = 2*sqrt(radius*radii[index+1])
            width += dist

    width += radii[-1]

    return round(width, 2)

def get_max_min(radii):
    min_width = [0, 0]
    max_width = [0, 0]

    for perm in permutations(radii):
        width = get_width(perm)
        
        if min_width[0] == 0 or width < min_width[0]:
            min_width = [width, perm]
        if max_width[0] == 0 or width > max_width[0]:
            max_width = [width, perm]
        
    return min_width, max_width

print(get_max_min(radii))
from math import sqrt
from itertools import permutations

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

def get_min_max(radii):
    min_width = [0, 0]
    max_width = [0, 0]

    for perm in permutations(radii):
        width = get_width(perm)
        
        if min_width[0] == 0 or width < min_width[0]:
            min_width = [width, perm]
        if max_width[0] == 0 or width > max_width[0]:
            max_width = [width, perm]
        
    return min_width, max_width

radii = []

while True:
    radius = input("Enter radius: ").strip()

    if radius:
        try:
            radius = float(radius)
        except ValueError:
            print("Input is not a valid number.")
            continue

        if radius > 0:
            radii.append(radius)

            if len(radii) >= 8:
                break
        else:
            print("Radius must be postiive.")
    else:
        break

if radii:
    original_width = get_width(radii)
    min_width, max_width = get_min_max(radii)
    
    print(f"{original_width:.2f}, {min_width[0]:.2f}, {min_width[1]}")

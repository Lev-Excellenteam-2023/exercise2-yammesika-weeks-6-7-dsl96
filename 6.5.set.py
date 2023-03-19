
import random
from itertools import combinations

def create_cards():
    cards = []

    for shape in range(1, 4):
        for shade in range(1, 4):
            for color in range(1, 4):
                for count in range(1, 4):
                    cards.append({'shape': shape, 'shade': shade, 'color': color, 'count': count})

    return cards


def is_set(trio):
    count_sum = sum([card['count'] for card in trio])
    shape_sum = sum([card['shape'] for card in trio])
    shade_sum = sum([card['shade'] for card in trio])
    color_sum = sum([card['color'] for card in trio])
    set_values_mod3 = [count_sum % 3, shape_sum % 3, shade_sum % 3, color_sum % 3]
    return set_values_mod3 == [0, 0, 0, 0]

def sets():
    cards = create_cards()
    random.shuffle(cards)

    twelve = cards[:12]
    sets = []
    for trio in combinations(twelve, 3):
        if is_set(trio):
            sets.append(trio)

    return sets


num = 0
for i in range(10000):
    if not sets():
        num = num + 1

print(f'{num / 10000 * 100:.2f}%')
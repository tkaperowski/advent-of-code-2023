'''
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
'''
import re
from typing import Iterator, Tuple

text = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''


def check_if_digit_next_to_star(iterator: Iterator, neighbor_digits: list, matches: int) -> Tuple[list, int]:
    for m in iterator:
        # print(f'{m.group()} in lines[{i-1}], span{m.span()}')
        # digit indexes
        digit_indexes = list(range(m.start(), m.end()))  # create list type by converting with list()
        # star indexes
        star_indexes = list(range(s.start() - 1, s.end() + 1))
        # check if any indexes in common
        is_match = any(i in digit_indexes for i in star_indexes)
        if is_match:
            # print(f'use this digit {m.group()}')
            neighbor_digits.append(int(m.group()))
            matches += 1
    return neighbor_digits, matches

with open('input.txt', 'r') as f:
    text = f.read()
lines = text.splitlines()

# add '.' to each line
width = len(lines[0])
hight = len(lines)

lines.insert(0, '.'*width)
lines.append('.'*width)
print(lines)

for i in range(len(lines)):
    lines[i] = '.'+lines[i]+'.'

pattern_star = re.compile('\*')
pattern_digit = re.compile('\d+')
sum = 0

# i for each line
for i in range(len(lines)):
    match_star = pattern_star.finditer(lines[i]) # return iterator with match objects for a match
    # s for each star
    for s in match_star:
        count_match = 0
        neighbor_list = []
        print(f'star * in lines[{i}], span{s.span()}')

        # check digit in line above
        match_digit = pattern_digit.finditer(lines[i-1])
        neighbor_list, count_match = check_if_digit_next_to_star(match_digit, neighbor_list, count_match)

        # check the same line
        match_digit = pattern_digit.finditer(lines[i])
        neighbor_list, count_match = check_if_digit_next_to_star(match_digit, neighbor_list, count_match)

        # check line below
        match_digit = pattern_digit.finditer(lines[i+1])
        neighbor_list, count_match = check_if_digit_next_to_star(match_digit, neighbor_list, count_match)

        # multiply and add if 2 or more digits next to '*'
        if count_match >= 2:
            multiply = neighbor_list[0] * neighbor_list[1]
            print(f'multiply: {neighbor_list[0]} * {neighbor_list[1]}')
            sum += multiply

print(sum)

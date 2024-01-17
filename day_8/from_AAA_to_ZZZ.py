'''
- make dict with tuple from data: {'AAA': ('BBB', 'CCC')}
- find_map returns tuple from key
- while loops for instruction_list, when index ends then starts from index=0
- in while use find_map
'''
'''
It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!
After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.
This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.
Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
'''

import re


# return tuple based on key
def find_map(element):
    for k, v in map_dict.items():
        if k == element:
            return v


with open('input.txt', 'r')as f:
    file = f.read()
# split by empty line
file_split = file.split('\n\n')

# make instruction list
instructions = file_split[0]
instruction_list = []
for x in instructions:
    instruction_list.append(x)
# make dict with maps
maps = file_split[1].splitlines()
map_dict = {}
for i in maps:
    find_words = re.findall('\w{3}', i)  # find words with len=3
    map_dict[find_words[0]] = (find_words[1], find_words[2])

step_number = 0

# find tuple for AAA map
start_element = 'AAA'
map_tuple = find_map(start_element)

index = 0
# while ends when finds ZZZ
while index < len(instruction_list):
    if instruction_list[index] == 'L':
        next_map = map_tuple[0]
    else:
        next_map = map_tuple[1]

    step_number += 1
    if next_map == 'ZZZ':
        break

    # find map
    map_tuple = find_map(next_map)

    index += 1
    # start instr_list from the beginning
    if index == len(instruction_list):
        index = 0

print(step_number)

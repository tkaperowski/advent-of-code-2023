'''
Start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.
For example:
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
'''
import math
import re


# return tuple based on key
def find_map(element):
    for k, v in map_dict.items():
        if k == element:
            return v


with open('input_p2.txt', 'r')as f:
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

# find tuple for xxA map
map_tuple = []
for k, v in map_dict.items():
    match = re.search('..A', k)
    if match:
        map_tuple.append(v)

'''
Find xxZ and count step_number for each map_tuple one by one as in part1. Then calculate step_number with math.lcm 
to find least common multiple which is lowest common value for all step_numbers.
Good to know: if map has 100 steps to find xxZ then 200, 300, ... also find xxZ, krotność step_number
'''
steps_required_for_lines = []
for i in map_tuple:

    step_number = 0
    index = 0
    # while ends when finds ZZZ
    while index < len(instruction_list):
        if instruction_list[index] == 'L':
            next_map = i[0]
        else:
            next_map = i[1]

        step_number += 1
        if next_map.endswith('Z'):
            break

        # find map
        i = find_map(next_map)

        index += 1
        # start instr_list from the beginning
        if index == len(instruction_list):
            index = 0

    print(step_number)
    steps_required_for_lines.append(step_number)

# use Least Common Multiple to find

# set first number
lcm = steps_required_for_lines[0]

for j in steps_required_for_lines:
    lcm = math.lcm(lcm, j)
print(lcm)



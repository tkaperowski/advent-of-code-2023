"""After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

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

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?"""
import math

with open("input_p2.txt", 'r') as file:
    instructions = file.readline().strip()
    nodes = file.read().strip().split("\n")

nodes_dict = {}
# create nodes dict
for node in nodes:
    nodes_dict.update({node[0:3]: [node[7:10], node[12:15]]})

# instructions to binary:
instructions = instructions.replace('R', '1')
instructions = instructions.replace('L', '0')

next_moves = []
for key in nodes_dict.keys():
    if key.endswith('A'):
        next_moves.append(key)

last_letter_in_next_moves = ''
steps_required_for_line = []
for x in range(len(next_moves)):
    steps = 0
    while not next_moves[x].endswith('Z'):
        for direction in instructions:
            next_moves[x] = nodes_dict[next_moves[x]][int(direction)]
            steps += 1
            if next_moves[x].endswith('Z'):
                break
    steps_required_for_line.append(steps)

# now we need to get least common multiple
lcm = 1
for n in steps_required_for_line:
    lcm = math.lcm(lcm, n)

print(steps_required_for_line)
print(lcm)
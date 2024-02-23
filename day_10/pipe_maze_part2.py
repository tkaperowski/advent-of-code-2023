'''
Find the path from S to S which is a loop, and verify how many points/tiles are inside the loop
- use Scanline algorithm to determine areas: inside or outside your polygon/object
- scan each line from left to right and switch from 'not in region' to 'in region' every time a boarder occurs
- boarders that switch a region are: a pipe |, L7, FJ, L--7, F---J
- U turns which do not switch a region are: F7, LJ, F---7
In the script:
- find the path and save each x:y which are line:index pairs
- S change with a correct symbol: L, J, F, ...
- replace each non-path sign to a dot '.'
- use Scanline algorithm to verify if a dot is in or not-in a region
https://www.reddit.com/r/adventofcode/comments/18f1sgh/comment/kcrecn6/
'''

import re

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

pipe = '|'
minus = '-'
l = 'L'
j = 'J'
seven = '7'
f = 'F'
dot = '.'
s = 'S'

line = 0
index = 0
direction = ''
step = 1
path = []
start_direction = 'left'

# find S position
a = range(len(lines))
for i in range(len(lines)):
    match = re.search('S', lines[i])
    if match:
        line = i
        index = match.start()
        print(f'S position: line id = {i}, index = {match.start()}')
        path.append((line, index))
        break

# find 1st move:
# check above
if lines[line - 1][index] in (pipe or seven or f):
    line -= 1
    start_direction = 'up'
    if lines[line][index] == pipe:
        direction = 'up'
    elif lines[line][index] == seven:
        direction = 'left'
    else:
        direction = 'right'
# check right
elif lines[i][index + 1] in (minus or j or seven):
    index += 1
    start_direction = 'right'
    print(f'line id: {line}, index: {index}')
    if lines[line][index] == minus:
        direction = 'right'
    elif lines[line][index] == j:
        direction = 'up'
    else:
        direction = 'down'
# check below
elif lines[i + 1][index] in (pipe or l or j):
    line += 1
    start_direction = 'down'
    if lines[line][index] == pipe:
        direction = 'down'
    elif lines[line][index] == l:
        direction = 'right'
    else:
        direction = 'left'
else:
    print('failed to find 1st move')

path.append((line, index))

# move and count steps
while step > 0:
    if direction == 'right':
        index += 1
        if lines[line][index] == seven:
            direction = 'down'
        elif lines[line][index] == j:
            direction = 'up'
        elif lines[line][index] == minus:
            direction = 'right'
        elif lines[line][index] == s:
            break
    elif direction == 'left':
        index -= 1
        if lines[line][index] == minus:
            direction = 'left'
        elif lines[line][index] == l:
            direction = 'up'
        elif lines[line][index] == f:
            direction = 'down'
        elif lines[line][index] == s:
            break
    elif direction == 'up':
        line -= 1
        if lines[line][index] == pipe:
            direction = 'up'
        elif lines[line][index] == f:
            direction = 'right'
        elif lines[line][index] == seven:
            direction = 'left'
        elif lines[line][index] == s:
            break
    elif direction == 'down':
        line += 1
        if lines[line][index] == pipe:
            direction = 'down'
        elif lines[line][index] == j:
            direction = 'left'
        elif lines[line][index] == l:
            direction = 'right'
        elif lines[line][index] == s:
            break
    step += 1
    path.append((line, index))
    # print(step, lines[line][index], direction)
    print(f'line id: {line}, index: {index}')

# replace S with a tile, tu oszukałeś bo działa dla konkretnego przypadku z przykładuL S -> F i zadania S -> L
# brak rozpisania dla wszystkich przypadków zamiany S na inne litery
if direction == 'up':
    if start_direction == 'right':
        new_char = 'F'
        before_index = lines[line][:index]
        after_index = lines[line][index+1:]
        lines[line] = before_index + new_char + after_index
elif direction == 'left':
    if start_direction == 'up':
        print(lines[line])
        new_char = 'L'
        before_index = lines[line][:index]
        after_index = lines[line][index + 1:]
        lines[line] = before_index + new_char + after_index
        print(lines[line])

# replace all non-path signs with '.'
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if (x, y) not in path:
            new_char = '.'
            before_index = lines[x][:y]
            after_index = lines[x][y+1:]
            lines[x] = before_index + new_char + after_index


# switch between in-region and not-in-region
def swap(x):
    return 'I' if x == 'O' else 'O'

# use Scanline algorithm to verify if a dot is in or not-in a region
count = 0
case = 'O' # O = not-in-region, I = in-region
corner = ''
unexpected = 0

for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == '.':
            if case == 'I':
                count += 1
        elif lines[x][y] == '|':
            case = swap(case)
        elif lines[x][y] == 'F':
            corner = 'F'
        elif lines[x][y] == '7':
            if corner == 'F':
                corner = ''
            elif corner == 'L':
                corner = ''
                case = swap(case)
            elif corner == '':
                corner = '7'
                unexpected += 1
                # what to do if stand alone?
        elif lines[x][y] == 'L':
            corner = 'L'
        elif lines[x][y] == 'J':
            if corner == 'L':
                corner = ''
            elif corner == 'F':
                corner = ''
                case = swap(case)
            elif corner == '':
                corner = 'J'
                unexpected += 1
                # what to do if stand alone?

print(count, unexpected)
pass

print(f'steps: {step}, farthest point: {int((step+1)/2)}')
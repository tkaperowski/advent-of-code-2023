'''
The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.

For example, here is a square loop of pipe.
If the animal had entered this loop in the northwest corner, the sketch would instead look like this:
.....
.S-7.
.|.|.
.L-J.
.....
In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.
Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).
Here is a sketch that contains a slightly more complex main loop:
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.
In the first example with the square loop:
.....
.S-7.
.|.|.
.L-J.
.....
You can count the distance each tile in the loop is from the starting point like this:
.....
.012.
.1.3.
.234.
.....
In this example, the farthest point from the start is 4 steps away.
Here's the more complex loop again:
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
Here are the distances for each tile on that loop:
..45.
.236.
01.78
14567
23...
Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
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

# find S position
for i in range(len(lines)):
    match = re.search('S', lines[i])
    if match:
        line = i
        index = match.start()
        print(f'S position: line id = {i}, index = {match.start()}')
        break

# find 1st move:
# check above
if lines[line - 1][index] in (pipe or seven or f):
    line -= 1
    if lines[line][index] == pipe:
        direction = 'up'
    elif lines[line][index] == seven:
        direction = 'left'
    else:
        direction = 'right'
# check right
elif lines[i][index + 1] in (minus or j or seven):
    index += 1
    if lines[line][index] == minus:
        direction = 'right'
    elif lines[line][index] == j:
        direction = 'up'
    else:
        direction = 'down'
# check below
elif lines[i + 1][index] in (pipe or l or j):
    line += 1
    if lines[line][index] == pipe:
        direction = 'down'
    elif lines[line][index] == l:
        direction = 'right'
    else:
        direction = 'left'
else:
    print('failed to find 1st move')

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
        if lines[line][index] == seven:
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
    # print(step, lines[line][index], direction)

print(f'steps: {step}, farthest point: {int((step+1)/2)}')
import re

'''
The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Explanation:
- add first and last line with dots for easier checking, then add dot at start and end of each line
- get digits with finditer()
- for each digit check all neighbour indexes
- if there is a symbol ther that a dot '.' next to this digit then add it
'''

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

with open('input.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')

width = len(lines[0])
hight = len(lines)

# Adding '.' to each side of 2D matrix:
# add first line with dots
lines.insert(0, '.'*width)
# add end line with dots
lines.append('.'*width)
# add '.' to start and end of each line
for i in range(len(lines)):
    lines[i] = '.'+lines[i]+'.'

sum = 0

for i in range(len(lines)):
    pattern1 = re.compile('\d+')    # compile patter '\d+' to pattern object for efficiency
                                    # https://docs.python.org/3/library/re.html#re.compile

    match1 = pattern1.finditer(lines[i])    # returns iterator with match objects for each match/digit in a row
    for m in match1:                        # skip 'for' when no match so digit not found in a row
        # def of match object, note: end()
        print(f'checking {m.group()} with start index {m.start()} and end index (note +1) {m.end()}')
        # digit length for '.' verification around the digit
        digit_length = len(m.group())
        digit = int(m.group())
        # print(lines[i-1])
        # print(lines[i-1][m.end()+1])

        sum_now = sum # to check if 'sum' changed in this iteration, then print/not-print info at the end

        # check '.' before and after the digit in the same line
        if lines[i][m.end()] != '.' or lines[i][m.start()-1] != '.':
            print(f'adding {digit} - there is a symbol other than dot "." next to it')
            sum += digit
            continue # skip this iteration

        # check '.' in the line above and below the digit
        for d in range(digit_length+2): # check indexes from end(), +2 is to check one index below match.start and also range() skips end value

            # check '.' in line above or in line below
            if lines[i-1][m.end()-d] != '.' or lines[i+1][m.end()-d] != '.':
                print(f'adding {digit} - there is a symbol other than dot "." next to it')
                sum += digit
                break # skip this for as digit done

        # print when sum not changed in this iteration meaning break wasn't called
        if sum_now == sum:
            print(f'ignoring {digit} as only dots next to it')
print(f'Suma wsyatlich liczb sąsiadujących z symbolem innym niż "." wynosi: {sum}')


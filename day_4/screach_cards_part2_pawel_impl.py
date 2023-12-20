'''
The same as before but now:
- not creating new cards but only counting them
- amount of matching numbers are added to below lines
- if there is 1 x line 1 with 4 matches (for line2+3+4+5) then 4 below lines get +1
- next is line 2 with amount=1+1 and 2 matches (line 3 & 4), then line 3 gets amount=1+1+2 and line 4 gets amount=1+1+2
- next line 3 with amount=4 and 1 match, then line 4 gets amount=1+1+2+4... and so on
'''
import re
import time

text = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


with open('data', 'r') as f:
    text = f.read()


lines = text.splitlines()
start = time.time()

number_of_cards = []
for x in range(len(lines)):
    number_of_cards.append(1)

# each card
for i in range(len(lines)):

    # count matching numbers
    winning_numbers = lines[i].split(':')[1].split('|')[0]  # = {str} ' 41 48 83 86 17 '
    winning_numbers = re.findall('\d+', winning_numbers)
    numbers = lines[i].split(':')[1].split('|')[1]          # = {str} ' 83 86  6 31 17  9 48 53'
    numbers = re.findall('\d+', numbers)
    matching_numbers = set(winning_numbers).intersection(numbers) # create new set with elements in common
    count = len(matching_numbers)

    # add cards
    for n in range(i+1, i + count + 1):
        number_of_cards[n] = number_of_cards[n] + number_of_cards[i]

end = time.time()
print(f'running time: {end-start} [s]')
print(f'all cards: {sum(number_of_cards)}')
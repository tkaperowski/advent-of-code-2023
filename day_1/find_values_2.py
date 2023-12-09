import re

'''
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''



replace_letters = {
    'one': '1ne',
    'two': '2wo',
    'three': '3hree',
    'four': '4our',
    'five': '5ive',
    'six': '6ix',
    'seven': '7even',
    'eight': '8ight',
    'nine': '9ine'
}

text = open('data.txt', 'r').read()

text_list = text.splitlines()


text_with_fix_letters = []
for line in text_list:

    first_positions = {}
    last_positions = {}
    # find index of first letters and index of last letters
    for item in replace_letters.items():
        # key is pattern to find
        pattern = item[0]
        # return index of 1st pattern from left, -1 on failure
        first_index = line.find(pattern)
        # add to dict when pattern found, ignore not found with -1
        if first_index >= 0:
            first_positions[pattern] = first_index
        # find pattern from reverse
        last_index = line.rfind(pattern)
        if last_index >= 0:
            last_positions[pattern] = last_index

    # true when dict from left not empty then modify letter with digit in line
    if first_positions:
        # find key with min value
        min_key = min(first_positions, key=first_positions.get)
        new_first_value = replace_letters[min_key]

        # replace str with pattern
        line = re.sub(min_key, new_first_value, line)

    # tru when dict from rihgt not empty
    if last_positions:
        # find key with max value
        max_key = max(last_positions, key=last_positions.get)
        new_last_value = replace_letters[max_key]

        line = re.sub(max_key, new_last_value, line)

    print(line)
    text_with_fix_letters.append(line)
print(text_with_fix_letters)


suma = 0

for line in text_with_fix_letters:
    # find digits as str -> ['2']
    digits_str = re.findall('\d', line)
    # str -> int
    digits = [int(s) for s in digits_str]
    first = digits[0]
    last = digits[-1]
    two_digit = int(str(first)+str(last)) # int -> str to have two-digit number, then str -> int
    print(two_digit)
    suma += two_digit
print(suma)




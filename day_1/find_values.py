import re

'''
Script:
- takes each line from data.txt
- find all digits in the line
- take first and last digit and form two-digit number
- add all numbers

For example:
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
In this example, the numbers are 12, 38, 15, and 77. Adding these together produces 142.
'''

with open('data.txt', 'r') as file:
    text = file.read()

# from file to list of lines -> ['str', ...]
list_of_lines = text.splitlines()

# remove empty lines like [..., '', ...]
list_of_lines = [s for s in list_of_lines if s]
print(list_of_lines)

def get_sum_from_all_lines(text_in_lines: list) -> int:
    suma = 0
    for line in text_in_lines:
        # find digits as str -> ['6', '3',...]
        digits_str = re.findall(r'\d', line)
        # str -> int
        digits = [int(s) for s in digits_str]
        # check if list not empty, for list index out of range error
        if digits_str:
            first = digits[0] # int
            last = digits[-1] # int
            # two_digit = int(str(first)+str(last)) # int -> str to have two-digit number, then str -> int
            two_digit = int(f'{first}{last}')
            # print(two_digit)
            suma += two_digit
    return suma

wynik = get_sum_from_all_lines(list_of_lines)
print(f'Sum of all lines: {wynik}')


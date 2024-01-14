'''
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
KK677 is now the only two pair, making it the second-weakest hand.
T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
With the new joker rule, the total winnings in this example are 5905.
'''



import re
from collections import defaultdict

'''
- use defaultdict() to count key characters, this dict can add new key:value pars without checking if key exists
- use list(sorted(dict.values())) to sort dict values like [1, 2, 3]
'''

def check_four_of_a_kind(hand: tuple) -> bool:
    default_dict = defaultdict(int)  # create default-dict, int is default value so called 'default_factory'
    for i in hand:
        default_dict[i] += 1  # add key to dict and count occurrences
    sort = list(sorted(default_dict.values()))  # sort values and make list
    if sort != [1, 4]:
        return False
    return True

def check_full_house(hand: tuple) -> bool:
    default_dict = defaultdict(int)
    for i in hand:
        default_dict[i] += 1
    sort = list(sorted(default_dict.values()))
    if sort != [2, 3]:
        return False
    return True

def check_three_of_a_kind(hand: str) -> bool:
    default_dict = defaultdict(int)
    for i in hand:
        default_dict[i] += 1
    sort = list(sorted(default_dict.values()))
    if sort != [1, 1, 3]:
        return False
    return True

def check_two_pair(hand: tuple) -> bool:
    default_dict = defaultdict(int)
    for i in hand:
        default_dict[i] += 1
    sort = list(sorted(default_dict.values()))
    if sort != [1, 2, 2]:
        return False
    return True

def check_one_pair(hand: tuple) -> bool:
    default_dict = defaultdict(int)
    for i in hand:
        default_dict[i] += 1
    sort = list(sorted(default_dict.values()))
    if sort != [1, 1, 1, 2]:
        return False
    return True



with open('example.txt', 'r') as f:
    read_file = f.read()

hands = read_file.splitlines()

hands_dict = {}
five_dict = {}
four_dict = {}
full_house_dict = {}
three_dict = {}
two_pair_dict = {}
one_pair_dict = {}
high_card_dict = {}

# convert hands to dict
for item in hands:
    item = item.split(" ")
    hands_dict[item[0]] = item[1]

# for each hand: check type, add to dict
for item in hands_dict.items():  # tuple (key, value)

    # check for J
    # use len() for types
    dafault_dictionary = defaultdict(int)
    if re.search('J', item[0]):  # if J in hand
        for j in item[0]:  # for each card
            if j == 'J':
                continue  # skip J card
            dafault_dictionary[j] += 1
        sorted_values = sorted(dafault_dictionary.values())
        if len(sorted_values) == 1:  # [3JJJJ], [3333J], ...
            five_dict[item[0]] = item[1]
            continue
        if sorted_values == [2, 2]:  # [33J44]
            full_house_dict[item[0]] = item[1]
            continue
        if len(sorted_values) == 2:  # [34JJJ]
            four_dict[item[0]] = item[1]
            continue
        if len(sorted_values) == 3:
            three_dict[item[0]] = item[1]
            continue
        if len(sorted_values) == 4:
            one_pair_dict[item[0]] = item[1]
            continue


    # check if all characters have the same value
    if all(i == item[0][0] for i in item[0][1:]):  # for each 'i' starting from item[0][1:] check if i === item[0][0], then all() returns True
        five_dict[item[0]] = item[1]
    # check if 4 the same characters
    elif check_four_of_a_kind(item[0]):
        four_dict[item[0]] = item[1]  # add hand to dict
    elif check_full_house(item[0]):
        full_house_dict[item[0]] = item[1]
    elif check_three_of_a_kind(item[0]):
        three_dict[item[0]] = item[1]
    elif check_two_pair(item[0]):
        two_pair_dict[item[0]] = item[1]
    elif check_one_pair(item[0]):
        one_pair_dict[item[0]] = item[1]
    else:
        high_card_dict[item[0]] = item[1]

'''
- check strength in each dict
'''

# assign int to labels, each label is a kay and needs to be str
labels = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


# from hand make list of int used as key for sorting
def cards_to_int_for_sorting(hand) -> list:  # hand: 'TTKTT'
    result = []
    for card in hand:
        result.append(labels[card])
    return result  # result: [10, 10, 13, 10, 10]


# sorted() returns list so next make sorted_dict from sorted_keys
sorted_five_dict_keys = sorted(five_dict, key=cards_to_int_for_sorting)  # key taken from dict
sorted_four_dict_keys = sorted(four_dict, key=cards_to_int_for_sorting)
sorted_full_house_dict_keys = sorted(full_house_dict, key=cards_to_int_for_sorting)
sorted_three_dict_keys = sorted(three_dict, key=cards_to_int_for_sorting)
sorted_two_pair_dict_keys = sorted(two_pair_dict, key=cards_to_int_for_sorting)
sorted_one_pair_dict_keys = sorted(one_pair_dict, key=cards_to_int_for_sorting)
sorted_high_card_dict_keys = sorted(high_card_dict, key=cards_to_int_for_sorting)


# make sorted_five_dict from sorted_five_dict_keys (list) and their values in five_dict
def make_dict_from_sorted_keys(sorted_keys, dict_for_values):
    sorted_dict = {}
    for item in sorted_keys:
        sorted_dict[item] = dict_for_values[item]
    return sorted_dict


# make sorted dict with types
sorted_five_dict = make_dict_from_sorted_keys(sorted_five_dict_keys, five_dict)
sorted_four_dict = make_dict_from_sorted_keys(sorted_four_dict_keys, four_dict)
sorted_full_house_dict = make_dict_from_sorted_keys(sorted_full_house_dict_keys, full_house_dict)
sorted_three_dict = make_dict_from_sorted_keys(sorted_three_dict_keys, three_dict)
sorted_two_pair_dicts = make_dict_from_sorted_keys(sorted_two_pair_dict_keys, two_pair_dict)
sorted_one_pair_dict = make_dict_from_sorted_keys(sorted_one_pair_dict_keys, one_pair_dict)
sorted_high_card_dict = make_dict_from_sorted_keys(sorted_high_card_dict_keys, high_card_dict)

# use | to join all dicts as a new copy, update can have ony one argument, | can have many
all_dict = sorted_high_card_dict | sorted_one_pair_dict | sorted_two_pair_dicts | sorted_three_dict | sorted_full_house_dict | sorted_four_dict | sorted_five_dict


i = 1
multiply = 0
for value in all_dict.values():
    multiply += int(value)*i
    i += 1

print(multiply)

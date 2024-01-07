'''
In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
'''




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

def check_three_of_a_kind(hand: tuple) -> bool:
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
labels = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


# from hand make list of int used as key for sorting
def cards_to_int_for_sorting(hand) -> list:
    result = []
    for card in hand:
        result.append(labels[card])
    return result


# sorted() returns list so next make sorted_dict from sorted_keys
sorted_five_dict_keys = sorted(five_dict, key=cards_to_int_for_sorting)
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

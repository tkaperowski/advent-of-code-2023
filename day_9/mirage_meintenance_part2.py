with open('input.txt', 'r') as f:
    read = f.read().splitlines()

history = []
for i in read:
    abc = i.split(' ')
    history.append([int(s) for s in abc])


def make_diff_seq(input_seq: list) -> list:
    diff_sequence = []
    for i in range(len(input_seq) - 1):
        diff_sequence.append(input_seq[i + 1] - input_seq[i])
    print(diff_sequence)
    return diff_sequence


sum = 0

for input in history:
    my_dict = {}
    my_dict['diff_seq_0'] = input
    i = 1
    # make sequence of differences
    while i > 0:
        my_dict[f'diff_seq_{i}'] = make_diff_seq(my_dict[f'diff_seq_{i - 1}'])

        if set(my_dict[f'diff_seq_{i}']) == {0}:
            print('found all-zeros list')
            i -= 1
            # add element to list above all-zeros list
            my_dict[f'diff_seq_{i}'].insert(0, my_dict[f'diff_seq_{i}'][-1])
            print(my_dict[f'diff_seq_{i}'])
            i -= 1
            break
        i += 1

    # extrapolate sequence of differences
    # pawel adds last element of all new lines! it makes sense!
    while i > -1:
        if i == 0:
            # calculate prediction
            prediction = my_dict[f'diff_seq_{i}'][0] - my_dict[f'diff_seq_{i + 1}'][0]
            break
        # add element which is sum of last elements of this list and list below
        my_dict[f'diff_seq_{i}'].insert(0, my_dict[f'diff_seq_{i}'][0] - my_dict[f'diff_seq_{i + 1}'][0])
        # print(my_dict[f'diff_seq_{i}'])
        i -= 1

    print(prediction)
    sum += prediction

print(f'sum: {sum}')



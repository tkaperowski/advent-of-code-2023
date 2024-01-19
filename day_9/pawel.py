"""You pull out your handy Oasis And Sand Instability Sensor and analyze your surroundings. The OASIS produces a report of many values and how they are changing over time (your puzzle input).
 Each line in the report contains the history of a single value. For example:

0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
To best protect the oasis, your environmental report should include a prediction of the next value in each history.
To do this, start by making a new sequence from the difference at each step of your history. If that sequence is not all zeroes, repeat this process,
using the sequence you just generated as the input sequence. Once all of the values in your latest sequence are zeroes, you can extrapolate what the next value of the original history should be.

In the above dataset, the first history is 0 3 6 9 12 15. Because the values increase by 3 each step, the first sequence of differences that you generate will be 3 3 3 3 3.
Note that this sequence has one fewer value than the input sequence because at each step it considers two numbers from the input.
Since these values aren't all zero, repeat the process: the values differ by 0 at each step, so the next sequence is 0 0 0 0.
This means you have enough information to extrapolate the history!"""


with open("input.txt", 'r') as file:
    lines = file.readlines()

history_sets = []
for line in lines:
    line = line.strip()
    history_sets.append([int(x) for x in line.split(" ")])

sum_extrapolated = 0
for history in history_sets:
    differences = []
    values = []
    sum_last = history[-1]
    # check when all elements after subtraction reach 0:
    while set(history) != {0}:
        # find differences betweeen numbers
        for n in range(len(history)-1):
            # append differences to values list
            values.append(history[n+1] - history[n])
        # differences will store all previous values
        differences.append(values)
        # next iteration will calculate differences for the values just calculated until all of them are 0
        history = values
        # reset values
        values = []
    # now get all last elements of differences and sum them up
    for step in differences:
        sum_last += step[-1]
    sum_extrapolated += sum_last

print(sum_extrapolated)
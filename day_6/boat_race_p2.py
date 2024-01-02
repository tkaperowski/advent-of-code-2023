'''
Time:      71530
Distance:  940200

Now, one race.
Code is the same, only input is different.
'''
import re

with open('input_p2.txt', 'r') as f:
    read_file = f.read()

# read race times
# regex positive lookbehind (?<=Time:) to find everything .+ in line after Time:
# search returns match obj, group() reads it and returns str, split() returns list ['', '', '', '', '', '', '7', '', '15', '', '', '30']
my_match = re.search('(?<=Time:).+', read_file).group().split(' ')
# remove empty str '' ['7', '15', '30']
while '' in my_match:
    my_match.remove('')
# race time in int
race_times = [int(x) for x in my_match]

# read race distances
my_match = re.search('(?<=Distance:).+', read_file).group().split(' ')
while '' in my_match:
    my_match.remove('')
race_distances = [int(s) for s in my_match]

# each element is a race with possible ways to beat a record
ways_to_beat_record = []

# for each race
for i in range(len(race_times)):
    # add empty element for new race
    ways_to_beat_record.append(0)
    # start from push_time=1ms
    push_time = 1
    # each while for 1ms push_time more
    while race_times[i] > push_time:
        # calculate reached distance for different push time
        reached_distance = (race_times[i] - push_time) * push_time
        # count reached records
        if reached_distance > race_distances[i]:
            ways_to_beat_record[i] += 1
        push_time += 1

multiply = 1 # use 1 to multiply first element of ways_to_beat_record[0]
for x in ways_to_beat_record:
    multiply *= x

print(multiply)


'''
Script:
- reads race_time[ms] and race_distance[mm]
- calculate reached_distance in race_time:
 e.g.
 race_time=15[ms] and race_distance=40[mm]
 push button time = 10ms gives speed v=10mm/1ms (pushing button time is added to race time)
 race_time 15ms - push time 10ms = 5ms race
 10ms for pushing, 5ms for race = 15ms race time
 boat reaches 50mm distance in 5ms race
'''
import re

with open('input.txt', 'r') as f:
    read_file = f.read()

# read race times
# regex positive lookbehind (?<=Time:) to find everything .+ in line after Time:
# search returns match obj, group() reads it and returns str, split() returns list ['', '', '', '', '', '', '7', '', '15', '', '', '30']
my_match = re.search('(?<=Time:).+', read_file).group().split(' ')
# remove empty str '' ['7', '15', '30']
while '' in my_match:
    my_match.remove('')
# time list with int
race_time = [int(x) for x in my_match]

# read race distances
my_match = re.search('(?<=Distance:).+', read_file).group().split(' ')
while '' in my_match:
    my_match.remove('')
race_distance = [int(s) for s in my_match]

# each element is a race with possible ways to beat a record
ways_to_beat_record = []

# for each race
for i in range(len(race_time)):
    # add empty element for new race
    ways_to_beat_record.append(0)
    # start from push_time=1ms
    push_time = 1
    # each while for 1ms push_time more
    while race_time[i] > push_time:
        # calculate reached distance for different push time
        reached_distance = (race_time[i] - push_time) * push_time
        # count reached records
        if reached_distance > race_distance[i]:
            ways_to_beat_record[i] += 1
        push_time += 1

multiply = 1 # use 1 to multiply first element of ways_to_beat_record[0]
for x in ways_to_beat_record:
    multiply *= x

print(multiply)


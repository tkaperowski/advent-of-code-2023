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

For example:

Time:      7  15   30
Distance:  9  40  200
This document describes three races:

The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.
Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.

So, because the first race lasts 7 milliseconds, you only have a few options:

Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it will have traveled 0 millimeters by the end of the race.
Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.
Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.
Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12 millimeters.
Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12 millimeters.
Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.
Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.
Hold the button for 7 milliseconds. That's the entire duration of the race. You never let go of the button. The boat can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move. 0 millimeters.
Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.

In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat the record, a total of 8 different ways to win.

In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and still beat the record, a total of 9 ways you could win.

To see how much margin of error you have, determine the number of ways you can beat the record in each race; in this example, if you multiply these values together, you get 288 (4 * 8 * 9).

Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?

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


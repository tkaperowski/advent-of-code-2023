'''
For example:
intput_example.txt

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?
'''





# each for iteration is for a single line e.g. seed_1, soil_1, range_1
# each if iteration checks if seed_1's value is in range_1's value
# len() // 3 in for as we get values of seed_'index', soil_'index', ... so index id part of key name in seed_dict{}
def get_soil_from_seed(seed: int) -> int:
    for index in range(len(seed_dict) // 3):
        if seed in range(seed_dict[f'seed_{index}'], seed_dict[f'seed_{index}'] + seed_dict[f'range_{index}']):
            # seed + |seed - soil|
            res = seed + abs(seed_dict[f'seed_{index}'] - seed_dict[f'soil_{index}'])       # + when seed lower than soil
            res2 = seed - abs(seed_dict[f'seed_{index}'] - seed_dict[f'soil_{index}'])      # - when seed higher than soil
            soil = res if seed_dict[f'seed_{index}'] < seed_dict[f'soil_{index}'] else res2
            # return soil
            return get_fertilizer_from_soil(soil) # call function for soil-to-fertilizer map
    soil = seed
    # return soil
    return get_fertilizer_from_soil(soil)

def get_fertilizer_from_soil(soil: int) -> int:
    for index in range(len(soil_dict) // 3):
        if soil in range(soil_dict[f'soil_{index}'], soil_dict[f'soil_{index}'] + soil_dict[f'range_{index}']):
            res = soil + abs(soil_dict[f'soil_{index}'] - soil_dict[f'fertilizer_{index}'])       # + when seed lower than soil
            res2 = soil - abs(soil_dict[f'soil_{index}'] - soil_dict[f'fertilizer_{index}'])      # - when seed higher than soil
            fertilizer = res if soil_dict[f'soil_{index}'] < soil_dict[f'fertilizer_{index}'] else res2
            return get_water_from_fertilizer(fertilizer)
    fertilizer = soil
    return get_water_from_fertilizer(fertilizer) # call function for fertilizer-to-water map

def get_water_from_fertilizer(source: int) -> int:
    for index in range(len(fertilizer_dict) // 3):
        if source in range(fertilizer_dict[f'source_{index}'], fertilizer_dict[f'source_{index}'] + fertilizer_dict[f'length_{index}']):
            res = source + abs(fertilizer_dict[f'source_{index}'] - fertilizer_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(fertilizer_dict[f'source_{index}'] - fertilizer_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if fertilizer_dict[f'source_{index}'] < fertilizer_dict[f'destination_{index}'] else res2
            return get_light_from_water(destination)
    destination = source
    return get_light_from_water(destination)

def get_light_from_water(source: int) -> int:
    for index in range(len(water_dict) // 3):
        if source in range(water_dict[f'source_{index}'], water_dict[f'source_{index}'] + water_dict[f'length_{index}']):
            res = source + abs(water_dict[f'source_{index}'] - water_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(water_dict[f'source_{index}'] - water_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if water_dict[f'source_{index}'] < water_dict[f'destination_{index}'] else res2
            return get_temp_from_light(destination)
    destination = source
    return get_temp_from_light(destination)

def get_temp_from_light(source: int) -> int:
    for index in range(len(light_dict) // 3):
        if source in range(light_dict[f'source_{index}'], light_dict[f'source_{index}'] + light_dict[f'length_{index}']):
            res = source + abs(light_dict[f'source_{index}'] - light_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(light_dict[f'source_{index}'] - light_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if light_dict[f'source_{index}'] < light_dict[f'destination_{index}'] else res2
            return get_humidity_from_temp(destination)
    destination = source
    return get_humidity_from_temp(destination)

def get_humidity_from_temp(source: int) -> int:
    for index in range(len(temp_dict) // 3):
        if source in range(temp_dict[f'source_{index}'], temp_dict[f'source_{index}'] + temp_dict[f'length_{index}']):
            res = source + abs(temp_dict[f'source_{index}'] - temp_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(temp_dict[f'source_{index}'] - temp_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if temp_dict[f'source_{index}'] < temp_dict[f'destination_{index}'] else res2
            return get_location_from_humidity(destination)
    destination = source
    return get_location_from_humidity(destination)

def get_location_from_humidity(source: int) -> int:
    for index in range(len(location_dict) // 3):
        if source in range(location_dict[f'source_{index}'], location_dict[f'source_{index}'] + location_dict[f'length_{index}']):
            res = source + abs(location_dict[f'source_{index}'] - location_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(location_dict[f'source_{index}'] - location_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if location_dict[f'source_{index}'] < location_dict[f'destination_{index}'] else res2
            return destination
    destination = source
    return destination




# with open('intput_example.txt', 'r') as f:
with open('input.txt', 'r') as f:
    maps = f.read()

# split by empty line
map_lines = maps.split('\n\n')

# get seeds
seed_line = map_lines[0].split(' ')[1:]
seed_list = [int(s) for s in seed_line]

# get seed-to-soil map
seed_to_soil_map = map_lines[1].split("\n")[1:]

# get soil-to-fertilizer map
soil_to_fertilizer_map = map_lines[2].split('\n')[1:]

# get fertilizer-to-water map
fertilizer_to_water_map = map_lines[3].split('\n')[1:]

# get water-to-light map
water_to_light_map = map_lines[4].split('\n')[1:]

# get light-to-temperature map
light_to_temp_map = map_lines[5].split('\n')[1:]

# get temperature-to-humidity map
temp_to_humidity_map = map_lines[6].split('\n')[1:]

# get humidity-to-location map
humidity_to_location_map = map_lines[7].split('\n')[1:]


# values from each line are saved in dictionary like: 'seed_1':value, 'range_1':value, 'soil_1':value, 'seed_2':value,... in seed_dict{}
seed_dict = {}
for line_index, line in enumerate(seed_to_soil_map):
    seed_key_name = f'seed_{line_index}'    # source
    range_key_name = f'range_{line_index}'  # lenght
    soil_key_name = f'soil_{line_index}'    # destination
    seed_dict[seed_key_name] = int(line.split(" ")[1])
    seed_dict[range_key_name] = int(line.split(" ")[2])
    seed_dict[soil_key_name] = int(line.split(" ")[0])
    print(seed_dict)

soil_dict = {}
for line_index, line in enumerate(soil_to_fertilizer_map):
    soil_key_name = f'soil_{line_index}'
    range_key_name = f'range_{line_index}'
    fertilizer_key_name = f'fertilizer_{line_index}'
    soil_dict[soil_key_name] = int(line.split(" ")[1])
    soil_dict[range_key_name] = int(line.split(" ")[2])
    soil_dict[fertilizer_key_name] = int(line.split(" ")[0])
    print(soil_dict)

fertilizer_dict = {}
for line_index, line in enumerate(fertilizer_to_water_map):
    source_key_name = f'source_{line_index}'
    length_key_name = f'length_{line_index}'
    destination_key_name = f'destination_{line_index}'
    fertilizer_dict[source_key_name] = int(line.split(" ")[1])
    fertilizer_dict[length_key_name] = int(line.split(" ")[2])
    fertilizer_dict[destination_key_name] = int(line.split(" ")[0])
    print(fertilizer_dict)

water_dict = {}
for line_index, line in enumerate(water_to_light_map):
    source_key_name = f'source_{line_index}'
    length_key_name = f'length_{line_index}'
    destination_key_name = f'destination_{line_index}'
    water_dict[source_key_name] = int(line.split(" ")[1])
    water_dict[length_key_name] = int(line.split(" ")[2])
    water_dict[destination_key_name] = int(line.split(" ")[0])
    print(water_dict)

light_dict = {}
for line_index, line in enumerate(light_to_temp_map):
    source_key_name = f'source_{line_index}'
    length_key_name = f'length_{line_index}'
    destination_key_name = f'destination_{line_index}'
    light_dict[source_key_name] = int(line.split(" ")[1])
    light_dict[length_key_name] = int(line.split(" ")[2])
    light_dict[destination_key_name] = int(line.split(" ")[0])
    print(light_dict)

temp_dict = {}
for line_index, line in enumerate(temp_to_humidity_map):
    source_key_name = f'source_{line_index}'
    length_key_name = f'length_{line_index}'
    destination_key_name = f'destination_{line_index}'
    temp_dict[source_key_name] = int(line.split(" ")[1])
    temp_dict[length_key_name] = int(line.split(" ")[2])
    temp_dict[destination_key_name] = int(line.split(" ")[0])
    print(temp_dict)

location_dict = {}
for line_index, line in enumerate(humidity_to_location_map):
    source_key_name = f'source_{line_index}'
    length_key_name = f'length_{line_index}'
    destination_key_name = f'destination_{line_index}'
    location_dict[source_key_name] = int(line.split(" ")[1])
    location_dict[length_key_name] = int(line.split(" ")[2])
    location_dict[destination_key_name] = int(line.split(" ")[0])
    print(location_dict)



# print(get_soil_from_seed(seed_list[3]))

location_list = []
for i in seed_list:
    location = get_soil_from_seed(i)
    location_list.append(location)
print(min(location_list))

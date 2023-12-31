'''
Now, seed pairs give a start number and a range:
seeds: 79 14 55 13
79 and next 13 seeds
55 and next 12 seeds
What is the lowest location number that corresponds to any of the initial seed numbers?

Here we do revers engineering: start from location=0 and try to find a seed from all ranges for it. Here we have to
modify dictionaries so source is [0] and destination is [1].
'''
import time


# each for iteration is for a single line e.g. seed_1, soil_1, range_1
# each if iteration checks if seed_1's value is in range_1's value
# len() // 3 in for as we get values of seed_'index', soil_'index', ... so index id part of key name in seed_dict{}
def get_soil_from_seed(source: int) -> int:
    for index in range(len(seed_dict) // 3):
        if source in range(seed_dict[f'source_{index}'], seed_dict[f'source_{index}'] + seed_dict[f'length_{index}']):
            # seed + |seed - soil|
            res = source + abs(seed_dict[f'source_{index}'] - seed_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(seed_dict[f'source_{index}'] - seed_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if seed_dict[f'source_{index}'] < seed_dict[f'destination_{index}'] else res2
            # return soil
            return destination # call function for soil-to-fertilizer map
    destination = source
    # return soil
    return destination

def get_fertilizer_from_soil(source: int) -> int:
    for index in range(len(soil_dict) // 3):
        if source in range(soil_dict[f'source_{index}'], soil_dict[f'source_{index}'] + soil_dict[f'length_{index}']):
            res = source + abs(soil_dict[f'source_{index}'] - soil_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(soil_dict[f'source_{index}'] - soil_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if soil_dict[f'source_{index}'] < soil_dict[f'destination_{index}'] else res2
            return get_soil_from_seed(destination)
    destination = source
    return get_soil_from_seed(destination) # call function for fertilizer-to-water map

def get_water_from_fertilizer(source: int) -> int:
    for index in range(len(fertilizer_dict) // 3):
        if source in range(fertilizer_dict[f'source_{index}'], fertilizer_dict[f'source_{index}'] + fertilizer_dict[f'length_{index}']):
            res = source + abs(fertilizer_dict[f'source_{index}'] - fertilizer_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(fertilizer_dict[f'source_{index}'] - fertilizer_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if fertilizer_dict[f'source_{index}'] < fertilizer_dict[f'destination_{index}'] else res2
            return get_fertilizer_from_soil(destination)
    destination = source
    return get_fertilizer_from_soil(destination)

def get_light_from_water(source: int) -> int:
    for index in range(len(water_dict) // 3):
        if source in range(water_dict[f'source_{index}'], water_dict[f'source_{index}'] + water_dict[f'length_{index}']):
            res = source + abs(water_dict[f'source_{index}'] - water_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(water_dict[f'source_{index}'] - water_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if water_dict[f'source_{index}'] < water_dict[f'destination_{index}'] else res2
            return get_water_from_fertilizer(destination)
    destination = source
    return get_water_from_fertilizer(destination)

def get_temp_from_light(source: int) -> int:
    for index in range(len(light_dict) // 3):
        if source in range(light_dict[f'source_{index}'], light_dict[f'source_{index}'] + light_dict[f'length_{index}']):
            res = source + abs(light_dict[f'source_{index}'] - light_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(light_dict[f'source_{index}'] - light_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if light_dict[f'source_{index}'] < light_dict[f'destination_{index}'] else res2
            return get_light_from_water(destination)
    destination = source
    return get_light_from_water(destination)

def get_humidity_from_temp(source: int) -> int:
    for index in range(len(temp_dict) // 3):
        if source in range(temp_dict[f'source_{index}'], temp_dict[f'source_{index}'] + temp_dict[f'length_{index}']):
            res = source + abs(temp_dict[f'source_{index}'] - temp_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(temp_dict[f'source_{index}'] - temp_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if temp_dict[f'source_{index}'] < temp_dict[f'destination_{index}'] else res2
            return get_temp_from_light(destination)
    destination = source
    return get_temp_from_light(destination)

def get_location_from_humidity(source: int) -> int:
    for index in range(len(location_dict) // 3):
        if source in range(location_dict[f'source_{index}'], location_dict[f'source_{index}'] + location_dict[f'length_{index}']):
            res = source + abs(location_dict[f'source_{index}'] - location_dict[f'destination_{index}'])       # + when seed lower than soil
            res2 = source - abs(location_dict[f'source_{index}'] - location_dict[f'destination_{index}'])      # - when seed higher than soil
            destination = res if location_dict[f'source_{index}'] < location_dict[f'destination_{index}'] else res2
            return get_humidity_from_temp(destination)
    destination = source
    return get_humidity_from_temp(destination)


start = time.time()

with open("input.txt", 'r') as f:
# with open('input.txt', 'r') as f:
    maps = f.read()

# split by empty line
map_lines = maps.split('\n\n')

# get seeds
seed_line = map_lines[0].split(' ')[1:]
seed_list = tuple(int(s) for s in seed_line)

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

# values from each map line are saved in dictionary: 'seed_1':value, 'range_1':value, 'soil_1':value, 'seed_2':value,...
def make_dict_for_each_value_from_map(map: list) -> dict:
    my_dict = {}
    for line_index, line in enumerate(map):
        source_key_name = f'source_{line_index}'
        length_key_name = f'length_{line_index}'
        destination_key_name = f'destination_{line_index}'
        my_dict[source_key_name] = int(line.split(" ")[0])
        my_dict[length_key_name] = int(line.split(" ")[2])
        my_dict[destination_key_name] = int(line.split(" ")[1])
    return my_dict


# make dict for each map with 3 pairs from each line: 'source_7': value, 'length_7': value, 'destination_7': value...
seed_dict = make_dict_for_each_value_from_map(seed_to_soil_map)
soil_dict = make_dict_for_each_value_from_map(soil_to_fertilizer_map)
fertilizer_dict = make_dict_for_each_value_from_map(fertilizer_to_water_map)
water_dict = make_dict_for_each_value_from_map(water_to_light_map)
light_dict = make_dict_for_each_value_from_map(light_to_temp_map)
temp_dict = make_dict_for_each_value_from_map(temp_to_humidity_map)
location_dict = make_dict_for_each_value_from_map(humidity_to_location_map)


# print(get_soil_from_seed(seed_list[3]))


# location = 34000000
location = 0
found = False
while not found:
    # get seed from location
    seed = get_location_from_humidity(location)
    print(f'seed {seed} from location {location}')
    # check if seed is in seed ranges
    for i in range(0, len(seed_list), 2):
        # check if seed in range
        if seed_list[i] <= seed < seed_list[i] + seed_list[i + 1]:
            for j in range(seed_list[i], seed_list[i]+seed_list[i+1]):
                # get seed again being in range
                print(f'range {j}, seed {seed}')
                if j == seed:
                    found = True
                    print(f'found seed {seed} in seed range {seed_list[i]} - {seed_list[i]+seed_list[i+1]} with location {location}')
                    break
            if found:
                break
    # increase by 100 to speed up
    location += 1

if not found:
    print("not found in seed range")

end = time.time()
print(f'czas: {end-start}')

# found seed 3751501334 in seed range 3736161691 - 3908507817 with location 34039469
# czas: 7999.656185626984
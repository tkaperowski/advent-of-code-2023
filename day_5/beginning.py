'''
rozpisz czytanie 2-3 linijek z pliku, rozpisz dla każdej co robisz zwiększając index, zobacz gdzie powtarza sie kod i jakie indexy się zmieniają i czy można zastąpić je jakąś zmienną czy funkcją czy for...
'''



# one if for each line in map list
def seed_to_soil_map(seed):
    if seed in range(seed1, seed1+range1):
        res = seed + abs(seed1-soil1)   # + when seed lower than soil
        res2 = seed - abs(seed1-soil1)  # - when seed higher than soil
        return res if seed1 < soil1 else res2
    elif seed in range(seed2, seed2 + range2):
            res = seed + abs(seed2-soil2)  # + when seed lower than soil
            res2 = seed - abs(seed2-soil2)  # - when seed higher than soil
            return res if seed2 < soil2 else res2
    else:
        return seed

# soil + |seed - soil|


seed = 50

input = '''seed-to-soil map:
50 98 2
52 50 48
'''

lines = input.split('\n')

seed1 = int(lines[1].split(" ")[1])
range1 = int(lines[1].split(" ")[2])
soil1 = int(lines[1].split(" ")[0])
seed2 = int(lines[2].split(" ")[1])
range2 = int(lines[2].split(" ")[2])
soil2 = int(lines[2].split(" ")[0])

print(seed_to_soil_map(seed))


# each for is for a single line e.g. seed_1, soil_1, range_1
# each if check if seed_1's value is in range_1' value
# len() // 3 in for loop as here we don't check slownik{} index which is 3x longer that lists[] but we search for key name
# max seed_index comes from max line[], max index is from line_index, slownik{} is 3x longer that lines[] and we add to it: seed, soil, range
#
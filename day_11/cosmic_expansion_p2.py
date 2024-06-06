"""
the same as part1 but now each empty row and column is replaced by 1000000 rows and columns
"""
import copy
from datetime import datetime

def find_empty_columns(data):
    # number of columns
    num_columns = len(data[0])
    # create list to mark column with '#'
    columns_with_hash = [False] * num_columns

    # iterate each row
    for row in data:
        # iterate each column
        for i in range(num_columns):
            if row[i] == '#':
                columns_with_hash[i] = True
    # create list with columns that do not contain '#'
    empty_columns = [i for i, has_hash in enumerate(columns_with_hash) if not has_hash]
    print(empty_columns)
    return empty_columns


def find_empty_rows(data):
    empty_rows = []
    # iterate each row
    for i, row in enumerate(data):
        if '#' not in row:
            empty_rows.append(i)
    print(empty_rows)
    return empty_rows


def add_empty_rows(data, row_indexes):
    print(id(data))
    # iterate from the end
    for row_index in reversed(row_indexes):
        i = 0
        while i < 9:
            data.insert(row_index, ',' * len(data[0]))
            i += 1
    return data


def add_empty_columns(data, column_indexes):
    # number of rows
    num_rows = len(data)
    # iterate each row
    for i in range(num_rows):
        # iterate each column_indexes
        for column_index in reversed(column_indexes):
            j = 0
            while j < 9:
                data[i] = data[i][:column_index] + ',' + data[i][column_index:]
                j += 1
    return data


def find_hash_positions(data):
    hash_positions = []
    # iterate each row with enumerate to get row and row_index
    for row_id, row in enumerate(data):
        # iterate each character in row with enumerate to get character and column_index
        for column_id, char in enumerate(row):
            if char == '#':
                # add tuple with row_id and column_id
                hash_positions.append((row_id, column_id))
    return hash_positions


def calculate_paths(data):
    total_sum = 0
    num_tuples = len(data)
    # iterate each tuple
    for i in range(num_tuples):
        # iterate over each following tuple
        for j in range(i + 1, num_tuples):
            row_diff = abs(data[i][0] - data[j][0])
# dla row nie trzeba sprawdzać czy indexy maleją dla pierwszego i drugiego hash'a bo row zawsze rośnie, można darować
# sobie definiowanie 'step' bo zawsze bedzie =1 czyli range() sprawdzamy od mniejszej do większej liczby
            # step for range()
            step = 1
            # step = -1 when indexes decreasing e.g. range(3, 0) -> [3, 2, 1]
            if data[i][0] > data[j][0]:
                step = -1
            # consider empty rows
            for row in empty_rows:
                if row in range(data[i][0], data[j][0], step):
                    row_diff += 999999

            column_diff = abs(data[i][1] - data[j][1])
# tu trzeba sprawdzać który index kolumny jest większy bo koluma drugiego hasha może mnieć mniejszy index i wtedy
# step =-1 musi być
            # step for range() =1 by default, step = -1 when indexes decreasing e.g. range(3, 0) -> [3, 2, 1]
            step = -1 if data[i][1] > data[j][1] else 1
            # consider empty columns
            for column in empty_columns:
                if column in range(data[i][1], data[j][1], step):
                    column_diff += 999999

            total_sum += row_diff + column_diff
    return total_sum


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

print(datetime.now())
# deepcopy line as lines/list is mutable and is changed when using it as def argument, deepcopy is good for lists in
# list
copy_lines = copy.deepcopy(lines)
# find column indexes that do not contain '#'
empty_columns = find_empty_columns(lines)
# find row indexes that do not contain '#'
empty_rows = find_empty_rows(lines)

# add row with '.' for empty_rows
lines_with_rows = add_empty_rows(copy_lines, empty_rows)
# add column with '.' for empty_columns
lines_with_rows_and_columns = add_empty_columns(lines_with_rows, empty_columns)

# find hash positions from lines
hash_positions = find_hash_positions(lines)
# calculate paths
paths_sum = calculate_paths(hash_positions)
print(paths_sum)
print(datetime.now())
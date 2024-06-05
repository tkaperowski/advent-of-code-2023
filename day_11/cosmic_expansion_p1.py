"""
- find rows and columns with '.' only, without '#'
- for rows and columns without '#' add new 'empty' rows and columns with '.'
- find '#' positions as tuple (row_id, column_id)
- calculate path between tuple1 and tuple2 by (I found this looking at '#' indexes):
 - tuple_1 (a, b)
 - tuple_2 (c, d)
 - path = |a - c| + |b - d|
- sum paths from tuple_1 to tuple_2, tuple_3,...
- sum paths from tuple_2 to tuple_3, tuple_4,...
...
- sum of all tuples is the total path
"""


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
    return empty_columns


def find_empty_rows(data):
    empty_rows = []
    # iterate each row
    for i, row in enumerate(data):
        if '#' not in row:
            empty_rows.append(i)
    return empty_rows


def add_empty_rows(data, row_indexes):
    # iterate from the end
    for row_index in reversed(row_indexes):
        data.insert(row_index, '.' * len(data[0]))
    return data

# def add_empty_columns(data, column_indexes):
#     # iterate each row
#     for index, row in enumerate(data):
#         # iterate each column index
#         for column_index in reversed(column_indexes):
#             row = row[:column_index] + '.' + row[column_index:]
#         data[index] = row
#     return data


def add_empty_columns(data, column_indexes):
    # number of rows
    num_rows = len(data)
    # iterate each row
    for i in range(num_rows):
        # iterate each column_indexes
        for column_index in reversed(column_indexes):
            data[i] = data[i][:column_index] + '.' + data[i][column_index:]
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


# def calculate_paths(data):
#     total_sum = 0
#     num_tuples = len(data)
#     # iterate each tuple
#     for index, main_tuple in enumerate(data):
#         while index < num_tuples - 1:
#             total_sum += abs(main_tuple[0] - data[index + 1][0]) + abs(main_tuple[1] - data[index + 1][1])
#             index += 1
#     return total_sum


def calculate_paths(data):
    total_sum = 0
    num_tuples = len(data)
    # iterate each tuple
    for i in range(num_tuples):
        # iterate over each following tuple
        for j in range(i + 1, num_tuples):
            total_sum += abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1])
    return total_sum


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

# find column indexes that do not contain '#'
empty_columns = find_empty_columns(lines)
# find row indexes that do not contain '#'
empty_rows = find_empty_rows(lines)

# add row with '.' for empty_rows
lines_with_rows = add_empty_rows(lines, empty_rows)
# add column with '.' for empty_columns
lines_with_rows_and_columns = add_empty_columns(lines_with_rows, empty_columns)

# find hash positions
hash_positions = find_hash_positions(lines_with_rows_and_columns)
# calculate paths
paths_sum = calculate_paths(hash_positions)
print(paths_sum)
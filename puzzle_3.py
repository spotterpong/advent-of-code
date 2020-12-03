import sys
import math

def read_file(file_name):
	with open(file_name) as f:
		lines = f.readlines()
		return [line.strip() for line in lines]

def count_trees(lines, right=3, down=1):
    num_trees = 0
    row_index = 0
    column_index = 0
    max_column_width = len(lines[0])
    while row_index <= len(lines):
        column_index = (column_index + right) % max_column_width
        row_index = row_index + down
        if row_index < len(lines) and lines[row_index][column_index] == '#':
            num_trees += 1
    return num_trees


if __name__ == "__main__":
    data = read_file(sys.argv[1])
    print(f"Part1: {count_trees(data)}")

    part_2_slopes = [
        {"right": 1, "down": 1},
        {"right": 3, "down": 1},
        {"right": 5, "down": 1},
        {"right": 7, "down": 1},
        {"right": 1, "down": 2}
    ]
    total_trees = 1
    for commands in part_2_slopes:
        total_trees *= count_trees(data, **commands)
    print(f"Part 2: {total_trees}")

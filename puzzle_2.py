import sys
import math

def read_file(file_name):
	with open(file_name) as f:
		lines = f.readlines()
		return [line.strip() for line in lines]

def breakup_line(line):
    length, letter, password = line.split(' ')
    min_length, max_length = length.split('-')
    letter = letter.replace(':','')
    return int(min_length), int(max_length), letter, password

def count_occurances(data):
    number_valid = 0
    for row in data:
        min_length, max_length, letter, password = breakup_line(row)
        letter_count = 0
        for char in password:
            if char == letter:
                letter_count += 1
                if letter_count > max_length:
                    break
        if letter_count >= min_length and letter_count <= max_length:
            number_valid += 1
    return number_valid

def get_valid_positions(data):
    number_valid = 0
    for row in data:
        found_character_count = 0
        first_occurance, second_occurance, letter, password = breakup_line(row)
        for x in [first_occurance, second_occurance]:
            if password[x-1] == letter:
                found_character_count += 1
        if found_character_count == 1:
            number_valid += 1
    return number_valid
        

if __name__ == "__main__":
    
    data = read_file(sys.argv[1])
    number_valid = count_occurances(data)
    print(f'Part 1: {number_valid}')
    
    valid_positions = get_valid_positions(data)
    print(f'Part 2: {valid_positions}')

                


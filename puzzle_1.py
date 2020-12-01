import sys
import math

def get_numbers(file_name):
	with open(file_name) as f:
		lines = f.readlines()
		return [int(number.strip()) for number in lines]

def find_numbers_to_goal(numbers, n=2, goal=2020):
	indexes = [0 for _ in range(n)]
	while True:
		numbers_add = sum([numbers[i] for i in indexes])
		if numbers_add == goal:
			return [numbers[i] for i in indexes]

		i = len(indexes) - 1
		indexes[i] += 1
		if indexes[i] >= len(numbers):
			indexes[i] = 0
			need_change = True
			for x in range(i-1,-1,-1):
				if need_change:
					need_change = False
					indexes[x] += 1
					if indexes[x] >= len(numbers):
						indexes[x] = 0
						need_change = True

		if i == 0 and indexes[i] > len(numbers):
			print("No solution found")
			return None			

if __name__ == "__main__":
	goal = 2020
	numbers = get_numbers(sys.argv[1])
	numbers = find_numbers_to_goal(numbers, n=sys.argv[2])
	print(f"{numbers} = {math.prod(numbers)}")
	sys.exit(1)
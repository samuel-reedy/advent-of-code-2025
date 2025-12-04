import numpy as np
from scipy.signal import convolve2d

day = "04"

def part_one(input_data):
    print("Part One")
    lines = input_data.splitlines()
    converted_data = np.array([[1 if c == '@' else 0 for c in line] for line in lines])
    
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    
    counts_grid = convolve2d(converted_data, kernel, mode='same', boundary='fill', fillvalue=0)
    
    result = np.sum((converted_data == 1) & (counts_grid < 4))
    
    print(result)


def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
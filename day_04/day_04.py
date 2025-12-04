import numpy as np
from scipy.signal import convolve2d

day = "04"

kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

def part_one(input_data):
    print("Part One")
    global kernel
    lines = input_data.splitlines()
    converted_data = np.array([[1 if c == '@' else 0 for c in line] for line in lines])

    counts_grid = convolve2d(converted_data, kernel, mode='same', boundary='fill', fillvalue=0)
    
    result = np.sum((converted_data == 1) & (counts_grid < 4))
    
    print(result)


def part_two(input_data):
    print("Part Two")    
    global kernel
    lines = input_data.splitlines()
    converted_data = np.array([[1 if c == '@' else 0 for c in line] for line in lines])
    
    can_remove = True
    
    total = 0
    
    while (can_remove):
        counts_grid = convolve2d(converted_data, kernel, mode='same', boundary='fill', fillvalue=0)
        to_remove = (converted_data == 1) & (counts_grid < 4)
        total += np.sum(to_remove)
        
        if np.any(to_remove):
            converted_data[to_remove] = 0
        else:
            can_remove = False
            
    print(total)
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
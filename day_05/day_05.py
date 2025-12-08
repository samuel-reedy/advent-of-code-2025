import numpy as np

day = "05"

def part_one(input_data):
    print("Part One")
    
    ranges, values = input_data.split("\n\n")
    
    ranges = [[int(x) for x in range.split("-")] for range in ranges.splitlines()]
    
    values = [int(x) for x in values.splitlines()]
    
    count = 0
    for value in values:
         for r in ranges:
            if value in range(r[0], r[1]):
                count += 1
                break
   
        
    
    print(count)
    
    
def part_two(input_data):
    print("Part Two")
    
    ranges, _ = input_data.split("\n\n")
    
    ranges = [[int(x) for x in line.split("-")] for line in ranges.splitlines()]
    
    ranges.sort(key=lambda x: x[0])

    merged = []
    for start, end in ranges:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total = sum(end - start + 1 for start, end in merged)
    print(total)
        
        
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read()
    
    part_one(input_data)
    part_two(input_data)
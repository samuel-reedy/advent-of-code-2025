import math

day = "06"

def part_one(input_data):
    print("Part One")
    
    rows = [line.split() for line in input_data]
    
    numbers = len(rows) - 1
    count = len(rows[0])
    
    total = 0
    
    for col in range(0, count):
        values = []
        for row in range(0, numbers):
            print(row)
            values.append(int(rows[row][col]))
        if rows[numbers][col] == "*":
            total += math.prod(values)
        elif rows[numbers][col] == "+":
            total += sum(values)
            
    print(total)
                
    

    
def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.readlines()
    
    part_one(input_data)
    part_two(input_data)
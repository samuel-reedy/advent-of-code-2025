day = "XX"

def part_one(input_data):
    print("Part One")
    
def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
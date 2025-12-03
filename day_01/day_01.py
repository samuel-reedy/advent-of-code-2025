day = "01"

def part_one(input_data):
    print("Part One")
    position = 50
    password = 0
    rotations = input_data.splitlines()
    for rotation in rotations:
        dir = 1 if rotation[0] == 'R' else -1
        steps = int(rotation[1:])
        position = (position + dir * steps) % 100
        password += 1 if position == 0 else 0
    print(f"Final Password: {password}")
        
        
    
def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
day = "02"

def part_one(input_data):
    print("Part One")
    total = 0
    ids = input_data.split(',')
    for id_range in ids:
        start_value = int(id_range.split('-')[0])
        end_value = int(id_range.split('-')[1])
        for value in range(start_value, end_value + 1):
            string = str(value)
            if len(string) % 2 == 0:
                mid = len(string) // 2
                if string[:mid] == string[mid:]:
                    print(f"Invalid ID: {value}")
                    total += value
    print(f"Final total: {total}")
        
    
def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
day = "02"

def part_one(input_data):
    print("Part One")
    total = 0
    ids = input_data.split(',')
    for id_range in ids:
        start_value, end_value = map(int, id_range.split('-'))
        for value in range(start_value, end_value + 1):
            string = str(value)
            if len(string) % 2 == 0:
                mid = len(string) // 2
                if string[:mid] == string[mid:]:
                    total += value
    print(f"Final total: {total}")
        
    
def part_two(input_data):
    print("Part Two")
    total = 0
    ids = input_data.split(',')
    for id_range in ids:
        start_value, end_value = map(int, id_range.split('-'))
        for value in range(start_value, end_value + 1):
            string = str(value)
            length = len(string)
            for pattern_length in range(1, length):
                if length % pattern_length == 0:
                    invalid = True
                    for pos in range(0, length - pattern_length, pattern_length):
                        if string[pos:pos+pattern_length] != string[pos+pattern_length:pos+2*pattern_length]:
                                invalid = False
                                break
                    if invalid:
                        total += value
                        break
    print(f"Final total: {total}")
    
if __name__ == "__main__":
    
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
day = "03"

def part_one(input_data):
    print("Part One")
    total = 0
    banks = input_data.splitlines()
    for bank in banks:
        largest_idx = 0
        largest = 0
        for idx in range(len(bank) - 1):
            if int(bank[idx]) > largest:
                largest_idx = idx
                largest = int(bank[idx])
        second_largest = 0
        for idx in range(largest_idx+1, int(len(bank))):
            if int(bank[idx]) > second_largest:
                second_largest = int(bank[idx])
            
        joltage = str(largest) + str(second_largest)
        total += int(joltage)
    print(f"Final total: {total}")
        
        
                
        
            
    
def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
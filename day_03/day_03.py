day = "03"

def find_joltage(banks, count):
    banks = input_data.splitlines()
    total = 0
    for bank in banks:
        batteries = []
        for step in range(count):
            index_end = len(bank) - (count - step) + 1
            largest = 0
            largest_idx = 0
            for idx in range(0, index_end):
                if int(bank[idx]) > largest:
                    largest = int(bank[idx])
                    largest_idx = idx
            batteries.append(str(largest))
            bank = bank[largest_idx+1:]
        joltage = "".join(batteries)
        total += int(joltage)
    return total

def part_one(input_data):
    print("Part One")
    banks = input_data.splitlines()
    total = find_joltage(banks, 2)
    print(f"Final total: {total}")
  
  
        
def part_two(input_data):
    print("Part Two")
    banks = input_data.splitlines()
    total = find_joltage(banks, 12)
    print(f"Final total: {total}")   
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
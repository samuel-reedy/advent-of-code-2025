from itertools import count


day = "03"

def find_joltage(bank, battery_count):
    batteries = []
    for _ in range(battery_count):
        index_end = len(bank) - battery_count + len(batteries) + 1
        largest_idx = bank.index(max(bank[:index_end], key=int))
        batteries.append(bank[largest_idx])
        bank = bank[largest_idx+1:]
    joltage = "".join(batteries)
    return int(joltage)

def part_one(input_data):
    print("Part One")
    banks = input_data.splitlines()
    total = 0
    for bank in banks:
        total += find_joltage(bank, 2)
    print(f"Final total: {total}")
  
  
        
def part_two(input_data):
    print("Part Two")
    banks = input_data.splitlines()
    total = 0
    for bank in banks:
        total += find_joltage(bank, 12)
    print(f"Final total: {total}")
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
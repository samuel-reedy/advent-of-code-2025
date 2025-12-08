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
            values.append(int(rows[row][col]))
        if rows[numbers][col] == "*":
            total += math.prod(values)
        elif rows[numbers][col] == "+":
            total += sum(values)
            
    print(total)
                
    

    
def part_two(input_data):
    print("Part Two") 
    
    rows = [line.split() for line in input_data]
    
    widths = []
    for r, c in enumerate(rows):
        for col, val in enumerate(c):
            if len(widths) <= col:
                widths.append(0)
            if len(val) > widths[col]:
                widths[col] = len(val)
                
    print(f"widths: {widths}")
                
    count = len(rows[0])
    parsed_rows = []
    for line in input_data:
        parsed_line = []
        for width in widths:
            parsed_line.append(line[:width])
            line = line[width+1:]
            
        parsed_rows.append(parsed_line)

    print(parsed_rows)
    
    numbers = len(rows) - 1
    count = len(rows[0])
    
    total = 0
    
    value_lists = []
    for col in range(0, count):
        values = [ [] for _ in range(0, numbers)]
        for row in range(0, numbers):
            for i in range(0, widths[col]):
                values[row].append((parsed_rows[row][col][i]))
        value_lists.append(values)
        
    print(f"value_lists: {value_lists}")
    
    value_list_flipped = []
    for col in range(0, len(value_lists)):
        values = []
        print(f"Processing column {col}")
        for i in range(0, widths[col]):
            print(f" Processing index {i}")
            value = []
            for row in range(0, len(value_lists[col])):
                print(value_lists[col][row])
                print(f"  Adding row {row} value {value_lists[col][row][i]}")
                value.append((value_lists[col][row][i]))
            values.append(value)
        value_list_flipped.append(values)
        
    print(f"value_list_flipped: {value_list_flipped}")
    
    final_numbers = []
    for group in value_list_flipped:
        group_numbers = []
        for values in group:
            number_str = ''.join(values).strip()
            if number_str:
                group_numbers.append(int(number_str))
        final_numbers.append(group_numbers)
        
    print(f"final_numbers: {final_numbers}")
        
    rows = [line.split() for line in input_data]
    operators = rows[-1]
    
    total = 0
    
    for col in range(0, len(final_numbers)):
        print(f"Processing column {col}")
        if operators[col] == "*":
            total += math.prod(final_numbers[col])
        elif operators[col] == "+":
            total += sum(final_numbers[col])
        else:
            print(f"Unknown operator {operators[col]}")
            
    print(total)
    

      
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.readlines()
    
    part_one(input_data)
    part_two(input_data)
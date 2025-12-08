day = "07"

total = 0

def add_beam(data_row, col):
    global total
    if col < 0 or col >= len(data_row):
        return data_row
    if data_row[col] == '.':
        data_row[col] = '|'
    elif data_row[col] == '^':
        total += 1
        data_row = add_beam(data_row, col - 1)
        data_row = add_beam(data_row, col + 1)
    elif data_row[col] == '|':
        return data_row
    return data_row
        

def part_one(input_data):
    print("Part One")
    rows = input_data.splitlines()
    print(rows)
    
    start_pos = rows[0].index('S')
    print(f"Start position: {start_pos}")
    
    for i, row in enumerate(rows):
        row_list = list(row)
        if i == 0:
            pass
        if i == 1:
            row_list = add_beam(row_list, start_pos)
        if i >= 2:
            for col in range(0, len(row_list)):
                if rows[i-1][col] == '|':
                    row_list = add_beam(row_list, col)
        rows[i] = ''.join(row_list)
        print(rows[i])
    
    print(total)     
            
    
def part_two(input_data):
    print("Part Two")    
    
if __name__ == "__main__":
    print(f"--- Day {day} ---")
    with open(f"day_{day}.txt", "r") as file:
        input_data = file.read().strip()
    
    part_one(input_data)
    part_two(input_data)
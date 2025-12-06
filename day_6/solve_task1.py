
def solve():
    try:
        with open('day_6/input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]

    if not lines:
        print("Grand total: 0")
        return

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    # Find columns that are NOT empty (have at least one non-space char)
    non_empty_cols = []
    for c in range(max_len):
        is_empty = True
        for line in padded_lines:
            if line[c] != ' ':
                is_empty = False
                break
        if not is_empty:
            non_empty_cols.append(c)
            
    if not non_empty_cols:
        print("Grand total: 0")
        return

    # Group adjacent non-empty columns into ranges
    ranges = []
    if non_empty_cols:
        start = non_empty_cols[0]
        prev = non_empty_cols[0]
        for col in non_empty_cols[1:]:
            if col > prev + 1:
                # Gap detected, close current range
                ranges.append((start, prev))
                start = col
            prev = col
        ranges.append((start, prev))
        
    grand_total = 0
    
    for start_col, end_col in ranges:
        # Extract numbers and operator
        # Operator is expected on the last line
        operator_str = padded_lines[-1][start_col:end_col+1].strip()
        
        # Numbers are on lines before the last one
        numbers = []
        for i in range(len(padded_lines) - 1):
            num_str = padded_lines[i][start_col:end_col+1].strip()
            if num_str:
                numbers.append(int(num_str))
                
        if operator_str == '+':
            val = sum(numbers)
            grand_total += val
        elif operator_str == '*':
            val = 1
            for n in numbers:
                val *= n
            grand_total += val
            
    print(f"Grand total: {grand_total}")
    
    try:
        with open('day_6/output1.txt', 'w') as f:
            f.write(str(grand_total))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(grand_total))

if __name__ == "__main__":
    solve()

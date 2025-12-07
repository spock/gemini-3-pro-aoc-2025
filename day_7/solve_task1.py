
def solve():
    try:
        with open('day_7/input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]

    if not lines:
        print("Splits: 0")
        return

    # Find S
    start_pos = None
    for r, line in enumerate(lines):
        if 'S' in line:
            start_pos = (r, line.index('S'))
            break
            
    if not start_pos:
        print("Splits: 0")
        return

    start_r, start_c = start_pos
    width = len(lines[0]) 
    height = len(active_lines := lines) # Rename to utilize later if needed, but lines is fine.

    active_xs = {start_c}
    total_splits = 0

    # Start processing from the row inclusive of S, or after?
    # "extends downward from S until it reaches the first splitter"
    # S acts like '.', so we process S row, it passes through to S row + 1.
    # So loop starts at start_r.
    
    for r in range(start_r, height):
        next_xs = set()
        current_line = lines[r]
        line_len = len(current_line)
        
        if not active_xs:
            break
            
        for x in active_xs:
            # Check bounds
            if x < 0 or x >= line_len:
                # Beam exits manifold
                continue
                
            char = current_line[x]
            
            if char == '^':
                total_splits += 1
                # Splits into left and right for NEXT row (x-1, x+1)
                # But since we are iterating rows, adding to next_xs handles the next row part implicitly
                # Wait, adding x-1 and x+1 to next_xs means checking grid[r+1][x-1] in next iteration.
                # Yes, correct.
                # Bounds check for next_xs addition?
                # We can add them, and check bounds when consuming in next loop.
                next_xs.add(x - 1)
                next_xs.add(x + 1)
            else:
                # '.' or 'S' or anything else passes through
                next_xs.add(x)
        
        active_xs = next_xs

    print(f"Splits: {total_splits}")
    
    try:
        with open('day_7/output1.txt', 'w') as f:
            f.write(str(total_splits))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(total_splits))

if __name__ == "__main__":
    solve()


from collections import defaultdict

def solve():
    try:
        with open('day_7/input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]

    if not lines:
        print("Timelines: 0")
        return

    # Pad lines to ensure uniform width
    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width, '.') for line in lines]
    height = len(grid)
    width = max_width

    # Find S
    start_pos = None
    for r, line in enumerate(grid):
        if 'S' in line:
            start_pos = (r, line.index('S'))
            break
            
    if not start_pos:
        print("Timelines: 0")
        return

    start_r, start_c = start_pos
    
    # counts matches column index to number of timelines at that column
    counts = defaultdict(int)
    counts[start_c] = 1
    
    total_timelines = 0
    
    # Process row by row
    # The beam is currently AT 'counts' columns in row 'r'.
    # We continually process rows until we fall off the bottom.
    
    for r in range(start_r, height):
        next_counts = defaultdict(int)
        
        # Optimize: if no counts, stop
        if not counts:
            break
            
        current_row_str = grid[r]
        
        for c, count in counts.items():
            # Check if this column is valid for the current row
            # Since we iterate r from start_r to height-1, and 'counts' represents
            # beams entering row r.
            
            # Since we are essentially "processing what happens at row r",
            # we look at grid[r][c].
            # If c is out of bounds, the beam has exited the manifold.
            # Wait, in the loop logic below, we add c-1 and c+1 to next_counts.
            # Those could be out of bounds.
            # So we check bounds when consuming 'counts'.
            
            if c < 0 or c >= width:
                total_timelines += count
                continue
                
            char = current_row_str[c]
            
            if char == '^':
                # Split: goes to (r+1, c-1) and (r+1, c+1)
                next_counts[c - 1] += count
                next_counts[c + 1] += count
            else:
                # Pass through: goes to (r+1, c)
                next_counts[c] += count
                
        counts = next_counts

    # Any beams remaining in 'counts' essentially exited the bottom
    total_timelines += sum(counts.values())

    print(f"Timelines: {total_timelines}")
    
    try:
        with open('day_7/output2.txt', 'w') as f:
            f.write(str(total_timelines))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(total_timelines))

if __name__ == "__main__":
    solve()

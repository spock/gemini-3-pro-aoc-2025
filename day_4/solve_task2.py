
def solve():
    try:
        with open('day_4/input.txt', 'r') as f:
            lines = [list(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [list(line.strip()) for line in f.readlines()]

    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    total_removed = 0
    
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == '@':
                    adjacent_rolls = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '@':
                                adjacent_rolls += 1
                    
                    if adjacent_rolls < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
            
        total_removed += len(to_remove)
        for r, c in to_remove:
            lines[r][c] = '.' # Or 'x' as in example, but '.' effectively removes it
            
    print(f"Total removed rolls: {total_removed}")
    
    try:
        with open('day_4/output2.txt', 'w') as f:
            f.write(str(total_removed))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(total_removed))

if __name__ == "__main__":
    solve()

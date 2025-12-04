
def solve():
    try:
        with open('day_4/input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines()]

    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    accessible_count = 0

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '@':
                adjacent_rolls = 0
                # Check 8 neighbors
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] == '@':
                            adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible_count += 1

    print(f"Accessible rolls: {accessible_count}")
    
    try:
        with open('day_4/output1.txt', 'w') as f:
            f.write(str(accessible_count))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(accessible_count))

if __name__ == "__main__":
    solve()

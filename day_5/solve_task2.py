
def solve():
    try:
        with open('day_5/input.txt', 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            content = f.read().strip()

    parts = content.split('\n\n')
    ranges_str = parts[0].split('\n')

    ranges = []
    for r in ranges_str:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))

    ranges.sort(key=lambda x: x[0])

    merged = []
    if ranges:
        curr_start, curr_end = ranges[0]
        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]
            
            # Check for overlap or touching (since we are counting integers)
            # e.g. 3-5 and 6-8 can be merged to 3-8
            if next_start <= curr_end + 1:
                curr_end = max(curr_end, next_end)
            else:
                merged.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end
        merged.append((curr_start, curr_end))

    total_fresh = 0
    for start, end in merged:
        total_fresh += (end - start + 1)

    print(f"Total fresh ingredients: {total_fresh}")
    
    try:
        with open('day_5/output2.txt', 'w') as f:
            f.write(str(total_fresh))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(total_fresh))

if __name__ == "__main__":
    solve()

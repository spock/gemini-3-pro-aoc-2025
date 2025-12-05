
def solve():
    try:
        with open('day_5/input.txt', 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            content = f.read().strip()

    parts = content.split('\n\n')
    ranges_str = parts[0].split('\n')
    ids_str = parts[1].split('\n')

    ranges = []
    for r in ranges_str:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))

    fresh_count = 0
    for id_str in ids_str:
        if not id_str:
            continue
        ingredient_id = int(id_str)
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1

    print(f"Fresh ingredients: {fresh_count}")
    
    try:
        with open('day_5/output1.txt', 'w') as f:
            f.write(str(fresh_count))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(fresh_count))

if __name__ == "__main__":
    solve()


def solve():
    try:
        with open('day_1/input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Fallback for running from inside day_1 directory
        with open('input.txt', 'r') as f:
            lines = f.readlines()

    current_pos = 50
    zero_count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            current_pos = (current_pos + distance) % 100
        elif direction == 'L':
            current_pos = (current_pos - distance) % 100
            
        if current_pos == 0:
            zero_count += 1
            
    print(f"Password: {zero_count}")
    
    try:
        with open('day_1/output1.txt', 'w') as f:
            f.write(str(zero_count))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(zero_count))

if __name__ == "__main__":
    solve()

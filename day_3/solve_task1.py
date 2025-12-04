
def solve():
    try:
        with open('day_3/input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = f.readlines()

    total_sum = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line]
        max_joltage = -1
        
        # Brute force all pairs (i, j) with i < j
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                joltage = digits[i] * 10 + digits[j]
                if joltage > max_joltage:
                    max_joltage = joltage
        
        total_sum += max_joltage
            
    print(f"Total output joltage: {total_sum}")
    
    try:
        with open('day_3/output1.txt', 'w') as f:
            f.write(str(total_sum))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(total_sum))

if __name__ == "__main__":
    solve()

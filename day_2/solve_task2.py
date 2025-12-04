
def is_invalid(num):
    s = str(num)
    L = len(s)
    # Try all possible lengths for the repeating substring
    for l in range(1, L // 2 + 1):
        if L % l == 0:
            substring = s[:l]
            repeats = L // l
            if substring * repeats == s:
                return True
    return False

def solve():
    try:
        with open('day_2/input.txt', 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            content = f.read().strip()

    ranges = content.split(',')
    total_sum = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if is_invalid(num):
                total_sum += num
            
    print(f"Sum of invalid IDs: {total_sum}")
    
    try:
        with open('day_2/output2.txt', 'w') as f:
            f.write(str(total_sum))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(total_sum))

if __name__ == "__main__":
    solve()


def is_invalid(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

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
        with open('day_2/output1.txt', 'w') as f:
            f.write(str(total_sum))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(total_sum))

if __name__ == "__main__":
    solve()

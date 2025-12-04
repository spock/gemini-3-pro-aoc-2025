
def solve():
    try:
        with open('day_3/input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = f.readlines()

    total_sum = 0
    k = 12

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        digits = [int(c) for c in line]
        n = len(digits)
        stack = []
        
        for i, digit in enumerate(digits):
            # While stack is not empty, current digit is larger than top,
            # and we have enough remaining digits to fill the stack to size k
            while stack and digit > stack[-1] and (len(stack) - 1 + (n - i)) >= k:
                stack.pop()
            
            if len(stack) < k:
                stack.append(digit)
        
        # In case we still have more than k (shouldn't happen with the logic above if n >= k)
        # But if n < k, we just take what we have (though problem implies n >= 12)
        result_digits = stack[:k]
        
        # Convert to integer
        if result_digits:
            num_str = "".join(map(str, result_digits))
            total_sum += int(num_str)
            
    print(f"Total output joltage: {total_sum}")
    
    try:
        with open('day_3/output2.txt', 'w') as f:
            f.write(str(total_sum))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(total_sum))

if __name__ == "__main__":
    solve()

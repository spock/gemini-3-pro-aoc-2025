import sys
import re
from itertools import product

def solve_system(buttons, target):
    """
    Solves Ax = b over GF(2)
    buttons: list of lists, where buttons[j] is the list of light indices toggled by button j.
             This forms the columns of A.
    target: list of booleans (0/1), target state of lights. This is b.
    
    Returns: min button presses (int)
    """
    num_lights = len(target)
    num_buttons = len(buttons)
    
    # Construct augmented matrix [A | b]
    # Rows are lights, Cols are buttons + target
    matrix = []
    for r in range(num_lights):
        row = []
        for c in range(num_buttons):
            if r in buttons[c]:
                row.append(1)
            else:
                row.append(0)
        row.append(target[r])
        matrix.append(row)
        
    # Gaussian elimination
    pivot_row = 0
    pivot_cols = []
    
    for c in range(num_buttons):
        if pivot_row >= num_lights:
            break
            
        # Find pivot
        curr = pivot_row
        while curr < num_lights and matrix[curr][c] == 0:
            curr += 1
            
        if curr == num_lights:
            continue
            
        # Swap rows
        matrix[pivot_row], matrix[curr] = matrix[curr], matrix[pivot_row]
        pivot_cols.append(c)
        
        # Eliminate other rows
        for r in range(num_lights):
            if r != pivot_row and matrix[r][c] == 1:
                # Add pivot row to row r (XOR)
                for k in range(c, num_buttons + 1):
                    matrix[r][k] ^= matrix[pivot_row][k]
                    
        pivot_row += 1

    # Check for consistency
    # If any row is all zeros except the last column, then 0 = 1 => impossible
    for r in range(pivot_row, num_lights):
        if matrix[r][num_buttons] == 1:
            return float('inf') # Should not happen based on problem description "determine the fewest... required" implying solution exists

    # Extract solution
    # Free variables are those columns not in pivot_cols
    free_vars = [c for c in range(num_buttons) if c not in pivot_cols]
    
    # We need to find min weight solution.
    # The system size is small enough to brute force free variables?
    # Let's check constraints. Line 1: 4 lights, 6 buttons.
    # Line 2: 5 lights, 5 buttons.
    # Line 3: 7 lights, 4 buttons.
    # The examples are small.
    # If free vars are many, it might be slow. But usually puzzle inputs are reasonable.
    
    min_presses = float('inf')
    
    # Iterate over all assignments of free variables
    for assignment in product([0, 1], repeat=len(free_vars)):
        # Construct solution vector x
        x = [0] * num_buttons
        
        # Set free variables
        for i, val in enumerate(assignment):
            x[free_vars[i]] = val
            
        # Back substitution for pivot variables
        # Iterate dimensions backwards
        # Equation for pivot_row i (which corresponds to pivot_col c):
        # x[c] + sum(matrix[i][k] * x[k] for k > c) = matrix[i][num_buttons]
        
        # We know matrix structure:
        # matrix[i][pivot_cols[i]] is 1.
        # matrix[i][c] is 0 for c < pivot_cols[i]
        
        # Be careful mapping pivot rows to pivot cols
        # pivot_cols[i] is the column index for the pivot in row i
        
        for i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[i]
            val = matrix[i][num_buttons]
            # Subtract (xor) contributions from variables to the right
            for k in range(col + 1, num_buttons):
                 if matrix[i][k] == 1:
                     val ^= x[k]
            x[col] = val
            
        min_presses = min(min_presses, sum(x))
        
    return min_presses

def parse_line(line):
    # Format: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # Extract lights part
    m_lights = re.match(r'^\[([.#]+)\]', line)
    if not m_lights:
        return None, None
    lights_str = m_lights.group(1)
    target = [1 if c == '#' else 0 for c in lights_str]
    
    # Extract buttons
    # Buttons are in parens ()
    # Remove the lights part and the braces part
    # A bit hacky but simple regex for ( ... ) groups finding
    
    # Find all (..._ content
    buttons_part = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    for b_str in buttons_part:
        indices = [int(x) for x in b_str.split(',')]
        buttons.append(indices)
        
    return target, buttons

def main():
    if len(sys.argv) < 2:
        print("Usage: python solution.py <input_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    
    total_presses = 0
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            target, buttons = parse_line(line)
            if target is None:
                continue
                
            pushes = solve_system(buttons, target)
            # print(f"Solved one: {pushes}")
            total_presses += pushes
            
    print(f"Total fewest presses: {total_presses}")
    
    # Write to output1.txt
    with open("output1.txt", "w") as f:
        f.write(str(total_presses))

if __name__ == '__main__':
    main()

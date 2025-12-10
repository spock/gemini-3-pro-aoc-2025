import sys
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve_with_milp(buttons, target):
    """
    Solves Ax = b for integer x >= 0 minimizing sum(x).
    """
    num_vars = len(buttons)
    num_eqs = len(target)
    
    # Construct A matrix
    # buttons[j] is list of row indices
    A = np.zeros((num_eqs, num_vars))
    for j, indices in enumerate(buttons):
        for i in indices:
            if i < num_eqs:
                A[i, j] = 1
                
    b = np.array(target)
    
    # Objective: Minimize sum of button presses
    c = np.ones(num_vars)
    
    # Constraints: Ax = b
    # LinearConstraint(A, lb, ub)
    constraints = LinearConstraint(A, lb=b, ub=b)
    
    # Variable bounds: x >= 0
    bounds = Bounds(lb=0, ub=np.inf)
    
    # Integrality: 1 means integer
    integrality = np.ones(num_vars)
    
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    
    if res.success:
        # res.x contains the solution
        # It might be floats close to integers, we round.
        # But res.fun is the objective value.
        return int(round(res.fun))
    else:
        # If it failed, it might be due to no solution or numerical issues?
        # For AoC usually there is a solution.
        # Check status
        # print(f"MILP failed: {res.message}")
        return float('inf')

def parse_line(line):
    # Format: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    m_joltage = re.search(r'\{([\d,]+)\}', line)
    if not m_joltage:
        return None, None
    joltage_str = m_joltage.group(1)
    target = [int(x) for x in joltage_str.split(',')]
    
    buttons_part = re.findall(r'\(([\d,]+)\)', line)
    buttons = []
    for b_str in buttons_part:
        indices = [int(x) for x in b_str.split(',')]
        buttons.append(indices)
        
    return target, buttons

def main():
    if len(sys.argv) < 2:
        print("Usage: python solution2.py <input_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    
    total_presses = 0
    count = 0
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            target, buttons = parse_line(line)
            if target is None:
                continue
            
            count += 1
            pushes = solve_with_milp(buttons, target)
            if pushes == float('inf'):
                print(f"No solution for machine {count}")
            else:
                total_presses += pushes
            
    print(f"Total fewest presses: {total_presses}")
    with open("output2.txt", "w") as f:
        f.write(str(total_presses))

if __name__ == '__main__':
    main()

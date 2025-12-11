import sys
import collections

def count_paths(start_node, end_node, graph, memo):
    if start_node == end_node:
        return 1
    if start_node not in graph:
        return 0
    
    # Memoization key needs to include end_node if we want to reuse memo generically, 
    # but here we can just clear memo or use (start, end) tuple.
    # Actually, for a fixed end_node, we can just memoize on start_node.
    # But since we call this function with different end_nodes, we should be careful.
    
    key = (start_node, end_node)
    if key in memo:
        return memo[key]
    
    total = 0
    for neighbor in graph[start_node]:
        total += count_paths(neighbor, end_node, graph, memo)
        
    memo[key] = total
    return total

def main():
    if len(sys.argv) < 2:
        print("Usage: python solve_task2.py <input_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    graph = collections.defaultdict(list)
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(':')
            if len(parts) != 2:
                continue
            
            src = parts[0].strip()
            dests = parts[1].strip().split()
            
            for d in dests:
                graph[src].append(d)
                
    # We need paths from svr to out visiting dac AND fft.
    # Possibility 1: svr -> ... -> dac -> ... -> fft -> ... -> out
    # Possibility 2: svr -> ... -> fft -> ... -> dac -> ... -> out
    
    memo = {}
    
    # Path 1: svr -> dac -> fft -> out
    s_d = count_paths('svr', 'dac', graph, memo)
    d_f = count_paths('dac', 'fft', graph, memo)
    f_o = count_paths('fft', 'out', graph, memo)
    
    total_1 = s_d * d_f * f_o
    
    # Path 2: svr -> fft -> dac -> out
    s_f = count_paths('svr', 'fft', graph, memo)
    f_d = count_paths('fft', 'dac', graph, memo)
    d_o = count_paths('dac', 'out', graph, memo)
    
    total_2 = s_f * f_d * d_o
    
    grand_total = total_1 + total_2
    
    print(f"Paths visiting both dac and fft: {grand_total}")
    
    with open("output2.txt", "w") as f:
        f.write(str(grand_total))

if __name__ == '__main__':
    main()

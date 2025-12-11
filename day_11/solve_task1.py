import sys
import collections

def count_paths(node, graph, memo):
    if node == 'out':
        return 1
    if node not in graph:
        return 0
    if node in memo:
        return memo[node]
    
    total = 0
    for neighbor in graph[node]:
        total += count_paths(neighbor, graph, memo)
        
    memo[node] = total
    return total

def main():
    if len(sys.argv) < 2:
        print("Usage: python solve_task1.py <input_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    graph = collections.defaultdict(list)
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Parse line: "aaa: you hhh"
            parts = line.split(':')
            if len(parts) != 2:
                continue
            
            src = parts[0].strip()
            dests = parts[1].strip().split()
            
            for d in dests:
                graph[src].append(d)
                
    memo = {}
    result = count_paths('you', graph, memo)
    
    print(f"Total paths from you to out: {result}")
    
    with open("output1.txt", "w") as f:
        f.write(str(result))

if __name__ == '__main__':
    main()

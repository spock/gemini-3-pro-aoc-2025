import sys

def main():
    nodes = set()
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.split(':')
            src = parts[0].strip()
            nodes.add(src)
            if len(parts) > 1:
                dests = parts[1].strip().split()
                for d in dests:
                    nodes.add(d)
    
    print("Nodes found:", " ".join(sorted(list(nodes))))
    
if __name__ == '__main__':
    main()

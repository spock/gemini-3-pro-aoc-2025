
def solve():
    try:
        with open('day_8/input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

    points = []
    for line in lines:
        points.append(list(map(int, line.split(','))))

    num_points = len(points)
    edges = []

    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
            edges.append((dist_sq, i, j))

    edges.sort(key=lambda x: x[0])

    # DSU
    parent = list(range(num_points))
    size = [1] * num_points

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Union by size
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]
            return True
        return False

    # Connect 1000 pairs (shortest edges)
    # The requirement says "connect together the 1000 pairs of junction boxes which are closest together"
    # This implies taking the first 1000 edges from the sorted list.
    
    limit = 1000
    if len(edges) < limit:
        limit = len(edges)
        
    for k in range(limit):
        _, u, v = edges[k]
        union(u, v)

    # Collect component sizes
    root_sizes = {}
    for i in range(num_points):
        root = find(i)
        root_sizes[root] = size[root] # size[root] is accurate after unions.
        
    sizes = list(root_sizes.values())
    sizes.sort(reverse=True)
    
    result = 1
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
    elif len(sizes) > 0:
        for s in sizes:
            result *= s
    else:
        result = 0

    print(f"Product of 3 largest: {result}")
    
    try:
        with open('day_8/output1.txt', 'w') as f:
            f.write(str(result))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(result))

if __name__ == "__main__":
    solve()


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
    num_components = num_points

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i
            return True
        return False

    result = 0
    
    for dist, u, v in edges:
        if union(u, v):
            num_components -= 1
            if num_components == 1:
                # Connected everything!
                result = points[u][0] * points[v][0]
                break

    print(f"Product of coordinates: {result}")
    
    try:
        with open('day_8/output2.txt', 'w') as f:
            f.write(str(result))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(result))

if __name__ == "__main__":
    solve()

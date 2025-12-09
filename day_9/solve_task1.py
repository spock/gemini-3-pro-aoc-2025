
def solve():
    try:
        with open('day_9/input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        with open('input.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

    points = []
    for line in lines:
        points.append(list(map(int, line.split(','))))

    num_points = len(points)
    max_area = 0

    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1 = points[i]
            p2 = points[j]
            
            # The problem states: uses red tiles for two of its opposite corners.
            # Area is inclusive of the tiles themselves.
            # Width = abs(x1 - x2) + 1
            # Height = abs(y1 - y2) + 1
            
            width = abs(p1[0] - p2[0]) + 1
            height = abs(p1[1] - p2[1]) + 1
            area = width * height
            
            if area > max_area:
                max_area = area

    print(f"Max Rectangle Area: {max_area}")
    
    try:
        with open('day_9/output1.txt', 'w') as f:
            f.write(str(max_area))
    except FileNotFoundError:
         with open('output1.txt', 'w') as f:
            f.write(str(max_area))

if __name__ == "__main__":
    solve()

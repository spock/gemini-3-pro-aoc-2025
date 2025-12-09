
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
    
    # Define polygon edges
    poly_edges = []
    for i in range(num_points):
        p1 = points[i]
        p2 = points[(i + 1) % num_points]
        poly_edges.append((p1, p2))

    # Generate all pairs (rectangles)
    rectangles = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1 = points[i]
            p2 = points[j]
            
            x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
            y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            width = x2 - x1 + 1
            height = y2 - y1 + 1
            area = width * height
            
            # Use tuple for sorting/storage: (area, x1, y1, x2, y2)
            # Storing coordinates inclusive
            rectangles.append((area, x1, y1, x2, y2))

    # Sort checks by area descending
    rectangles.sort(key=lambda x: x[0], reverse=True)

    def is_point_on_edge(px, py, edge):
        (ex1, ey1), (ex2, ey2) = edge
        if ex1 == ex2: # Vertical
            if ex1 == px and min(ey1, ey2) <= py <= max(ey1, ey2):
                return True
        else: # Horizontal
            if ey1 == py and min(ex1, ex2) <= px <= max(ex1, ex2):
                return True
        return False

    def is_center_inside(rx1, ry1, rx2, ry2, poly_edges):
        cx = (rx1 + rx2) / 2
        cy = (ry1 + ry2) / 2
        
        # Ray cast to right
        intersections = 0
        on_edge = False
        
        for p1, p2 in poly_edges:
            # Check if center is on edge (unlikely with half-integers unless width/height is 1)
            # If coordinates are integers, and center is half-int, it won't be on integer edge.
            # But width/height could be even/odd.
            if is_point_on_edge(cx, cy, (p1, p2)):
                return True
            
            # Ray casting for Y
            # Edge must straddle cy
            # Check vertical edges?
            # Standard algo: check edges that cross Y-level of point
            
            y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
            if y_min <= cy < y_max:
                # Calculate x intersection
                # p1, p2
                if p1[0] == p2[0]: # Vertical edge
                    x_int = p1[0]
                else: # Horizontal edge - cannot cross Y level unless it IS Y level (handled by on_edge)
                    continue
                
                if x_int > cx:
                    intersections += 1
                    
        return (intersections % 2) == 1

    def edges_intersect_rect_interior(rx1, ry1, rx2, ry2, poly_edges):
        # Rect x range: (rx1, rx2), y range: (ry1, ry2)
        # Strict intersection
        for p1, p2 in poly_edges:
            x_min_e, x_max_e = min(p1[0], p2[0]), max(p1[0], p2[0])
            y_min_e, y_max_e = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            if p1[0] == p2[0]: # Vertical Edge
                # Must be strictly between rect xs
                if rx1 < p1[0] < rx2:
                    # Y intervals must overlap
                    if max(ry1, y_min_e) < min(ry2, y_max_e):
                        return True
            else: # Horizontal Edge
                # Must be strictly between rect ys
                if ry1 < p1[1] < ry2:
                    # X intervals must overlap
                    if max(rx1, x_min_e) < min(rx2, x_max_e):
                        return True
        return False

    max_valid_area = 0
    
    for area, x1, y1, x2, y2 in rectangles:
        # Optimization
        if area <= max_valid_area:
            break
            
        if is_center_inside(x1, y1, x2, y2, poly_edges):
            if not edges_intersect_rect_interior(x1, y1, x2, y2, poly_edges):
                max_valid_area = area
                # Since we sorted descending, the first valid one is the max
                break

    print(f"Max Valid Area: {max_valid_area}")
    
    try:
        with open('day_9/output2.txt', 'w') as f:
            f.write(str(max_valid_area))
    except FileNotFoundError:
         with open('output2.txt', 'w') as f:
            f.write(str(max_valid_area))

if __name__ == "__main__":
    solve()

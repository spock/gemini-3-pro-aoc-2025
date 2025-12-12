import sys
import copy

class Shape:
    def __init__(self, index, coords):
        self.index = index
        # Normalize coords locally (0,0 based)
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        self.coords = frozenset((r - min_r, c - min_c) for r, c in coords)
        self.height = max(r for r, c in self.coords) + 1
        self.width = max(c for r, c in self.coords) + 1
        
    def generate_variants(self):
        """Generate all unique rotations and flips."""
        variants = set()
        
        current = self.coords
        
        # 4 rotations
        for _ in range(4):
            # Add current
            variants.add(self._normalize(current))
            # Flux (Mirror x) and add
            variants.add(self._normalize(self._flip(current)))
            
            # Rotate 90 deg
            current = self._rotate(current)
            
        return [Shape(self.index, v) for v in variants]
    
    def _normalize(self, coords):
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        return frozenset((r - min_r, c - min_c) for r, c in coords)
        
    def _rotate(self, coords):
        # Rotate 90 degrees clockwise: (r, c) -> (c, -r)
        return set((c, -r) for r, c in coords)
        
    def _flip(self, coords):
        # Flip vertically: (r, c) -> (-r, c)
        return set((-r, c) for r, c in coords)

def parse_input(filepath):
    shapes = {}
    queries = []
    
    with open(filepath, 'r') as f:
        lines = [line.rstrip() for line in f]
        
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if not line:
            idx += 1
            continue
            
        # Check for query line "WxH: ..."
        if ':' in line and 'x' in line.split(':')[0]:
            # Query section
            parts = line.split(':')
            dim_part = parts[0]
            count_part = parts[1]
            w, h = map(int, dim_part.split('x'))
            counts = list(map(int, count_part.strip().split()))
            queries.append({
                'w': w,
                'h': h,
                'counts': counts
            })
            idx += 1
        else:
            # Shape definition "ID:"
            if line.endswith(':'):
                shape_id = int(line[:-1])
                idx += 1
                coords = set()
                r = 0
                while idx < len(lines) and lines[idx].strip() != "" and not (':' in lines[idx] and 'x' in lines[idx].split(':')[0]) and not lines[idx].endswith(':'):
                    # It's a shape row
                    row_str = lines[idx]
                    for c, char in enumerate(row_str):
                        if char == '#':
                            coords.add((r, c))
                    r += 1
                    idx += 1
                shapes[shape_id] = Shape(shape_id, coords)
            else:
                idx += 1
                
    return shapes, queries

def solve_region(w, h, pieces):
    # pieces is a list of Shape objects (variants lists actually?)
    # No, let's pass list of (shape_id, variants)
    # Optimization: area check
    total_area = sum(len(p[0].coords) for p in pieces)
    if total_area > w * h:
        return False
        
    # Sort pieces by size (descending)
    pieces.sort(key=lambda x: len(x[0].coords), reverse=True)
    
    # Grid: True if occupied
    grid = [[False] * w for _ in range(h)]
    
    return backtrack(0, pieces, grid, w, h)

def backtrack(idx, pieces, grid, W, H):
    if idx == len(pieces):
        return True
    
    variants = pieces[idx]
    
    # Try to place this piece
    # Heuristic: Optimization - Find the first free cell?
    # Actually, for the current piece, we can place it anywhere valid.
    # To reduce search space, we can enforce that the first piece is placed "top-left-most" available?
    # Or just standard packing: try all positions.
    # HOWEVER, naive try all positions is slow. 
    # Better: Scan the grid for the first empty cell. The current piece MUST cover that cell?
    # NO, that's exact cover / pentomino puzzle style. That works if we must fill the grid completely.
    # But here we don't need to fill the grid, just fit pieces.
    # So we don't have to cover the first empty cell.
    
    # But finding the "first available slot" for the piece is distinct.
    
    # Let's iterate over positions (r, c).
    # Optimization: To avoid symmetry in placement of the *first* piece if grid is empty?
    # Maybe not worth complexity.
    
    # Optimization: If pieces are identical, ordering doesn't matter.
    # We handled this by flattening the list of pieces. If we have multiple same shapes, 
    # we treat them as Check 1, Check 2. We can enforce an ordering on their positions to break symmetry.
    # E.g. Piece A1 must be "before" Piece A2.
    # Let's verify if we need this. 6 shapes, total ~30-40 squares area?
    # Grid 50x50 is 2500 squares. 30 area is tiny.
    # Wait, the example density is low.
    # 4x4 region, shape index 4 (3 blocks). 2 of them. 2*3 = 6 blocks. 16 cells. WAAAAY low density.
    # If density is low, "try all positions" is expensive (lots of valid positions).
    
    # But wait, pieces are small?
    # "39x35: 35 44 39 31 39 25" -> counts are high!
    # 35 of shape 0, 44 of shape 1...
    # Sum of counts ~ 200 pieces?
    # Each piece ~4 blocks. Total area ~800.
    # Grid 39x35 = 1365.
    # Density is actually high! > 50%.
    
    # If density is high, "first empty cell" heuristic is good?
    # But we don't *have* to cover the first empty cell.
    
    # Let's stick to standard backtracking: place current piece in first valid position, then next valid position...
    # This might be slow if the solution is "deep" in the tree.
    
    # Pruning: Is there enough space left? (Area check).
    # Pruning: Largest empty rectangle?
    
    # Let's try simple first.
    
    # The piece variants are pre-calculated.
    
    for variant in variants:
        # Try to place variant at (r, c)
        # Scan grid
        # Optimization: only check valid ranges
        max_r = H - variant.height
        max_c = W - variant.width
        
        for r in range(max_r + 1):
            for c in range(max_c + 1):
                if can_place(grid, variant, r, c):
                    place(grid, variant, r, c, True)
                    if backtrack(idx + 1, pieces, grid, W, H):
                        return True
                    place(grid, variant, r, c, False)
                    
    return False

def can_place(grid, shape, r, c):
    for dr, dc in shape.coords:
        if grid[r + dr][c + dc]:
            return False
    return True

def place(grid, shape, r, c, val):
    for dr, dc in shape.coords:
        grid[r + dr][c + dc] = val

def main():
    if len(sys.argv) < 2:
        print("Usage: python solve_puzzle.py <input_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    raw_shapes, queries = parse_input(filepath)
    
    # Pre-calculate variants for all distinct shapes
    variants_map = {}
    for sid, shape in raw_shapes.items():
        variants_map[sid] = shape.generate_variants()
        
    total_valid = 0
    
    for i, q in enumerate(queries):
        W, H = q['w'], q['h']
        counts = q['counts']
        
        # Build pieces list
        pieces = []
        for sid, count in enumerate(counts):
            if count > 0 and sid in variants_map:
                # Add 'count' copies of this shape's variants
                # Note: pass reference to variants list is fine
                for _ in range(count):
                    pieces.append(variants_map[sid])
            elif count > 0:
                # Referenced shape not found? Should not happen based on problem
                pass
                
        # print(f"Checking region {i}: {W}x{H} with {len(pieces)} pieces...")
        if solve_region(W, H, pieces):
            # print(f"Region {i} FITS")
            total_valid += 1
        else:
            # print(f"Region {i} NO FIT")
            pass
            
    print(f"Total regions that fit: {total_valid}")
    with open("output1.txt", "w") as f:
        f.write(str(total_valid))

if __name__ == '__main__':
    # Increase recursion depth just in case
    sys.setrecursionlimit(20000)
    main()

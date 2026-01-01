import math

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Line:
    """Defined by two points P1 and P2 or by coefficients ax + by + c = 0"""
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        # Standard form: ax + by + c = 0
        self.a = p1.y - p2.y
        self.b = p2.x - p1.x
        self.c = p1.x * p2.y - p2.x * p1.y

    def __repr__(self):
        return f"Line({self.a:.2f}x + {self.b:.2f}y + {self.c:.2f} = 0)"

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = float(radius)

    def __repr__(self):
        return f"Circle(Center: {self.center}, Radius: {self.radius:.2f})"

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.points = [p1, p2, p3]

    def __repr__(self):
        return f"Triangle({self.points[0]}, {self.points[1]}, {self.points[2]})"

# --- 1. Intersection Calculations ---

def intersect_lines(l1: Line, l2: Line):
    det = l1.a * l2.b - l2.a * l1.b
    if abs(det) < 1e-9:
        return None  # Parallel
    x = (l1.b * l2.c - l2.b * l1.c) / det
    y = (l2.a * l1.c - l1.a * l2.c) / det
    return Point(x, y)

def intersect_line_circle(line: Line, circle: Circle):
    # Distance from center to line
    dist = abs(line.a * circle.center.x + line.b * circle.center.y + line.c) / math.sqrt(line.a**2 + line.b**2)
    if dist > circle.radius:
        return []
    
    # Projection of center onto line (Perpendicular Foot)
    p_foot = get_perpendicular_foot(circle.center, line)
    
    if abs(dist - circle.radius) < 1e-9:
        return [p_foot]
    
    # Distance from foot to intersection points
    h = math.sqrt(circle.radius**2 - dist**2)
    # Unit vector along the line
    dx = line.p2.x - line.p1.x
    dy = line.p2.y - line.p1.y
    length = math.sqrt(dx**2 + dy**2)
    ux, uy = dx/length, dy/length
    
    return [
        Point(p_foot.x + ux * h, p_foot.y + uy * h),
        Point(p_foot.x - ux * h, p_foot.y - uy * h)
    ]

def intersect_circles(c1: Circle, c2: Circle):
    d = c1.center.distance_to(c2.center)
    if d > c1.radius + c2.radius or d < abs(c1.radius - c2.radius) or d == 0:
        return []
    
    # Radical axis: 2x(x2-x1) + 2y(y2-y1) = r1^2 - r2^2 - x1^2 + x2^2 - y1^2 + y2^2
    # This reduces to a line-circle intersection problem
    a = 2 * (c2.center.x - c1.center.x)
    b = 2 * (c2.center.y - c1.center.y)
    c = c1.center.x**2 + c1.center.y**2 - c2.center.x**2 - c2.center.y**2 - c1.radius**2 + c2.radius**2
    
    # Construct a dummy line using the linear equation ax + by + c = 0
    # To use our intersect_line_circle, we need two points on this radical axis
    if abs(b) > 1e-9:
        p1 = Point(0, -c/b)
        p2 = Point(1, -(c+a)/b)
    else:
        p1 = Point(-c/a, 0)
        p2 = Point(-c/a, 1)
        
    radical_line = Line(p1, p2)
    return intersect_line_circle(radical_line, c1)

# --- 2. Perpendicular and Pythagorean Verification ---

def get_perpendicular_foot(p: Point, line: Line):
    k = - (line.a * p.x + line.b * p.y + line.c) / (line.a**2 + line.b**2)
    return Point(p.x + k * line.a, p.y + k * line.b)

def verify_pythagoras():
    print("--- Pythagorean Verification ---")
    line = Line(Point(0, 0), Point(10, 0)) # Horizontal line on X axis
    p_ext = Point(5, 5)                    # Point above line
    p_foot = get_perpendicular_foot(p_ext, line)
    p_on_line = Point(0, 0)                # Another point on line
    
    # Triangle: (p_ext, p_foot, p_on_line) - Right angle at p_foot
    a = p_ext.distance_to(p_foot)
    b = p_foot.distance_to(p_on_line)
    c = p_ext.distance_to(p_on_line)
    
    print(f"Sides: a={a:.2f}, b={b:.2f}, hypotenuse c={c:.2f}")
    print(f"a^2 + b^2 = {a**2 + b**2:.2f}")
    print(f"c^2       = {c**2:.2f}")
    assert math.isclose(a**2 + b**2, c**2)

# --- 3. Transformations ---

class Transformer:
    @staticmethod
    def translate(obj, dx, dy):
        if isinstance(obj, Point): return Point(obj.x + dx, obj.y + dy)
        if isinstance(obj, Line): return Line(Transformer.translate(obj.p1, dx, dy), Transformer.translate(obj.p2, dx, dy))
        if isinstance(obj, Circle): return Circle(Transformer.translate(obj.center, dx, dy), obj.radius)
        if isinstance(obj, Triangle): return Triangle(*(Transformer.translate(p, dx, dy) for p in obj.points))

    @staticmethod
    def scale(obj, factor, center=Point(0,0)):
        def scale_pt(p):
            return Point(center.x + (p.x - center.x) * factor, center.y + (p.y - center.y) * factor)
        
        if isinstance(obj, Point): return scale_pt(obj)
        if isinstance(obj, Line): return Line(scale_pt(obj.p1), scale_pt(obj.p2))
        if isinstance(obj, Circle): return Circle(scale_pt(obj.center), obj.radius * factor)
        if isinstance(obj, Triangle): return Triangle(*(scale_pt(p) for p in obj.points))

    @staticmethod
    def rotate(obj, angle_deg, center=Point(0,0)):
        rad = math.radians(angle_deg)
        def rotate_pt(p):
            nx = center.x + (p.x - center.x) * math.cos(rad) - (p.y - center.y) * math.sin(rad)
            ny = center.y + (p.x - center.x) * math.sin(rad) + (p.y - center.y) * math.cos(rad)
            return Point(nx, ny)
        
        if isinstance(obj, Point): return rotate_pt(obj)
        if isinstance(obj, Line): return Line(rotate_pt(obj.p1), rotate_pt(obj.p2))
        if isinstance(obj, Circle): return Circle(rotate_pt(obj.center), obj.radius)
        if isinstance(obj, Triangle): return Triangle(*(rotate_pt(p) for p in obj.points))

# --- Execution ---
if __name__ == "__main__":
    verify_pythagoras()
    
    # Transformation Example
    tri = Triangle(Point(0,0), Point(2,0), Point(1,2))
    shifted_tri = Transformer.translate(tri, 5, 5)
    rotated_tri = Transformer.rotate(tri, 90)
    
    print("\n--- Transformation Test ---")
    print(f"Original: {tri}")
    print(f"Rotated 90deg: {rotated_tri}")
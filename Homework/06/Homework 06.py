import math
from typing import List, Tuple, Optional

# =========================
# Basic Geometry Objects
# =========================
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.3f}, {self.y:.3f})"

    # translation
    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    # scaling (relative to origin)
    def scale(self, sx: float, sy: float):
        self.x *= sx
        self.y *= sy

    # rotation (around origin)
    def rotate(self, angle_deg: float):
        angle_rad = math.radians(angle_deg)
        x_new = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_new = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        self.x, self.y = x_new, y_new


class Line:
    # Line defined by Ax + By + C = 0
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self):
        return f"Line({self.A}x + {self.B}y + {self.C} = 0)"

    # intersection with another line
    def intersection(self, other: 'Line') -> Optional[Point]:
        det = self.A * other.B - other.A * self.B
        if det == 0:
            return None  # parallel lines
        x = (self.B * other.C - other.B * self.C) / det
        y = (other.A * self.C - self.A * other.C) / det
        return Point(x, y)

    # perpendicular from a point
    def perpendicular_from_point(self, p: Point) -> Point:
        # Line equation: Ax + By + C = 0
        # Foot of perpendicular: (x0, y0)
        denom = self.A**2 + self.B**2
        x0 = (self.B*(self.B*p.x - self.A*p.y) - self.A*self.C) / denom
        y0 = (self.A*(-self.B*p.x + self.A*p.y) - self.B*self.C) / denom
        return Point(x0, y0)


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(center={self.center}, r={self.radius})"

    # intersection with another circle
    def intersection_with_circle(self, other: 'Circle') -> List[Point]:
        # Refer to circle-circle intersection formulas
        x0, y0 = self.center.x, self.center.y
        x1, y1 = other.center.x, other.center.y
        r0, r1 = self.radius, other.radius

        dx, dy = x1 - x0, y1 - y0
        d = math.hypot(dx, dy)

        if d > r0 + r1 or d < abs(r0 - r1) or d == 0:
            return []  # no intersection or coincident circles

        a = (r0**2 - r1**2 + d**2) / (2*d)
        h = math.sqrt(r0**2 - a**2)

        x2 = x0 + a * dx / d
        y2 = y0 + a * dy / d

        rx = -dy * (h/d)
        ry = dx * (h/d)

        p1 = Point(x2 + rx, y2 + ry)
        p2 = Point(x2 - rx, y2 - ry)
        return [p1, p2]

    # intersection with a line
    def intersection_with_line(self, line: Line) -> List[Point]:
        A, B, C = line.A, line.B, line.C
        h, k, r = self.center.x, self.center.y, self.radius
        points = []

        if B != 0:
            # y = (-A*x - C)/B
            a = 1 + (A/B)**2
            b = 2*A*C/B**2 + 2*A*k/B - 2*h
            c = h**2 + k**2 + (C/B)**2 - 2*k*C/B - r**2
            disc = b**2 - 4*a*c
            if disc < 0:
                return []
            sqrt_disc = math.sqrt(disc)
            x1 = (-b + sqrt_disc) / (2*a)
            x2 = (-b - sqrt_disc) / (2*a)
            y1 = (-A*x1 - C)/B
            y2 = (-A*x2 - C)/B
            points = [Point(x1, y1), Point(x2, y2)]
        elif A != 0:
            # vertical line x = -C/A
            x = -C/A
            delta = r**2 - (x - h)**2
            if delta < 0:
                return []
            y1 = k + math.sqrt(delta)
            y2 = k - math.sqrt(delta)
            points = [Point(x, y1), Point(x, y2)]

        return points


# =========================
# Triangle Object
# =========================
class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

    # translation
    def translate(self, dx: float, dy: float):
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)
        self.p3.translate(dx, dy)

    # scaling
    def scale(self, sx: float, sy: float):
        self.p1.scale(sx, sy)
        self.p2.scale(sx, sy)
        self.p3.scale(sx, sy)

    # rotation
    def rotate(self, angle_deg: float):
        self.p1.rotate(angle_deg)
        self.p2.rotate(angle_deg)
        self.p3.rotate(angle_deg)


# =========================
# Pythagorean Theorem Verification
# =========================
def verify_pythagoras(line: Line, external_point: Point) -> bool:
    foot = line.perpendicular_from_point(external_point)
    a = math.hypot(external_point.x - foot.x, external_point.y - foot.y)
    b = math.hypot(foot.x, foot.y)  # assuming line passes through origin
    c = math.hypot(external_point.x, external_point.y)
    return abs(a**2 + b**2 - c**2) < 1e-6


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    # Example points
    p1 = Point(0, 0)
    p2 = Point(1, 2)

    # Example line: y = x -> -x + y = 0
    line1 = Line(-1, 1, 0)
    line2 = Line(1, 1, -4)

    print("Intersection of lines:", line1.intersection(line2))

    circle1 = Circle(Point(0, 0), 5)
    circle2 = Circle(Point(4, 0), 3)

    print("Circle-Circle intersection:", circle1.intersection_with_circle(circle2))

    print("Line-Circle intersection:", circle1.intersection_with_line(line2))

    # Triangle example
    tri = Triangle(Point(0,0), Point(3,0), Point(0,4))
    print("Original triangle:", tri)
    tri.translate(1,1)
    print("Translated triangle:", tri)
    tri.rotate(90)
    print("Rotated triangle:", tri)

    # Pythagorean verification
    external_point = Point(3,4)
    line = Line(1, 0, 0)  # x=0 vertical line
    print("Pythagorean verification:", verify_pythagoras(line, external_point))
import math
from typing import List, Tuple, Optional

# =========================
# Basic Geometry Objects
# =========================
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.3f}, {self.y:.3f})"

    # translation
    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    # scaling (relative to origin)
    def scale(self, sx: float, sy: float):
        self.x *= sx
        self.y *= sy

    # rotation (around origin)
    def rotate(self, angle_deg: float):
        angle_rad = math.radians(angle_deg)
        x_new = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_new = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        self.x, self.y = x_new, y_new


class Line:
    # Line defined by Ax + By + C = 0
    def __init__(self, A: float, B: float, C: float):
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self):
        return f"Line({self.A}x + {self.B}y + {self.C} = 0)"

    # intersection with another line
    def intersection(self, other: 'Line') -> Optional[Point]:
        det = self.A * other.B - other.A * self.B
        if det == 0:
            return None  # parallel lines
        x = (self.B * other.C - other.B * self.C) / det
        y = (other.A * self.C - self.A * other.C) / det
        return Point(x, y)

    # perpendicular from a point
    def perpendicular_from_point(self, p: Point) -> Point:
        # Line equation: Ax + By + C = 0
        # Foot of perpendicular: (x0, y0)
        denom = self.A**2 + self.B**2
        x0 = (self.B*(self.B*p.x - self.A*p.y) - self.A*self.C) / denom
        y0 = (self.A*(-self.B*p.x + self.A*p.y) - self.B*self.C) / denom
        return Point(x0, y0)


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(center={self.center}, r={self.radius})"

    # intersection with another circle
    def intersection_with_circle(self, other: 'Circle') -> List[Point]:
        # Refer to circle-circle intersection formulas
        x0, y0 = self.center.x, self.center.y
        x1, y1 = other.center.x, other.center.y
        r0, r1 = self.radius, other.radius

        dx, dy = x1 - x0, y1 - y0
        d = math.hypot(dx, dy)

        if d > r0 + r1 or d < abs(r0 - r1) or d == 0:
            return []  # no intersection or coincident circles

        a = (r0**2 - r1**2 + d**2) / (2*d)
        h = math.sqrt(r0**2 - a**2)

        x2 = x0 + a * dx / d
        y2 = y0 + a * dy / d

        rx = -dy * (h/d)
        ry = dx * (h/d)

        p1 = Point(x2 + rx, y2 + ry)
        p2 = Point(x2 - rx, y2 - ry)
        return [p1, p2]

    # intersection with a line
    def intersection_with_line(self, line: Line) -> List[Point]:
        A, B, C = line.A, line.B, line.C
        h, k, r = self.center.x, self.center.y, self.radius
        points = []

        if B != 0:
            # y = (-A*x - C)/B
            a = 1 + (A/B)**2
            b = 2*A*C/B**2 + 2*A*k/B - 2*h
            c = h**2 + k**2 + (C/B)**2 - 2*k*C/B - r**2
            disc = b**2 - 4*a*c
            if disc < 0:
                return []
            sqrt_disc = math.sqrt(disc)
            x1 = (-b + sqrt_disc) / (2*a)
            x2 = (-b - sqrt_disc) / (2*a)
            y1 = (-A*x1 - C)/B
            y2 = (-A*x2 - C)/B
            points = [Point(x1, y1), Point(x2, y2)]
        elif A != 0:
            # vertical line x = -C/A
            x = -C/A
            delta = r**2 - (x - h)**2
            if delta < 0:
                return []
            y1 = k + math.sqrt(delta)
            y2 = k - math.sqrt(delta)
            points = [Point(x, y1), Point(x, y2)]

        return points


# =========================
# Triangle Object
# =========================
class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

    # translation
    def translate(self, dx: float, dy: float):
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)
        self.p3.translate(dx, dy)

    # scaling
    def scale(self, sx: float, sy: float):
        self.p1.scale(sx, sy)
        self.p2.scale(sx, sy)
        self.p3.scale(sx, sy)

    # rotation
    def rotate(self, angle_deg: float):
        self.p1.rotate(angle_deg)
        self.p2.rotate(angle_deg)
        self.p3.rotate(angle_deg)


# =========================
# Pythagorean Theorem Verification
# =========================
def verify_pythagoras(line: Line, external_point: Point) -> bool:
    foot = line.perpendicular_from_point(external_point)
    a = math.hypot(external_point.x - foot.x, external_point.y - foot.y)
    b = math.hypot(foot.x, foot.y)  # assuming line passes through origin
    c = math.hypot(external_point.x, external_point.y)
    return abs(a**2 + b**2 - c**2) < 1e-6


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    # Example points
    p1 = Point(0, 0)
    p2 = Point(1, 2)

    # Example line: y = x -> -x + y = 0
    line1 = Line(-1, 1, 0)
    line2 = Line(1, 1, -4)

    print("Intersection of lines:", line1.intersection(line2))

    circle1 = Circle(Point(0, 0), 5)
    circle2 = Circle(Point(4, 0), 3)

    print("Circle-Circle intersection:", circle1.intersection_with_circle(circle2))

    print("Line-Circle intersection:", circle1.intersection_with_line(line2))

    # Triangle example
    tri = Triangle(Point(0,0), Point(3,0), Point(0,4))
    print("Original triangle:", tri)
    tri.translate(1,1)
    print("Translated triangle:", tri)
    tri.rotate(90)
    print("Rotated triangle:", tri)

    # Pythagorean verification
    external_point = Point(3,4)
    line = Line(1, 0, 0)  # x=0 vertical line
    print("Pythagorean verification:", verify_pythagoras(line, external_point))

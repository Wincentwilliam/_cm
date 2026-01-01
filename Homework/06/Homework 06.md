# 2D Geometry Toolkit

A Python-based geometric engine to define fundamental shapes (Points, Lines, Circles, Triangles) and perform complex operations like intersection detection, perpendicular projections, and affine transformations.

## Features

- **Geometric Definitions**: Object-oriented representation of `Point`, `Line`, `Circle`, and `Triangle`.
- **Intersection Algorithms**: 
  - Line-Line intersections.
  - Line-Circle intersections.
  - Circle-Circle intersections.
- **Geometric Construction**: Calculate the perpendicular foot from a point to a line.
- **Theorem Verification**: Automated verification of the Pythagorean Theorem using generated coordinates.
- **Transformations**: Support for **Translation**, **Scaling**, and **Rotation**.

---

## Mathematical Background

### 1. Geometric Intersections

**Line-Line Intersection**  
Lines are represented in the standard form: `ax + by + c = 0`. Finding the intersection involves solving a system of two linear equations using **Cramer's Rule**. If the determinant is zero, the lines are parallel.

**Line-Circle Intersection**  
1. Calculate the shortest distance `d` from the circle center to the line.
2. If `d > r`, no intersection exists.
3. If `d <= r`, find the perpendicular foot of the center onto the line.
4. Calculate the offset `h = sqrt(r^2 - d^2)` to find the specific points along the line.

**Circle-Circle Intersection**  
By subtracting the equations of two circles, the quadratic terms (x² and y²) cancel out, leaving a linear equation: `ax + by + c = 0`. This is the **Radical Axis**. The intersection points of the circles are found by intersecting this line with either circle.

---

### 2. Perpendicular Foot and Pythagoras

- **Perpendicular Foot**: To find the projection of point `P` onto line `L`, we calculate a point `P'` such that the vector `PP'` is parallel to the line's normal vector `(a, b)`.
- **Pythagorean Theorem**: In a right triangle with legs `a, b` and hypotenuse `c`, the script verifies that `a² + b² = c²` by calculating Euclidean distances between the generated points.

---

### 3. Transformations (Linear Algebra)

- **Translation**: Vector addition: `P' = P + V`.
- **Scaling**: Resizing relative to center `C`: `P' = C + s(P - C)`.
- **Rotation**: Rotating a point `(x, y)` by angle `θ` using the rotation matrix:
  - `x' = x * cos(θ) - y * sin(θ)`
  - `y' = x * sin(θ) + y * cos(θ)`

---

## Usage

### Running the Script
```bash
python geometry_toolkit.py
```
import cmath

def root2(a, b, c):
    disc = cmath.sqrt(b*b - 4*a*c)   
    x1 = (-b + disc) / (2*a)
    x2 = (-b - disc) / (2*a)
    return (x1, x2)

print(root2(1, -5, 6))   
print(root2(1, 4, 3))    
print(root2(1, 1, 1))    
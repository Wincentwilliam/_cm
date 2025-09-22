import math

def root3(a, b, c, d):
    if a == 0:
        return

    b1 = b / a
    c1 = c / a
    d1 = d / a

    p = c1 - (b1**2) / 3
    q = (2*b1**3)/27 - (b1*c1)/3 + d1

    delta = (q/2)**2 + (p/3)**3
    print(f"判別式 Δ = {delta:.4f}")

    if delta <= 0:
        phi = math.acos(-q / (2 * math.sqrt(- (p**3)/27)))
        m = 2 * math.sqrt(-p/3)
        r1 = m*math.cos(phi/3) - b1/3
        r2 = m*math.cos((phi+2*math.pi)/3) - b1/3
        r3 = m*math.cos((phi+4*math.pi)/3) - b1/3
        print("answer:", (r1, r2, r3))

root3(1, -6, 11, -6)   

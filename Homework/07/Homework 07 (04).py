import math

EPS = 1e-12

# ===============================
# Entropy, Cross-Entropy, KL
# ===============================
def entropy(p_dist, base=2):
    H = 0.0
    for p in p_dist:
        if p > 0:
            H -= p * math.log(p, base)
    return H

def cross_entropy(p_dist, q_dist, base=2):
    return -sum(p * math.log(max(q, EPS), base) for p, q in zip(p_dist, q_dist))

def kl_divergence(p_dist, q_dist, base=2):
    return sum(
        p * math.log(max(p, EPS) / max(q, EPS), base)
        for p, q in zip(p_dist, q_dist)
        if p > 0
    )

def mutual_information(joint_xy, base=2):
    # Compute marginals
    px = {}
    py = {}
    for (x, y), pxy in joint_xy.items():
        px[x] = px.get(x, 0.0) + pxy
        py[y] = py.get(y, 0.0) + pxy

    # Compute I(X;Y)
    I = 0.0
    for (x, y), pxy in joint_xy.items():
        if pxy > 0:
            I += pxy * math.log(pxy / (px[x] * py[y] + EPS), base)
    return I

# ===============================
# DEMO: verify cross-entropy inequality
# ===============================
def verify_cross_entropy():
    p = [0.3, 0.7]
    q_same = [0.3, 0.7]
    q_diff = [0.6, 0.4]

    H_p = entropy(p)
    H_pp = cross_entropy(p, q_same)
    H_pq = cross_entropy(p, q_diff)
    D = kl_divergence(p, q_diff)

    print("H(p) =", H_p)
    print("H(p,p) =", H_pp)
    print("H(p,q) =", H_pq)
    print("KL(p||q) =", D)
    print("Check: H(p,q) == H(p) + KL:", H_pq, H_p + D)
    print("Inequality: H(p,q) >= H(p,p) ?", H_pq >= H_pp)

# ===============================
# Mutual Information demo
# ===============================
def demo_mutual_information():
    # Perfect correlation example
    joint = {(0,0): 0.5, (1,1): 0.5}
    I = mutual_information(joint)
    print("Mutual Information (perfect correlation):", I, "bits")

# ===============================
# MAIN
# ===============================
if __name__ == "__main__":
    verify_cross_entropy()
    demo_mutual_information()

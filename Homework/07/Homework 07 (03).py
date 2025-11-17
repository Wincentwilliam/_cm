# information_measures.py
import math
from collections import Counter

EPS = 1e-12  # small value to avoid log(0)

def entropy(p_dist, base=2):
    """Shannon entropy H(p) for discrete distribution p_dist (dict or list)."""
    # p_dist can be dict {symbol:prob} or list of probs
    if isinstance(p_dist, dict):
        probs = list(p_dist.values())
    else:
        probs = list(p_dist)
    H = 0.0
    for p in probs:
        if p > 0:
            H -= p * math.log(p, base)
    return H

def cross_entropy(p_dist, q_dist, base=2):
    """Cross-entropy H(p,q) = - sum_x p(x) log q(x). p and q must align order-wise.
       Accepts dicts with same keys or two lists of same length."""
    if isinstance(p_dist, dict) and isinstance(q_dist, dict):
        keys = p_dist.keys()
        return -sum(p_dist[k] * math.log(max(q_dist.get(k, 0.0), EPS), base) for k in keys)
    else:
        # lists
        return -sum(p * math.log(max(q, EPS), base) for p, q in zip(p_dist, q_dist))

def kl_divergence(p_dist, q_dist, base=2):
    """D_KL(p||q) = sum p * log(p/q)."""
    if isinstance(p_dist, dict) and isinstance(q_dist, dict):
        keys = p_dist.keys()
        return sum(p_dist[k] * math.log(max(p_dist[k], EPS) / max(q_dist.get(k, EPS), EPS), base) for k in keys if p_dist[k] > 0)
    else:
        return sum(p * math.log(max(p, EPS) / max(q, EPS), base) for p, q in zip(p_dist, q_dist) if p > 0)

def mutual_information(joint_xy, base=2):
    """Mutual information I(X;Y) given joint distribution as dict {(x,y): prob}.
       Marginals are computed. joint_xy is a dict mapping (x,y)->p(x,y)."""
    # compute marginals
    px = {}
    py = {}
    for (x, y), pxy in joint_xy.items():
        px[x] = px.get(x, 0.0) + pxy
        py[y] = py.get(y, 0.0) + pxy
    I = 0.0
    for (x, y), pxy in joint_xy.items():
        if pxy <= 0: 
            continue
        I += pxy * math.log(pxy / (px[x] * py[y] + EPS), base)
    return I

if __name__ == "__main__":
    # Example: Bernoulli p = 0.3
    p = 0.3
    p_dist = [p, 1-p]  # [P(1), P(0)]
    q_dist = [0.6, 0.4]  # different model

    H_p = entropy(p_dist)
    H_pq = cross_entropy(p_dist, q_dist)
    D_pq = kl_divergence(p_dist, q_dist)
    print(f"H(p) = {H_p:.6f} bits")
    print(f"H(p,q) = {H_pq:.6f} bits")
    print(f"D_KL(p||q) = {D_pq:.6f} bits")
    print("Check: H(p,q) ?= H(p) + D_KL(p||q) ->", H_pq, H_p + D_pq)

    # Mutual information example: X and Y perfectly correlated
    joint = { (0,0): 0.5, (1,1): 0.5 }
    I = mutual_information(joint)
    print(f"I(X;Y) for perfect correlation = {I:.6f} bits")  # should be H(X)

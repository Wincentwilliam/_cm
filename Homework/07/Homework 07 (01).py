# prob_all_heads.py
from math import log2

def prob_all_heads(n, p=0.5):
    return p ** n

if __name__ == "__main__":
    n = 10000
    p = 0.5
    prob = prob_all_heads(n, p)
    print(f"Probability of {n} heads in a row with p={p}:")
    print(prob)  # this will be 0.0 in float underflow
    # Show in logarithmic form to avoid underflow:
    log2_prob = n * (log2(p))
    print(f"log2(probability) = {log2_prob}")
    print(f"Probability = 2^({log2_prob})")

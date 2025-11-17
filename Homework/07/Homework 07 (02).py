# log_prob.py
import math

def log_prob(n, p=0.5, base=math.e):
    # returns log_base(p^n) = n * log_base(p)
    return n * math.log(p, base)

if __name__ == "__main__":
    n = 10000
    p = 0.5
    ln_val = log_prob(n, p, base=math.e)
    log10_val = log_prob(n, p, base=10)
    log2_val = log_prob(n, p, base=2)
    print(f"ln(0.5^{n}) = {ln_val}")
    print(f"log10(0.5^{n}) = {log10_val}")
    print(f"log2(0.5^{n}) = {log2_val}")
    # show probability from log (if desired)
    # prob = math.exp(ln_val)  # will underflow to 0.0

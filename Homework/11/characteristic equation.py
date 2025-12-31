import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    # 1. Find the roots of the characteristic polynomial
    # np.roots expects coefficients from highest power to lowest
    raw_roots = np.roots(coefficients)
    
    # 2. Handle numerical precision issues (rounding)
    # Roots like 1.000000000004 become 1.0
    # Roots like 1e-15j become 0.0j
    roots = []
    for r in raw_roots:
        real_part = round(r.real, 4)
        imag_part = round(r.imag, 4)
        roots.append(complex(real_part, imag_part))
    
    # 3. Count multiplicities of each root
    root_counts = Counter(roots)
    
    # We use a set to keep track of processed roots (to handle complex pairs together)
    processed_roots = set()
    terms = []
    c_index = 1 # To track constant names C_1, C_2, etc.
    
    # Sort unique roots to keep output consistent (real roots first, then complex)
    unique_roots = sorted(root_counts.keys(), key=lambda x: (abs(x.imag), x.real))

    for root in unique_roots:
        if root in processed_roots:
            continue
            
        multiplicity = root_counts[root]
        
        # CASE 1: Real Roots (imaginary part is 0)
        if abs(root.imag) < 1e-6:
            val = root.real
            for m in range(multiplicity):
                # Format: C_n * x^m * e^(val*x)
                x_term = f"x^{m}" if m > 0 else ""
                term = f"C_{c_index}{x_term}e^({val}x)"
                terms.append(term)
                c_index += 1
            processed_roots.add(root)
            
        # CASE 2: Complex Conjugate Roots (alpha +/- beta*i)
        else:
            alpha = root.real
            beta = abs(root.imag)
            # Find the conjugate root in the list to mark it as processed
            conjugate = complex(alpha, -beta)
            
            for m in range(multiplicity):
                x_term = f"x^{m}" if m > 0 else ""
                # Exponential part (if alpha is 0, e^0x = 1, but we keep it for general format)
                exp_part = f"e^({alpha}x)"
                
                # Cosine term
                terms.append(f"C_{c_index}{x_term}{exp_part}cos({beta}x)")
                c_index += 1
                
                # Sine term
                terms.append(f"C_{c_index}{x_term}{exp_part}sin({beta}x)")
                c_index += 1
                
            processed_roots.add(root)
            processed_roots.add(conjugate)

    # Combine all terms into the final string
    solution = "y(x) = " + " + ".join(terms)
    return solution

# --- Test code (provided in your image) ---
print("--- 實數單根範例 ---")
print(solve_ode_general([1, -3, 2]))

print("\n--- 實數重根範例 ---")
print(solve_ode_general([1, -4, 4]))

print("\n--- 複數共軛根範例 ---")
print(solve_ode_general([1, 0, 4]))

print("\n--- 複數重根範例 ---")
print(solve_ode_general([1, 0, 2, 0, 1]))

print("\n--- 高階重根範例 ---")
print(solve_ode_general([1, -6, 12, -8]))
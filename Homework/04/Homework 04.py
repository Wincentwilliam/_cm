import numpy as np

def cubic_roots(coeffs):
    # Ensure it's cubic
    if len(coeffs) != 4:
        print("Error: This function only handles cubic polynomials (degree 3).")
        return

    # Normalize coefficients so leading term = 1
    c = [ci / coeffs[-1] for ci in coeffs]

    # Companion matrix
    companion = np.zeros((3,3))
    companion[1:, :-1] = np.eye(2)
    companion[0, :] = -np.array(c[:-1])

    # Eigenvalues = roots
    roots = np.linalg.eigvals(companion)

    # Convert NumPy floats to standard Python floats and round
    real_roots = [round(float(r.real), 10) for r in roots if abs(r.imag) < 1e-10]

    # Sort descending
    real_roots.sort(reverse=True)

    # Calculate discriminant Δ = b^2 - 3ac (for cubic)
    a, b, c_, d = c[-1], c[-2], c[-3], c[-4]
    Δ = b**2 - 3*a*c_
    print(f"判別式 Δ = {Δ:.4f}")
    print(f"answer: {tuple(real_roots)}")
    return real_roots

# Example usage
coeffs = [-6, 11, -6, 1]  # x^3 - 6x^2 + 11x - 6
cubic_roots(coeffs)

import cmath

# 1. Forward Transform: dft(f)
def dft(f):
    """
    Performs the Discrete Fourier Transform on a list of values.
    Formula used: F[k] = Σ (f[n] * e^(-i * 2 * pi * k * n / N))
    """
    N = len(f)
    F = [0] * N
    for k in range(N):
        sum_val = complex(0, 0)
        for n in range(N):
            # Calculate the angle for the complex exponential
            angle = -2j * cmath.pi * k * n / N
            sum_val += f[n] * cmath.exp(angle)
        F[k] = sum_val
    return F

# 2. Inverse Transform: idft(F)
def idft(F):
    """
    Performs the Inverse Discrete Fourier Transform.
    Formula used: f[n] = (1/N) * Σ (F[k] * e^(i * 2 * pi * k * n / N))
    Note: While the image shows 1/2π, in discrete signals, 1/N is used for normalization.
    """
    N = len(F)
    f_recovered = [0] * N
    for n in range(N):
        sum_val = complex(0, 0)
        for k in range(N):
            # Calculate the angle (positive for inverse transform)
            angle = 2j * cmath.pi * k * n / N
            sum_val += F[k] * cmath.exp(angle)
        # Normalize by dividing by N
        f_recovered[n] = sum_val / N
    return f_recovered

# 3. Verification: Check if f -> F -> f works
def verify():
    # Define an original sample function f (a simple list of numbers)
    f_original = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Original Function f: {f_original}")

    # Step 1: Forward Transform
    F_omega = dft(f_original)
    print("\nResult after Forward Transform F(ω):")
    for val in F_omega:
        print(f"{val:.4f}")

    # Step 2: Inverse Transform
    f_back = idft(F_omega)
    
    # Extract only the real part for comparison 
    # (Inverse results often have tiny imaginary residuals like 1e-16 due to floating point math)
    f_back_real = [round(val.real, 10) for val in f_back]
    
    print("\nResult after Inverse Transform (Back to f):")
    print(f_back_real)

    # Step 3: Check if they match
    if f_original == f_back_real:
        print("\nVerification: SUCCESS!")
        print("The function was correctly transformed and recovered.")
    else:
        print("\nVerification: FAILED.")

if __name__ == "__main__":
    verify()
# Fourier Transform: Python Implementation Study Notes

This document provides a scratch-built implementation of the Discrete Fourier Transform (DFT) and its Inverse (IDFT) in Python, following the mathematical principles of signal processing.

---

## 1. Mathematical Concept

The formulas in the assignment represent the **Continuous Fourier Transform**. However, in Python, we work with lists of data, so we use the **Discrete** versions:

### Forward Transform (dft)
We convert a signal from the **Time Domain** to the **Frequency Domain**.
- **Logic:** `F[k] = Sum(f[n] * e^(-i * 2 * pi * k * n / N))`

### Inverse Transform (idft)
We convert the frequency data back into the **original signal**.
- **Logic:** `f[n] = (1/N) * Sum(F[k] * e^(i * 2 * pi * k * n / N))`
- *Note: In discrete computing, we use 1/N as the scaling factor to recover the original amplitude.*

---

## 2. Python Code Implementation

This implementation uses the built-in `cmath` library for complex number calculations.

```python
import cmath

def dft(f):
    """
    1. Forward Discrete Fourier Transform
    Inputs: f (list of real or complex numbers)
    Outputs: F (list of frequency components)
    """
    N = len(f)
    F = [0] * N
    for k in range(N):
        sum_val = 0
        for n in range(N):
            # Formula: f(n) * e^(-i * 2 * pi * k * n / N)
            angle = -2j * cmath.pi * k * n / N
            sum_val += f[n] * cmath.exp(angle)
        F[k] = sum_val
    return F

def idft(F):
    """
    2. Inverse Discrete Fourier Transform
    Inputs: F (frequency components)
    Outputs: f (recovered signal)
    """
    N = len(F)
    f_recovered = [0] * N
    for n in range(N):
        sum_val = 0
        for k in range(N):
            # Formula: F(k) * e^(i * 2 * pi * k * n / N)
            angle = 2j * cmath.pi * k * n / N
            sum_val += F[k] * cmath.exp(angle)
        # Apply normalization 1/N
        f_recovered[n] = sum_val / N
    return f_recovered

# 3. Verification Script
if __name__ == "__main__":
    # Define a test function f
    f_original = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Original Signal f:    {f_original}")

    # Forward transform
    F_freq = dft(f_original)
    
    # Inverse transform
    f_recovered = idft(F_freq)
    
    # Clean up results (remove tiny floating point errors)
    f_final = [round(val.real, 10) for val in f_recovered]
    
    print(f"Recovered Signal f:   {f_final}")
    
    # Check if they are the same
    if f_original == f_final:
        print("\nSUCCESS: The recovered function matches the original function!")
    else:
        print("\nFAILURE: Data mismatch.")
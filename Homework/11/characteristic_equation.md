# Engineering Mathematics: ODE Solver Notes

## 1. Problem Definition
We are solving **nth-order linear homogeneous ordinary differential equations (ODEs)** with constant coefficients:
$$a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_1 y' + a_0 y = 0$$

## 2. The Characteristic Equation
To find the solution, we substitute $y = e^{\lambda x}$ into the differential equation, which leads to the **characteristic polynomial**:
$$a_n \lambda^n + a_{n-1} \lambda^{n-1} + \dots + a_1 \lambda + a_0 = 0$$

The roots ($\lambda$) of this equation determine the form of the general solution $y(x)$.

---

## 3. General Solution Cases

### Case 1: Distinct Real Roots
If all roots $\lambda_1, \lambda_2, \dots$ are real and unique:
$$y(x) = C_1 e^{\lambda_1 x} + C_2 e^{\lambda_2 x} + \dots$$

### Case 2: Repeated Real Roots
If a root $\lambda$ repeats $k$ times (multiplicity $k$), we multiply by powers of $x$ to ensure the solutions are linearly independent:
$$y(x) = (C_1 + C_2 x + C_3 x^2 + \dots + C_k x^{k-1}) e^{\lambda x}$$

### Case 3: Complex Conjugate Roots
If roots are complex numbers $\lambda = \alpha \pm \beta i$, we use Euler's formula to convert exponentials into sines and cosines:
$$y(x) = e^{\alpha x} (C_1 \cos(\beta x) + C_2 \sin(\beta x))$$

### Case 4: Repeated Complex Roots
If the complex pair $\alpha \pm \beta i$ repeats $k$ times:
$$y(x) = e^{\alpha x} \sum_{m=0}^{k-1} x^m [C_{2m+1} \cos(\beta x) + C_{2m+2} \sin(\beta x)]$$

---

## 4. Implementation Logic (Python)

The Python function `solve_ode_general(coefficients)` follows these logical steps:

1.  **Root Extraction**: Uses `numpy.roots(coefficients)` to find all numerical solutions for $\lambda$.
2.  **Numerical Cleaning**: 
    *   Due to floating-point precision, a root like $2$ might appear as $2.000000000004$.
    *   The code uses `round(r, 4)` to consolidate these values so the computer recognizes them as the same root.
3.  **Frequency Analysis**: Uses `collections.Counter` to determine the **multiplicity** of each root.
4.  **Term Building**:
    *   **Real Roots**: Generates terms like `C_n * x^m * e^(ax)`.
    *   **Complex Roots**: Detects the imaginary part. It processes the pair ($\alpha + \beta i$ and $\alpha - \beta i$) together to generate both $\cos$ and $\sin$ terms in one pass.
5.  **String Formatting**: Joins all terms into a final readable string `y(x) = ...`.

---

## 5. Test Examples Reference

| Equation Type | Coefficients | Expected Roots |
| :--- | :--- | :--- |
| **Distinct Real** | `[1, -3, 2]` | $\lambda = 1, 2$ |
| **Repeated Real** | `[1, -4, 4]` | $\lambda = 2, 2$ |
| **Complex Conjugate** | `[1, 0, 4]` | $\lambda = 0 \pm 2i$ |
| **Repeated Complex** | `[1, 0, 2, 0, 1]` | $\lambda = \pm i, \pm i$ |
| **High Order Repeated** | `[1, -6, 12, -8]` | $\lambda = 2, 2, 2$ |

---
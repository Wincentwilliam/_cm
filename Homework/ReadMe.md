Homework 7:
Shannon’s Big Picture: How Information Survives Noise

Claude Shannon basically laid down the law for all modern communication — WiFi, 4G, 5G, Bluetooth, satellite, everything.
He created two big ideas that work together like a power duo:

1. Shannon Channel Coding Theorem
“You CAN beat noise, but only if you don’t go too fast.”

Imagine you’re trying to talk to someone during a storm.
There’s noise everywhere, but if you speak clearly and not too fast, they can still understand you.

Shannon says:

Every communication channel has a maximum safe speed for sending information.

If you stay below that limit, you can design coding methods that make errors almost disappear.

If you try to send faster than the limit, errors will happen forever — nothing can save you.

Simple idea:

Stay below the channel’s limit → reliable communication is possible.

2. Shannon–Hartley Theorem
“Here’s how big that limit actually is.”

This theorem explains what controls the maximum safe data speed.

Two things matter:

Bandwidth — how wide the channel is
(wider = more information can pass)

Signal vs Noise — how strong your message is compared to the background noise
(clearer = more data can pass)

Simple idea:

More bandwidth + cleaner signal → higher data capacity.

How They Work Together (The Fusion Explanation)

You can think of it like a highway:

Shannon–Hartley tells you how wide the road is and how clean the traffic is.

Shannon Channel Coding Theorem tells you how safely you can drive without crashing.

So combined together:

First, use Shannon–Hartley to know the channel’s maximum possible data capacity
Then, use Shannon Channel Coding Theorem to send your data reliably as long as you stay under that capacity.

TL;DR Version

Shannon Channel Coding Theorem:
You can communicate reliably over a noisy channel if your data rate is below the channel’s capacity.

Shannon–Hartley Theorem:
The channel’s capacity depends on two things:
bandwidth (how wide the channel is) and signal-to-noise ratio (how strong the signal is compared to the noise).

Together, they explain:

=> How much information you can send,
=> How fast you can send it,
=> And how to make it reliable even when the world is noisy.

Homework 9:
### 1. The Meaning of "Linear" and "Algebra"
In this context, **Linear** refers to a relationship governed by the principles of superposition. A function or map $f$ is linear if it satisfies two specific rules:
1.  **Additivity:** $f(x + y) = f(x) + f(y)$
2.  **Homogeneity (Scaling):** $f(cx) = c \cdot f(x)$

Geometrically, this implies a constant proportional relationship (straight lines or flat planes passing through the origin). It is called **Algebra** because it abstracts these relationships using symbols, variables, and equations to generalize arithmetic operations across different structures.

### 2. Defining "Space" and "Vector Space"
In mathematics, a **space** is simply a set of objects equipped with a specific structure or set of rules. A **Vector Space** is a specific type of space where the objects (vectors) can be added together and multiplied by scalars (numbers) while satisfying specific axioms (like associativity and commutativity).
Crucially, a vector space requires **closure**: adding two vectors or scaling a vector must produce a result that remains within the same space.

### 3. Matrices vs. Vectors
A **vector** is fundamentally a specific instance of a matrix. It can be viewed as a matrix with a single column ($n \times 1$) or a single row ($1 \times n$).
A **matrix**, broadly speaking, is a rectangular array of numbers. While it can store multidimensional data (like an image), in linear algebra, a matrix primarily represents a **linear transformation**—a machine that takes an input vector and transforms it (warps, rotates, or scales it) into a new output vector.

### 4. Geometric Transformations (Translation, Scaling, Rotation)
Matrices serve as the instructions for manipulating geometry.
*   **2D Scaling:** Multiplies $x$ and $y$ coordinates by scaling factors $s_x$ and $s_y$.
    $$
    \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}
    $$
*   **2D Rotation:** Rotates a vector by an angle $\theta$.
    $$
    \begin{bmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}
    $$
*   **3D Translation:** Standard linear multiplication cannot move the origin $(0,0,0)$; therefore, we use **homogeneous coordinates** (adding a 4th dimension) to represent translation in a $4 \times 4$ matrix:
    $$
    \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}
    $$

### 5. The Determinant and Volume
The **determinant** provides a single number that describes how a matrix changes volume.
*   **Geometric Meaning:** The absolute value, $|\det(A)|$, represents the volume of the parallelepiped formed by the matrix's column vectors.
    *   If $\det(A) = 0$: The matrix collapses space (e.g., 3D becomes 2D), and it is **singular** (not invertible).
    *   If $\det(A) < 0$: The transformation reverses orientation (like turning a glove inside out).

**Calculation via Cofactor Expansion (Recursive):**
The standard recursive formula involves breaking the matrix down into smaller "minor" matrices ($M_{ij}$):
$$ \det(A) = \sum (-1)^{i+j} a_{ij} \det(M_{ij}) $$

### 6. Efficient Determinant Calculation
Calculating determinants recursively is slow for large matrices. We use decompositions to speed this up:
*   **I. Using Diagonalization:**
    If a matrix is diagonal, the determinant is simply the product of the diagonal elements ($\det(A) = a \times b \times c$).
    Even if $A$ is not diagonal, if $A = PDP^{-1}$, then $\det(A) = \det(D)$. Thus, the determinant is the product of the **eigenvalues** ($\prod \lambda_i$).
*   **II. Using LU Decomposition:**
    We factor $A$ into Lower ($L$) and Upper ($U$) triangular matrices. Since $L$ usually has $1$s on the diagonal, $\det(L)=1$. Therefore, the determinant is the product of the diagonal elements of $U$:
    $$ \det(A) = \prod (\text{diagonal of } U) $$

### 7. Eigenvalues and Eigenvectors
When a matrix transforms space, most vectors get knocked off their original path.
*   **Eigenvectors ($v$):** The special vectors that *do not change direction* during the transformation.
*   **Eigenvalues ($\lambda$):** The scalar factor by which the eigenvector is stretched or shrunk.
$$ Av = \lambda v $$
**Eigenvalue Decomposition ($A = PDP^{-1}$)** is useful for simplifying matrix powers (system dynamics), analyzing stability in differential equations, and vibration analysis.

### 8. QR Decomposition and Eigenvalue Algorithms
**QR Decomposition** factors a matrix $A$ into:
*   $Q$: An **orthogonal matrix** (pure rotation/reflection).
*   $R$: An **upper triangular matrix**.
$$ A = QR $$

**Finding Eigenvalues via QR Algorithm:**
We can find eigenvalues not by decomposing once, but iteratively. By repeatedly setting $A_{k+1} = R_k Q_k$, the matrix gradually converges to a form where the diagonal elements are the eigenvalues.

### 9. SVD (Singular Value Decomposition)
While Eigendecomposition requires square matrices, **SVD** works for *any* matrix (rectangular or square). It breaks a matrix into three geometric steps:
1.  **Rotation ($V^T$):** Rotate input space.
2.  **Scaling ($\Sigma$):** Stretch along axes (Singular Values).
3.  **Rotation ($U$):** Rotate into output space.
$$ A = U \Sigma V^T $$
**Connection:** The singular values in $\Sigma$ are the square roots of the eigenvalues of $A^T A$.

### 10. SVD and Principal Component Analysis (PCA)
**Principal Component Analysis (PCA)** is a statistical technique used for dimensionality reduction. It finds the "principal directions" (eigenvectors) where data varies the most.
**Relationship:** SVD is the standard computational method used to perform PCA. Instead of calculating the computationally expensive covariance matrix ($C = X^T X$) and finding its eigenvalues, we can simply run SVD on the centered data matrix $X$. The resulting singular values and vectors provide the principal components directly and efficiently.

Homework 10:
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

Homework 11:
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

Midterm Exam:
# Chaos Theory & Data Engineering: Visualizing the Lorenz Attractor

## 1. Project Overview & Attribution
* **Student Name:** 洪偉升
* **Submission Date:** 2025/12/31
* **Course:** Math and coding
* **Professor:** ccckmit (Chen Zhongcheng)

### Source Declaration (As per Requirement #7)
> **Statement of Originality:** This project utilizes AI (Claude/ChatGPT) for high-level mathematical modeling and Python architecture. I have integrated the components, customized the data engineering pipeline (CSV persistence), and documented the theoretical derivation to demonstrate academic understanding.
> 
> **AI Usage:** Used AI to generate the core Lorenz algorithm and documentation structure.
> **Code Origin:** Modified from AI-generated logic to include data persistence and specialized 3D visualization.

---

## 2. Mathematical Theory: The Lorenz Equations
The **Lorenz Attractor** is a mathematical object that demonstrates **Deterministic Chaos**. It was discovered by meteorologist Edward Lorenz while modeling atmospheric convection.

### The Problem: The Butterfly Effect
In a chaotic system, a tiny change in the initial state (e.g., changing $1.0$ to $1.000001$) leads to a massive difference in the long-term path. This is known as "sensitive dependence on initial conditions."

### The Mathematical Formula
The system is defined by three non-linear ordinary differential equations (ODEs):

$$ \frac{dx}{dt} = \sigma(y - x) $$
$$ \frac{dy}{dt} = x(\rho - z) - y $$
$$ \frac{dz}{dt} = xy - \beta z $$

**Parameter Meanings:**
*   $x, y, z$: Represent the physical state of the fluid (convection rate and temperature gradients).
*   $\sigma$ (Prandtl Number): Ratio of momentum to thermal diffusivity.
*   $\rho$ (Rayleigh Number): Heat transfer ratio (Chaos occurs when $\rho \approx 28$).
*   $\beta$: Represents the geometry of the physical space.

---

## 3. Data Engineering & Tracking Workflow
This project does not just plot numbers; it implements a modern **Data Engineering Pipeline**:

1.  **Numerical Integration:** We use the `scipy.integrate.odeint` library to solve the continuous differential equations. Since computers cannot solve calculus "perfectly," we discretize the time into 5,000 tiny intervals.
2.  **Data Persistence (The CSV Layer):** Instead of keeping results in temporary memory (RAM), we use `pandas` to convert the mathematical results into a structured **CSV (Comma Separated Values)** file. 
    *   **Why?** This allows the chaotic path to be tracked and audited. We can open `chaos_tracking_data.csv` in Excel to inspect the specific $(x, y, z)$ coordinates.
3.  **Graphic Reconstruction:** The final visualization reads the data back from the CSV file rather than the math engine, simulating a real-world scenario where data scientists analyze pre-collected data.

---

## 4. Python Implementation

```python
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# --- STEP 1: MATHEMATICAL LOGIC ---
def lorenz_system(current_state, t, sigma, rho, beta):
    x, y, z = current_state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Constants
SIGMA, RHO, BETA = 10.0, 28.0, 8.0/3.0
initial_condition = [1.0, 1.0, 1.0]
time_steps = np.linspace(0, 50, 5000)

# --- STEP 2: NUMERICAL CALCULATION ---
solutions = odeint(lorenz_system, initial_condition, time_steps, args=(SIGMA, RHO, BETA))

# --- STEP 3: DATA ENGINEERING (CSV EXPORT) ---
df = pd.DataFrame(solutions, columns=['X_Coordinate', 'Y_Coordinate', 'Z_Coordinate'])
df['Timestamp'] = time_steps
csv_file = "chaos_tracking_data.csv"
df.to_csv(csv_file, index=False)

# --- STEP 4: GRAPHICAL RECONSTRUCTION ---
data_to_plot = pd.read_csv(csv_file)
fig = plt.figure(figsize=(12, 9), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')
colors = plt.cm.plasma(np.linspace(0, 1, len(data_to_plot)))

for i in range(len(data_to_plot) - 1):
    ax.plot(data_to_plot['X_Coordinate'][i:i+2], 
            data_to_plot['Y_Coordinate'][i:i+2], 
            data_to_plot['Z_Coordinate'][i:i+2], 
            color=colors[i], linewidth=0.8)

ax.set_title("3D Lorenz Attractor: Chaos Theory via Data Engineering", color='white', fontsize=15)
ax.axis('off')
plt.show()

## 5. *Conclusion*
By combining Non-linear Differential Equations with Data Engineering techniques, this project demonstrates how we can capture and visualize the complex geometry of chaos. The resulting "Butterfly" shape is not just a drawing; it is the physical representation of thousands of mathematical calculations tracked, saved to a database (CSV), and reconstructed in 3D space. It proves that even in deterministic systems, complexity and beauty can emerge from simple mathematical rules.
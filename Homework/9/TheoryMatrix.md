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
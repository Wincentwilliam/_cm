import numpy as np

def lu_decompose(A):
    A = A.astype(float)
    n = len(A)
    L = np.eye(n) 
    U = A.copy()
    
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            U[j] -= factor * U[i]
    return L, U

def det_from_lu(A):
    L, U = lu_decompose(A)
    det = np.prod(np.diag(U))  
    return det, L, U

def verify_all(A):
    print("\nMatrix A:")
    print(A)

    detA, L, U = det_from_lu(A)
    print("\nLU Decomposition:")
    print("L =\n", L)
    print("\nU =\n", U)
    print("\nDeterminant(LU) =", detA)
    print("Determinant(numpy) =", np.linalg.det(A))
    print("Reconstruction L U =\n", L @ U)

    print("\nEigen Decomposition:")
    eigvals, eigvecs = np.linalg.eig(A)
    print("Eigenvalues =", eigvals)
    print("\nEigenvectors =\n", eigvecs)
    print("\nReconstruction V Λ V⁻¹ =\n", eigvecs @ np.diag(eigvals) @ np.linalg.inv(eigvecs))

    print("\nSVD Decomposition:")
    U_svd, S_svd, VT_svd = np.linalg.svd(A)
    Sigma = np.zeros_like(A)
    np.fill_diagonal(Sigma, S_svd)
    print("U =\n", U_svd)
    print("\nΣ =\n", Sigma)
    print("\nV^T =\n", VT_svd)
    print("\nReconstruction U Σ Vᵀ =\n", U_svd @ Sigma @ VT_svd)

A = np.array([
    [2,  1,  1],
    [4, -6,  0],
    [-2, 7,  2]
], dtype=float)

verify_all(A)
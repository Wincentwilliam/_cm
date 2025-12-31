import numpy as np

def svd_manual(A):
    # Step 1: compute Aᵀ A
    ATA = A.T @ A
    print("\nAᵀ A =\n", ATA)

    # Step 2: eigen decomposition of Aᵀ A -> gives V and eigenvalues
    eigvals, V = np.linalg.eig(ATA)

    # Sort eigenvalues descending
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    V = V[:, idx]

    print("\nEigenvalues (sorted) =\n", eigvals)
    print("\nV matrix (eigenvectors) =\n", V)

    # Step 3: singular values = sqrt(eigenvalues)
    singular_values = np.sqrt(eigvals)
    print("\nSingular values =\n", singular_values)

    # Build Σ (Sigma)
    Sigma = np.zeros_like(A, dtype=float)
    np.fill_diagonal(Sigma, singular_values)
    print("\nΣ =\n", Sigma)

    # Step 4: compute U = A V Σ^{-1}
    # Create Sigma^{-1}
    Sigma_inv = np.zeros_like(A, dtype=float)
    for i in range(len(singular_values)):
        if singular_values[i] != 0:
            Sigma_inv[i][i] = 1 / singular_values[i]

    U = A @ V @ Sigma_inv
    print("\nU =\n", U)

    # Step 5: verify U Σ V^T = A
    reconstruction = U @ Sigma @ V.T
    print("\nReconstruction U Σ Vᵀ =\n", reconstruction)

    return U, Sigma, V

A = np.array([
    [2,  1,  4],
    [-1, 3,  1],
    [1, -2,  -2]
], dtype=float)

U, Sigma, V = svd_manual(A)
import numpy as np

def PCA(X, k=2):
    # 1. Center
    mean = np.mean(X, axis=0)
    X_centered = X - mean

    # 2. Covariance
    C = np.cov(X_centered, rowvar=False)

    # 3. Eigen decomposition
    vals, vecs = np.linalg.eig(C)

    # 4. Sort
    idx = np.argsort(-vals)
    vals = vals[idx]
    vecs = vecs[:, idx]

    # 5. Principal components
    W = vecs[:, :k]

    # 6. Transform
    X_pca = X_centered @ W

    # 7. Explained variance
    explained_variance = vals[:k]

    # 8. Explained variance ratio
    explained_variance_ratio = explained_variance / np.sum(vals)

    # 9. Reconstruction
    X_reconstructed = X_pca @ W.T + mean

    return {
        "X_pca": X_pca,
        "components": W,
        "eigenvalues": vals,
        "explained_variance": explained_variance,
        "explained_variance_ratio": explained_variance_ratio,
        "X_reconstructed": X_reconstructed
    }

# MATRIX
A = np.array([
    [4,   3,  -5],
    [1,  -4,   2],
    [-3,  2,   4]
], dtype=float)

# RUN PCA
result = PCA(A, k=2)

# PRINT RESULTS
print("X_pca =\n", result["X_pca"])
print("\nComponents (W) =\n", result["components"])
print("\nEigenvalues =\n", result["eigenvalues"])
print("\nExplained Variance =\n", result["explained_variance"])
print("\nExplained Variance Ratio =\n", result["explained_variance_ratio"])
print("\nX_reconstructed =\n", result["X_reconstructed"])
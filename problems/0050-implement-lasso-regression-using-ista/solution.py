import numpy as np

def soft_threshold(w: np.ndarray, threshold: float) -> np.ndarray:
    """Apply soft-thresholding operator element-wise.
    
    S(w, λ) = sign(w) * max(|w| - λ, 0)
    
    Args:
        w: Input array
        threshold: Threshold value λ
    
    Returns:
        Soft-thresholded array where:
        - Values with |w| > λ are shrunk toward zero by λ
        - Values with |w| ≤ λ become exactly zero
    """
    # Your code here
    mod_of_weights_abs = np.abs(w)
    mod_of_weights = mod_of_weights_abs - threshold * np.ones(w.shape)
    mod_of_weights = mod_of_weights.reshape(-1,1)
    mod_of_weights = np.concatenate([mod_of_weights,np.zeros(mod_of_weights.shape)], axis=1)
    mod_of_weights = np.max(mod_of_weights, axis = 1)
    
    return np.sign(w)* mod_of_weights


    pass

def l1_regularization_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    """
    Implement Lasso Regression using ISTA (Iterative Shrinkage-Thresholding Algorithm).
    
    ISTA alternates between:
    1. Gradient step on MSE loss: w_temp = w - lr * gradient_mse
    2. Proximal step (soft-thresholding): w_new = soft_threshold(w_temp, lr * alpha)
    
    Args:
        X: Feature matrix of shape (n_samples, n_features)
        y: Target vector of shape (n_samples,)
        alpha: L1 regularization strength
        learning_rate: Step size for gradient descent
        max_iter: Maximum iterations
        tol: Convergence tolerance on weight change
    
    Returns:
        tuple: (weights, bias)
    
    Note: The bias term is NOT regularized.
    """
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0.0
    for i in range(0,max_iter): 
            # print(X.shape,weights.shape)
            y_pred = X @ weights.reshape(-1,1) + bias
            residual = (y_pred - y.reshape(-1,1))/len(X)
            updates = X.T@ residual

            weights -=learning_rate*updates.reshape(-1)
            bias = bias - learning_rate * np.sum(residual)/len(X)

            weights = soft_threshold(weights,learning_rate*alpha).reshape(-1)

    return (weights,bias)


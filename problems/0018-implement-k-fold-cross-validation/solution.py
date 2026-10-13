import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    n_samples = [i for i in range(0,n_samples)]
    if shuffle :
        np.random.shuffle(n_samples)
    
    list_of_folds = []

    size = len(n_samples) // k 
    for i in range(0, k)  : 
        list_of_folds.append(tuple([n_samples[0:i*size]+n_samples[(i+1)*size:len(n_samples)],n_samples[i*size:(i+1)*size]]))

    return list_of_folds

    # Your code here
    pass
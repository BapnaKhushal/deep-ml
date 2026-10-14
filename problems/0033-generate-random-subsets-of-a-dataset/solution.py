import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    # Your code here
    n_samples,features = X.shape

    size = n_samples if replacements else n_samples // 2 
    list_of_array = []
    for i in range(n_subsets) : 
        indexes = np.random.choice(n_samples,size,replace = replacements)
        list_of_array.append(tuple([X[indexes],y[indexes]]))
    
    return list_of_array
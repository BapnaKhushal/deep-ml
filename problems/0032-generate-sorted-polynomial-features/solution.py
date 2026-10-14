import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    # ✏️  Your code here
    samples, features = X.shape
    list_of_array = []
    for i in range(0,degree+1):
        for combi in combinations_with_replacement(range(features),i):
            column = np.prod(X[:,combi], axis=1) if i >0 else np.ones(samples)
            list_of_array.append(column)
    
    return np.sort(np.column_stack(list_of_array),axis = 1)

    pass
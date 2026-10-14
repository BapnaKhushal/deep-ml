import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    for i in range(0, X.shape[0], batch_size):
        X_batch = X[i:i + batch_size]
        if y is not None:
            yield [X_batch, y[i:i + batch_size]]
        else:
            yield [X_batch]
import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    # Your code here
    if len(y_true) == 0 :
        return 0
    indexes= np.where(y_true !=0)
    y_true = y_true[indexes]
    y_pred = y_pred[indexes]
    return np.sum(y_pred ==y_true)/len(y_true)
    pass

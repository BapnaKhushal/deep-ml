import numpy as np

def divide_on_feature(X, feature_i, threshold):

	array1 = X[np.where(X[:,feature_i] >= threshold)]
	array2 = X[np.where(X[:,feature_i] < threshold)]
	# Your code here
	# print(array1,array2)
	return [array1,array2]
import numpy as np
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	predicted = np.array(predicted)
	actual = np.array(actual)
	TP = np.sum((predicted ==1) & (actual == 1)) 
	FP = np.sum((predicted == 1) & (actual == 0) )
	TN = np.sum((predicted == 0) & (actual == 0))
	FN = np.sum((actual == 1) & (predicted == 0))

	confusion_matrix = np.array([[TP,FN],[FP,TN]])
	accuracy = (TP+TN)/(TP+TN+FP+FN)
	precision = TP/(TP+FP)
	recall = TP/(TP+FN)
	f1 = 2*precision*recall/(precision + recall)
	specificity = TN/(TN+FP)
	negativePredictive = TN/(TN+FN)
	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)

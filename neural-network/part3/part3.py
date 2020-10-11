import numpy as np

inputs = [3.2, 2.1, 8.1, 4.6]

weights = [[1.1, 2.4, 2.7, -2.4],
		   [4.6, 2.5, 7.8, 1.3],
		   [5.1, 4.0, -2.1, 1.1]]

biases = [9.7, 3.4, 6.7]

outputs = np.dot(weights, inputs) + biases
print(outputs)

import numpy as np

inputs = [[1.2, 2.1, 2.9, 2.6],
		  [2.0, 5.0, -1.0, 2.0],
		  [-1.5, 2.7, 3.3, -0.8]]

weights = [[1.1, 2.4, 2.7, -2.4],
		   [4.6, 2.5, 7.8, 1.3],
		   [5.1, 4.0, -2.1, 1.1]]

biases = [9.7, 3.4, 6.7]

weights2 = [[0.1, 0.14, 2.7],
		   [-1.2, 0.8, 1.8],
		   [1.1, 2.1, -2.1,]]

biases2 = [1.7, 2.2, 0.4]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

print(layer2_outputs)

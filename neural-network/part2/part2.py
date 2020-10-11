inputs = [3.2, 2.1, 8.1, 4.6]

weights = [[1.1, 2.4, 2.7, -2.4],
		   [4.6, 2.5, 7.8, 1.3],
		   [5.1, 4.0, -2.1, 1.1]]

biases = [9.7, 3.4, 6.7]

outputs = [ inputs[0] * weights[i][0] + inputs[1] * weights[i][1] + inputs[2] * weights[i][2] + inputs[3] * weights[i][3] + biases[i] for i in range(3) ]
print(outputs)

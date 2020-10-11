import numpy as np

np.random.seed(14)

X = [[1.2, 2.1, 2.9, 2.6],
	 [2.0, 5.0, -1.0, 2.0],
	 [-1.5, 2.7, 3.3, -0.8]]

class Layer_dense():

	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.25 * np.random.rand(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))

	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:

	def forward(self, input):
		self.output = np.max(0, input)


layer1 = Layer_dense(4,5)
layer2 = Layer_dense(5,2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)
import numpy as np
class NeuralNetwork:

	class DenseLayer:

		def __init__(self, n_neurons, n_inputs):
			self.weights = np.random.uniform(-1, 1, (n_inputs, n_neurons))
			self.biases = np.zeros((1, n_neurons))

		def forward(self, inputs):
			self.output =  np.dot(inputs, self.weights) + self.biases
			self.output = self.ReLU(self.output)

		def backward(self, inputs):
			pass

		def cost(self, inputs):
			pass

		def ReLU(self, inputs):
			return np.maximum(0, inputs)


#     				   structure = [3,4,4,2]
	def __init__(self, structure, batch):
		# creating layers 
		self.layers = [ self.DenseLayer(structure[i], structure[i-1]) for i in range(1, len(structure))]
		self.batch = batch

	def train(self, X, Y, valid_x, valid_y, batch_size):
		pass

	def predict(self, X):
		pass

def create_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)  # radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y 

X, y = create_data(100, 3)   

NN = NeuralNetwork([2,6,2], 6)


NN.layers[0].forward(X)
print(NN.layers[0].output)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


np.random.seed(14)

df = pd.read_csv('/home/lato/Desktop/statistic/data/iris-flower/IRIS.csv')
df = df.sample(frac=1)
df = df.iloc[:5, :]

# multiplied by 1.1 to give maximum value 10 percent gap incase of bigger value
X = df.iloc[:, :-1] / (np.max(df.iloc[:, :-1]) * 1.1)

OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
Y = pd.DataFrame(OH_encoder.fit_transform(df.iloc[:, -1].values.reshape(-1, 1)))

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=14)


class NeuralNetwork:

    class DenseLayer:

        def __init__(self, n_neurons, n_inputs):
            self.weights = np.random.uniform(-1, 1, (n_inputs, n_neurons))
            self.biases = np.zeros((1, n_neurons))

        def forward(self, inputs):
            self.output = np.dot(inputs, self.weights) + self.biases
            self.output = self.ReLU(self.output)

        def predict(self, inputs):
            self.probalities = self.softmax(inputs)
            empty_array = np.zeros((self.probalities.shape))

            for i in range(len(empty_array[0])):
            	print(len(self.probalities[0]))
                # arg_max = np.argmax(self.probalities[i])
                # empty_array[i, arg_max] = 1

            self.output = empty_array

        def cost(self, real_output):
            self.cost = np.sum(np.sqrt(self.output - real_output), axis=0)

        def backward(self, inputs):
            pass

        def cost(self, inputs):
            pass

        def ReLU(self, inputs):
            return np.maximum(0, inputs)

        def softmax(self, inputs):
            exp = np.exp(inputs)
            # print(inputs)
            return exp / np.sum(exp, axis=1).reshape(exp.shape[0], -1)

    def __init__(self, structure):
    	# self.input_layer = self.DenseLayer()
        self.hidden_layers = [self.DenseLayer(structure[i], structure[i-1]) for i in range(1, len(structure) - 1)]
        self.output_layer = self.DenseLayer(structure[-1], structure[-2])

    def train(self, X_train, Y_train, valid_x, valid_y, batch_size, epochs=1):

        X, Y = X_train.reshape(batch_size, -1, X_train.shape[1]), Y_train.reshape(batch_size, -1, Y_train.shape[1])

        for epoch in range(epochs):

            for batch in range(X.shape[0]):
                output = []

                for i in range(len(self.hidden_layers) - 1):

                    if i == 0:
                        self.hidden_layers[i].forward(X[batch])
                        output = self.hidden_layers[i].output
                    else:
                        self.hidden_layers[i].forward(output)
                        output = self.hidden_layers[i].output

                # output = self.hidden_layers[-1].forward(output)
                output = self.output_layer.predict(output)

    def predict(self, X):
        pass


NN = NeuralNetwork([4, 6, 5, 3])

NN.train(X_train.values, y_train.values, X_test.values, y_test.values, 2)

# NN.layers[0].forward(X.iloc[:5,:])
# print(NN.layers[0].output)
# print()

# print(np.sqrt(NN.layers[0].output - y))
# print(y)

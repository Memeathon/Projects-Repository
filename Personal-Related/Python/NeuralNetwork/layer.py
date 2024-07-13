import numpy as np 

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

activations = {
    'sigmoid': sigmoid,
    'tanh': tanh,
    'relu': relu,
    'leakyrelu': leaky_relu,
    'softmax': softmax,
}

# Base class
class Layer:
    def __init__(self, weights, biases, activation):
        self.inputs = None
        self.output = None

        self.weights = weights
        self.biases = biases
        self.activation = activation

    # computes the output Y of a layer for a given input X
    def forward_propagation(self, inputs):
        self.inputs = inputs
        weightedSum = 0
        Sum = 0
        for inp in inputs:
            i = inputs.index(inp)
            Sum += inp * self.weights[i] + self.biases[i]
            Sum = activations[self.activation](Sum) if self.activation else 0
            weightedSum += Sum
        return weightedSum
        

    # computes dE/dX for a given dE/dY (and update parameters if any)
    def backward_propagation(self, output_error, learning_rate):
        raise NotImplementedError


Net = Layer([0.1], [-1], 'tanh')
print(Net.forward_propagation([-10]))
class SimpleNeuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        
    def activate(self, inputs):
        return sum(w * i for w, i in zip(self.weights, inputs)) +   self.bias

# Create a neuron with weights and bias
weights = [0.2, 0.3, 0.5]
bias = 0.1
neuron = SimpleNeuron(weights, bias)

# Create some input values
inputs = [1.0, 2.0, 3.0]

# Activate the neuron with the input values
output = neuron.activate(inputs)

print("Output:", output)
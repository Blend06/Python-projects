import numpy as np

class Neuron:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize the weights and biases for the first layer
        # W1 is a matrix of shape (hidden_size, input_size) with random values between 0 and 1
        self.W1 = np.random.rand(hidden_size, input_size) * 0.01
        # b1 is a vector of shape (hidden_size, 1) with all zeros
        self.b1 = np.zeros((hidden_size, 1))
        
        # Initialize the weights and biases for the second layer
        # W2 is a matrix of shape (output_size, hidden_size) with random values between 0 and 1
        self.W2 = np.random.rand(output_size, hidden_size) * 0.01
        # b2 is a vector of shape (output_size, 1) with all zeros
        self.b2 = np.zeros((output_size, 1))
        
    def forward(self, x):
        # Calculate the output of the first layer
        # Z1 is the dot product of W1 and x, plus the bias b1
        self.Z1 = np.dot(self.W1, x) + self.b1
        # A1 is the activation of Z1 using the tanh function
        self.A1 = np.tanh(self.Z1)
        
        # Calculate the output of the second layer
        # Z2 is the dot product of W2 and A1, plus the bias b2
        self.Z2 = np.dot(self.W2, self.A1) + self.b2
        # A2 is the activation of Z2 using the sigmoid function
        self.A2 = self.sigmoid(self.Z2)
        # Return the output of the second layer
        return self.A2
    
    def sigmoid(self, Z):
        # Calculate the sigmoid of Z
        return 1 / (1 + np.exp(-Z))
    
    def train(self, X, Y, iterations, learning_rate):
        for i in range(iterations):
            A2 = self.forward(X)
            cost = self.compute_cost(A2, Y)
            dW1, db1, dW2, db2 = self.backward(X, Y, A2)
            self.W1 -= learning_rate * dW1
            self.b1 -= learning_rate * db1
            self.W2 -= learning_rate * dW2
            self.b2 -= learning_rate * db2
            if i % 100 == 0:
                print(f"Iteration {i}, Cost: {cost}")
    
    def compute_cost(self, A2, Y):
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A2) + (1 - Y) * np.log(1 - A2)) / m
        return cost
    
    def preprocess_data(self, X, Y):
        X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
        Y_encoded = np.eye(np.max(Y) + 1)[Y].T
        return X, Y_encoded

# Example usage
X_raw = np.random.randint(10, 100, size=(100, 1))
Y_raw = np.random.randint(0, 3, 100)

neuron = Neuron(1, 10, 3)  
X_processed, Y_processed = neuron.preprocess_data(X_raw, Y_raw) 
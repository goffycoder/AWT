import random
import numpy as np

class Perceptron:
    def __init__(self, num_inputs, learning_rate):
        self.learning_rate = learning_rate
        self.weights = np.random.rand(num_inputs + 1)

    def compute_net(self, inputs):
        net = np.dot(inputs, self.weights[:-1]) + self.weights[-1]
        return net

    def step_function(self, net):
        return 1 if net >= 0 else 0

    def train(self, inputs, targets, epochs=1000):
        for _ in range(epochs):
            for i in range(len(inputs)):
                net = self.compute_net(inputs[i])
                output = self.step_function(net)
                if output != targets[i]:
                    error = targets[i] - output
                    self.weights[:-1] += self.learning_rate * error * inputs[i]
                    self.weights[-1] += self.learning_rate * error

    def get_weights(self):
        return self.weights

if __name__ == "__main__":
    num_inputs = 2
    learning_rate = 0.1
    perceptron = Perceptron(num_inputs, learning_rate)

    training_data = np.array([
        [0.25, 0.353],
        [0.25, 0.471],
        [0.5, 0.353],
        [0.5, 0.647],
        [0.75, 0.705],
        [0.75, 0.882],
        [1, 0.705],
        [1, 1],
        [0, 0],
        [0, 1],
        [1, 0]
    ])

    # Corrected target outputs based on the pattern described
    target_outputs = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

    perceptron.train(training_data, target_outputs)

    trained_weights = perceptron.get_weights()

    print("Trained weights:")
    for i, weight in enumerate(trained_weights):
        print(f"Weight {i}: {weight}")

    # Print predicted outputs for each input pattern after training
    print("Predicted outputs:")
    for i in range(len(training_data)):
        net = np.dot(training_data[i], trained_weights[:-1]) + trained_weights[-1]
        predicted_output = perceptron.step_function(net)
        print(f"Input: {training_data[i]}, Predicted Output: {predicted_output}")

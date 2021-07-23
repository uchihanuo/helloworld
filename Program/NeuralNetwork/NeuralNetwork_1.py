#! python3
# -- coding: utf-8 --


import numpy as np
import random
from scipy.special import expit
from scipy.special import logit
from scipy.ndimage.interpolation import rotate
import matplotlib.pyplot as plt
# import logging
# logging.disable(logging.CRITICAL)
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug("Start of program.")


class NEURALNETWORK:
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, output, hidden layers
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # set the learning rate
        self.lr = learningrate
        # link weight matrices, wih and who
        # weight inside the arrays are w_i_j, where link is from node i to node j in the next layer
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # activation function is the sigmoid function
        self.activation_function = lambda x: expit(x)
        self.inverse_activation_function = lambda x: logit(x)
        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        # convert targets list to 2d array
        targets = np.array(targets_list, ndmin=2).T
        # calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        # calculate signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final outputs layer
        final_inputs = np.dot(self.who, hidden_outputs)
        # calculate signals emerging from final outputs layer
        final_output = self.activation_function(final_inputs)

        # calculate output errors
        output_errors = targets - final_output
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = np.dot(self.who.T, output_errors)
        # update the weights for the links between the hidden and outputs layers
        self.who += self.lr * np.dot((output_errors * final_output * (1 - final_output)), hidden_outputs.T)
        # update the weights for the links between the inputs and hiddens layers
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1 - hidden_outputs)), inputs.T)
        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        # calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        # calculate signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final outputs layer
        final_inputs = np.dot(self.who, hidden_outputs)
        # calculate signals emerging from final outputs layer
        final_outputs = self.activation_function(final_inputs)
        return final_outputs

    # backquery the neural network
    def backquery(self, targets_list):
        # transpose the targets list to a vertical array
        final_outputs = np.array(targets_list, ndmin=2).T
        # calculate the signal into the final output layer
        final_inputs = self.inverse_activation_function(final_outputs)

        # calculate the signal out of the hidden layer
        hidden_outputs = np.dot(self.who.T, final_inputs)
        # scale them back to 0.01 to 0.99
        hidden_outputs -= np.min(hidden_outputs)
        hidden_outputs /= np.max(hidden_outputs)
        hidden_outputs *= 0.98
        hidden_outputs += 0.01
        # calculate the signal into the hidden layer
        hidden_inputs = self.inverse_activation_function(hidden_outputs)
        # calculate the signal out of the input layer
        inputs = np.dot(self.wih.T, hidden_inputs)
        # scale them back to 0.01 to 0.99
        inputs -= np.min(inputs)
        inputs /= np.max(inputs)
        inputs *= 0.98
        inputs += 0.01
        # inputs = (inputs - 0.01) / 0.99 * 255
        return inputs


# number of input, hidden and output nodes, and rate of learning
input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.1
learning_cyc = 7
mini_batch = 6000  # max: 60000
# create instance of neural network
n = NEURALNETWORK(input_nodes, hidden_nodes, output_nodes, learning_rate)

# load the mnist training data CSV file into a list
with open('.\\mnist_dataset\\mnist_train.csv', 'r') as training_data_file:
    training_data_list = training_data_file.readlines()

# train the neural network
# go through all records in the training data set
for i in range(1, learning_cyc):
    print('Training... the %s cycle.' % i)
    for record in random.sample(training_data_list, mini_batch):
        # split the record by the ',' commas
        training_values = record.replace('\n', '')
        training_values = training_values.split(',')
        # scale and shift the inputs
        training_inputs = (np.asfarray(training_values[1:]) / 255 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
        training_targets = np.zeros(output_nodes) + 0.01
        # training_values[0] is the target label for this record
        training_targets[int(training_values[0])] = 0.99
        n.train(training_inputs, training_targets)
        # add rotated training values
        training_inputs_plus10 = rotate(training_inputs.reshape((28, 28)), 10, cval=0.01, reshape=False)
        n.train(training_inputs_plus10.reshape(784), training_targets)
        training_inputs_minus10 = rotate(training_inputs.reshape((28, 28)), -10, cval=0.01, reshape=False)
        n.train(training_inputs_minus10.reshape(784), training_targets)

# test the neural net work
with open('.\\mnist_dataset\\mnist_test.csv', 'r') as querying_data_file:
    querying_data_list = querying_data_file.readlines()
scorecard = []
for record in querying_data_list:
    querying_values = record.replace('\n', '')
    querying_values = querying_values.split(',')
    querying_inputs = (np.asfarray(querying_values[1:]) / 255 * 0.99) + 0.01

    querying_outputs = n.query(querying_inputs)
    if int(querying_values[0]) == querying_outputs.argmax():
        print('The output number is %s, same as target.' % querying_values[0])
        scorecard.append(1)
    else:
        print('The target number is %s, but the output number is %s.' % (querying_values[0], querying_outputs.argmax()))
        scorecard.append(0)
print('The score of this neural network is %.2f.' % (sum(scorecard) / len(scorecard) * 100))

# back to query after training
for i in range(output_nodes):
    target = np.zeros(output_nodes) + 0.01
    target[i] = 0.99
    image_data = n.backquery(target)
    plt.subplot(2, 5, i + 1)  # row:2, column:5
    plt.imshow(image_data.reshape((28, 28)), cmap='Greys', interpolation='None')
# plt.show()

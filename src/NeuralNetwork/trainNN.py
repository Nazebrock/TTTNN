from fann2 import libfann

connection_rate = 1
learning_rate = 0.7
num_input = 9
num_neurons_hidden = 9
num_output = 1

desired_error = 0.0001
max_iterations = 100000
iterations_between_reports = 1000


nn = libfann.neural_net()
nn.create_sparse_array(connection_rate, (num_input, num_neurons_hidden, num_output))
nn.set_learning_rate(learning_rate)
nn.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)

nn.train_on_file("train.data", max_iterations, iterations_between_reports, desired_error)

nn.save("nn.net")

from fann2 import libfann

input = [0,0,0,0,0,0,0,0,0]

nn = libfann.neural_net()

nn.create_from_file("nn.net")

calc = nn.run(input)
print(str(input)+" => "+str(calc))

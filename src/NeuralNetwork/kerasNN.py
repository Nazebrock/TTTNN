from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import theano
import pickle

#Enable multi core
theano.config.openmp = True

#Global NeuralNetwork Settings
batch = 170000 

#Format data to train the NN
def get_fit_arrays(b, filename):
    f = open(filename, "r")
    f.readline()
    x = []
    y = []
    
    for i in range(b*2):
        line = f.readline()

        if i%2 == 0:
            line_array = line.split(' ')
            line_array.pop(len(line_array)-1)
            for a in line_array:
                x.append(int(a))
        else:
            y.append(int(line))

    x = np.array(x).reshape(b, 9)
    y = np.array(y).reshape(b, 1)

    return [x,y]

#Build Neural Network model
model = Sequential()

model.add(Dense(9, input_dim=9))
model.add(Activation('sigmoid'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
model.summary()

#Train Neural Network
print("\nTRAINING\nSample size : "+str(batch))
data = get_fit_arrays(batch, "train.data")
train = model.fit(data[0], data[1], nb_epoch=100, verbose=0, batch_size=batch)

#Test Neural Network
print("\nTESTING")
data = get_fit_arrays(batch, "test.data")
loss_and_metrics = model.evaluate(data[0], data[1], batch_size=batch)
print("Result : Loss="+str(loss_and_metrics[0])+" metrics="+str(loss_and_metrics[1]))

#Export Neural Network
config = open("config.pkl", "w")
print(model.get_config())
pickle.dump(model.get_config(), config, pickle.HIGHEST_PROTOCOL)
config.close()
model.save_weights("wheights.h5")


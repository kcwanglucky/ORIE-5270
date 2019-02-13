# Problem 3
# Reference: https://adventuresinmachinelearning.com/keras-tutorial-cnn-11-lines/
# https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
#import tensorflow as tf
import keras
#import numpy as np
import random
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, Dropout
from keras.datasets import cifar10
from keras.layers import Dense, Flatten
from keras.utils import to_categorical
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=(32, 32, 3)))

## ----- For Problem 3-3, UNCOMMNET the Following Line then run ----- 
#model.add(BatchNormalization())

## ----- For Problem 3-4, UNCOMMNET the Following Line then run ----- 
#model.add(Dropout(0.15))

model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

print(model.summary())

# Question 3-2
#np.random.seed(1)
id1 = random.sample(range(1,len(x_train)), int(len(x_train) * 0.1))
id2 = random.sample(range(1,len(x_test)), int(len(x_test) * 0.1))

#modify the size of data
x_train = x_train[id1]
y_train = y_train[id1]
x_test = x_test[id2]
y_test = y_test[id2]

# to_categorical() convert class vectors to binary class matrices
history = model.fit(x_train, to_categorical(y_train), 
	batch_size=128, epochs=10, verbose=1, 
	validation_data=(x_test, to_categorical(y_test)), validation_split=0.33)

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig('p3_2.png')
plt.show()


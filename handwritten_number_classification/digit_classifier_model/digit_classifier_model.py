import numpy as np # working with arrays
import matplotlib.pyplot as plt # visulisation of digits
import tensorflow as tf # machine learning package

# load existing dataset from the tensorflow package and divide into testing and training data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(f'Training samples {len(x_train):,}')
print(f'Test samples {len(x_test):,}')

# create neural network model
model = tf.keras.Sequential()

model.add(tf.keras.layers.Flatten(input_shape=(28,28,1)))
model.add(tf.keras.layers.Dense(300, activation='relu'))  
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# compile all layers
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(0.0003),
              metrics=['accuracy'])

# check the model structure and layers
model.summary()

# train the model
model.fit(x_train, y_train, batch_size=32, epochs=20)

# get information about perfomance of model
model.evaluate(x_test, y_test)

# save and serialize your model to be used later in streamlit webapp
model.save('handwritten_number_classification/digit_classifier_model/digit_classifier.model')

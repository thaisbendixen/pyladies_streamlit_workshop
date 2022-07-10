import numpy as np # working with arrays
import matplotlib.pyplot as plt # visulisation of digits
import tensorflow as tf # machine learning package

# load existing dataset from the tensorflow package
# we could use our own but here we are using an existin one
# x represents te hand drawn image file while y is the label 
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(f'Training samples {len(x_train):,}')
print(f'Test samples {len(x_test):,}')

# visualize the data here
def show(idx):
    print(f"The label for training image {idx} is {y_train[idx]}")
    plt.imshow(x_train[idx])
    plt.show()

# create neural network model
model = tf.keras.Sequential()

# turns grid into one line
model.add(tf.keras.layers.Flatten(input_shape=(28,28,1)))
model.add(tf.keras.layers.Dense(300, activation='relu'))  # rectify linear unit
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dropout(0.3))
# this is the output layer, which has 10 unit, which represent individual digits: 0, 1, 2, ... 9
# softmax make sure all neuron values add up to 1, which reprsents the confidence or how likely it is the drawn number is that digit.
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# combines all layers
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(0.0003),
              metrics=['accuracy'])

# shows the model structure including layers and output shape
model.summary()

# here is where we train the model
# epoch how many iterations
model.fit(x_train, y_train, batch_size=32, epochs=20)

# calculate accuracy and 
model.evaluate(x_test, y_test)

# the SavedModel format is another way to serialize models. Models saved in this format can be restored using 
# tf.keras.models.load_model
model.save('handwritten_number_classification/digit_classifier_model/digit_classifier.model')

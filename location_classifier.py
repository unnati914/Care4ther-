import os
import cv2
import numpy as np
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten,Dropout
from keras.layers import Conv2D, MaxPooling2D,ZeroPadding2D
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img


num_classes = 3
batch_size = 128
epochs = 10

def load_img_data(img_path):
	image = cv2.imread(img_path)
	x = cv2.resize(image, (128, 128))
	x = np.expand_dims(x,axis=0)
	return np.array(x);

def load_data(dir):
	X = []
	Y = []
	count = 0
	for filename in os.listdir(dir):
		
		for files in os.listdir(dir+"/"+filename):

			img = load_img_data(dir+"/"+filename+"/"+files)
			X.append(img)
			Y.append(count)
		count += 1 
	return np.array(X),np.array(Y)
train_dir1 = "/home/ritwik/Desktop/minor/car-damage-dataset/data2a/training"
test_dir1 = "/home/ritwik/Desktop/minor/car-damage-dataset/data2a/validation"


x_train,y_train = load_data(train_dir1)
x_test,y_test = load_data(test_dir1)

x_train = x_train.reshape(x_train.shape[0],128,128,3)
x_test = x_test.reshape(x_test.shape[0],128,128,3)
x_train = x_train.astype('float64')
x_test = x_test.astype('float64')
x_train /= 255
x_test /=255



y_train = keras.utils.to_categorical(y_train,num_classes)
y_test = keras.utils.to_categorical(y_test,num_classes)



model= Sequential()


model.add(Conv2D(16, (3, 3),input_shape=(128,128,3)))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Conv2D(16, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(128,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(512))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(3))

model.add(Activation('softmax'))

gen = ImageDataGenerator()
train_generator = gen.flow(x_train, y_train, batch_size=batch_size)
model.compile(loss='categorical_crossentropy'
  , optimizer=keras.optimizers.Adam()
 , metrics=['accuracy']
)

model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs,
	validation_data=(x_test, y_test)
)

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', 100*score[1])


print(model.summary())

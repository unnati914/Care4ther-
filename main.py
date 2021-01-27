'''
import the required libraries 
for image processing ,building the model
and for plotting the graphs
'''
import os
import glob
import keras
import random
import sklearn
import skimage
import numpy as np
import matplotlib as plt
from keras.layers import LSTM
from skimage import transform
from keras.models import Model 
from sklearn.model_selection import train_test_split 
from keras.layers import Input,Dense,TimeDistributed
from keras.preprocessing.image import ImageDataGenerator,array_to_img,img_to_array,load_img

'''
initialisation of batch_size,num_classes and epochs
'''
batch_size = 15
num_classes = 2
epochs = 40

#size of each extacted frame
row_hidden = 128
col_hidden = 128


frame , row, col =(99,144,256)

'''
Loading all the Positive and negative according to the desired 
file path and the load_set preprocess the data in which each frame
is extracted to a paricular size of (144,256)
'''

def load_set(img_path):
  img = load_img(img_path)
  tmp = skimage.color.rgb2gray(np.array(img))
  tmp = transform.resize(tmp, (144, 256))
return tmp

'''
Loading all the Positive and negative according to the desired 
file path and the load_set preprocess the data in which each frame
is extracted to a paricular size of (144,256) and is horizontally filpped
'''

def horizontal_flip(img_path):
  img = load_img(img_path)
  tmp = skimage.color.rgb2gray(np.array(img))
  tmp = skimage.transform.resize(tmp, (144, 256))
  tmp = np.array(tmp)
  tmp = np.flip(tmp, axis = 1)
return tmp


'''
Loading all the Positive and negative files assigned to varaiable
neg and pos respectively
All files contains both the files paths
'''
pos = glob.glob( '99frames/*.mp4')
neg = glob.glob( 'negative/*.mp4')
all_files = np.concatenate((pos, neg[0:len(pos)]))

#print(len(neg),len(pos))
#print(all_files) 


'''
label matrix is used to make one hot encoding ie [0 1] for
positve data and [1 0] for negative data
'''


def label_matrivalues):

  n_values = np.mavalues) + 1 
return np.eye(n_values)[values] 

labels = np.concatenate(([1]*len(pos), [0]*len(neg[0:len(pos)]))) 
labels = label_matrilabels) 
#print(len(labels)) 


def load_data1(path):

  x = []
  for files in os.listdir(path):

  frames = []
  img_path = path+"/"+files
  if files !=("frame99.jpg"):
    img = load_set(img_path)
  x.append(img)
return x



def load_data3(path):
  count = 0
  x = []
  for files in os.listdir(path):
    frames = []
    img_path = path+"/"+files
    if count < 99:
      count = count + 1
      img = load_set(img_path)
  x.append(img)
return x


def load_data2(path): 
  x = []

for files in os.listdir(path):

frames = []
img_path = path+"/"+files
if files !=("frame99.jpg") :

img = horizontal_flip(img_path)
x.append(img)
return x



def load_data4(path): 
x = []
count =0
for files in os.listdir(path):

frames = []
img_path = path+"/"+files
if count < 99 :
count = count +1
img = horizontal_flip(img_path)
x.append(img)
return x 

'''
this function used to make dataset depending upon file name
'''
def make_dataset(rand):
seq1 = np.zeros((len(rand), 99, 144, 256)) 
for i,fi in enumerate(rand): 
print (i, fi)

if fi[9:11] == '00' :
t = load_data1(fi)
elif fi[9:13] == 'MVIH':
t = load_data3(fi)
elif fi[9:13] == 'MVI_': 
t = load_data4(fi) 
elif fi[9:11]=='11' :
t = load_data2(fi) 

seq1[i] = t 

return seq1

'''
make the x_test,x_train and validation data in ration of 
(60% 20% 20%)
'''

x_train, x_t1, y_train, y_t1 = train_test_split(all_files, labels, test_size=0.40, random_state=0) 
x_train = np.array(x_train); y_train = np.array(y_train) 

x_testA = np.array(x_t1[int(len(x_t1)/2):]); y_testA = np.array(y_t1[int(len(y_t1)/2):]) 
x_testA = make_dataset(x_testA)

### valid set for model
x_testB = np.array(x_t1[:int(len(x_t1)/2)]); y_testB = np.array(y_t1[:int(len(y_t1)/2)]) 
x_testB = make_dataset(x_testB)


'''
making the pipeline using keras
using auto encoders(HRRN and LSTM)
'''



x =Input(shape=(frame, row, col))
encoded_rows = TimeDistributed(LSTM(row_hidden))(x) 
encoded_columns =LSTM(col_hidden)(encoded_rows)

prediction = Dense(num_classes, activation='softmax')(encoded_columns)

model = Model(x, prediction)

model.compile(loss='categorical_crossentropy', 
optimizer='NAdam', 
metrics=['accuracy']) 
model.summary()

i=0; filepath='HRNN_pretrained_model.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

np.random.seed(18247)

'''
training on dataset as well as validation
'''

for i in range(0, epochs): 
c = list(zip(x_train, y_train)) 
random.shuffle(c) 
x_shuff, y_shuff = zip(*c) 
x_shuff = np.array(x_shuff); y_shuff=np.array(y_shuff) 

x_batch = [x_shuff[i:i + batch_size] for i in range(0, len(x_shuff), batch_size)] 
y_batch = [y_shuff[i:i + batch_size] for i in range(0, len(x_shuff), batch_size)] 

for j,xb in enumerate(x_batch): 
xx = make_dataset(xb) 
yy = y_batch[j] 

model.fit(xx, yy, 
batch_size=len(xx), 
epochs=3, 
validation_data=(x_testB, y_testB), 
callbacks=callbacks_list
) 

loss = model.history['loss']
val_loss = model.history['val_loss']
epochs = range(epochs)
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

'''
evaluating model on test dataset
'''
scores = model.evaluate(x_testA, y_testA, verbose=0) 
print('Test loss:', scores[0]) 
print('Test accuracy:', scores[1])

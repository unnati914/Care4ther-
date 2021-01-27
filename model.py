import keras
from keras.models import Model 
from keras.layers import Input,Dense,TimeDistributed
from keras.layers import LSTM





import glob
import numpy as np




img_filepath = "/home/ritwik/Desktop/MINI PROJECT/"
pos = glob.glob(img_filepath + '99frames/*.mp4')
neg = glob.glob(img_filepath + 'negative/*.mp4')
all_files =  np.concatenate((pos, neg))
print(len(neg),len(pos))
print(all_files)       


def label_matrix(values):
    
    n_values = np.max(values) + 1    
    return np.eye(n_values)[values] 

labels = np.concatenate(([1]*len(pos), [0]*len(neg[0:len(pos)])))  
labels = label_matrix(labels)    
print(len(labels))      










batch_size = 15
num_classes = 2
epochs = 30

row_hidden = 128
col_hidden = 128


frame , row, col =(99,144,256)

x =Input(shape=(frame, row, col))
encoded_rows = TimeDistributed(LSTM(row_hidden))(x) 
encoded_columns =LSTM(col_hidden)(encoded_rows)

prediction = Dense(num_classes, activation='softmax')(encoded_columns)

model = Model(x, prediction)

model.compile(loss='categorical_crossentropy', 
				optimizer='NAdam',               
				metrics=['accuracy']) 

# import tensorflow as tf
# print(tf.__version__)
# import keras



import numpy as np
import matplotlib.pyplot as plt
import random
import os
import cv2
import glob
print('Fully Imported... Starting!')




DATADIR = '.\\Data\\CharFolders'
CATEGORIES = []
IMG_SIZE_W, IMG_SIZE_H = 81, 108

for folder in glob.glob(f'{DATADIR}\\*'):
    Foldername = os.path.basename(folder)
    # print(f'  f={folder}\n  n={Foldername}')
    CATEGORIES.append(Foldername)



print('Started Creating Training Data')
training_data = []

def create_training_data():
    for category in CATEGORIES:  # for each CATEGORY

        path = os.path.join(DATADIR,category)  # create path to dogs and cats
        class_num = CATEGORIES.index(category)  # get the Num of class


        # Progress % Variables
        totalfileamount = len(os.listdir(path))
        CurFileNum = 0

        for img in os.listdir(path):  # iterate over each image
            CurFileNum += 1
            # Show Progress
            if CurFileNum % 100 == 0:
                print(f'\rGenereting Data for char "{category}" at {round(CurFileNum / totalfileamount * 100, 1)}%',
                      end='')

            # Process
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE_W, IMG_SIZE_H))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add to our training_data
            except Exception as e:  # ignore errors
                pass

        print(f'\rGenereting Data for char "{category}" at 100% Done.')
print('')
create_training_data()
print('Done Creating Training Data')

print(f'len(training_data) = {len(training_data)}')


print(f'Shuffeling Data...', end='')
random.shuffle(training_data)
print(' done.')

for sample in training_data[:10]:
    print(f'data sample:\n{sample[1]}')



print('Put data and label in x and y')
x = []
y = []

for features, label in training_data:
    x.append(features)
    y.append(label)

print('Reshape x and y')
x = np.array(x).reshape(-1, IMG_SIZE_W, IMG_SIZE_H, 1)
y = np.array(y)




# Save Training Data
print('Save Dumping data onto .pickle files.')
import pickle

# Dump X data to file
pickle_out = open('CapLargeData_X.pickle', 'wb')
pickle.dump(x, pickle_out)
pickle_out.close()

# Dump y data to file
pickle_out = open('CapLargeData_Y.pickle', 'wb')
pickle.dump(y, pickle_out)
pickle_out.close()


print('Load Dumping data from .pickle files.')
# Load Training Data
pickle_in = open('CapLargeData_X.pickle', 'rb')
x = pickle.load(pickle_in)
pickle_in = open('CapLargeData_Y.pickle', 'rb')
y = pickle.load(pickle_in)

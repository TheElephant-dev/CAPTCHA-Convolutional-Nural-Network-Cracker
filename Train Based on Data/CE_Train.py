import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard


from time import gmtime, strftime


#Limit VRAM usage to 66% so other vram applications can run in backround.
gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.666)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))



def TrainWith(TrainData, NameAddition, ConvKernalSize, CoveLayerC, EpocNum, validation_split, ConvStride,ConvActivationMethod, CompilerOptimizersMethod):
    X = TrainData[0]
    y = TrainData[1]

    SettingsString = f'ConKS.{ConvKernalSize}_ConLC.{CoveLayerC}_Epoc.{EpocNum}_VSplit.{validation_split}_ConStrid.{ConvStride}_ConAM.{ConvActivationMethod}_CompOptM.{CompilerOptimizersMethod}'
    #######################################################################################
    ################################# Define A Logs Dir
    NAME = f'{SettingsString}__AT_{str(strftime("%Y-%m-%d_%H-%M-%S", gmtime()))}_{NameAddition}'
    LOGDIR = f'logs/{NAME}'
    from tensorflow.keras.callbacks import TensorBoard
    TensorBoard = TensorBoard(log_dir=LOGDIR)
    # tensorboard --logdir=".\\Code\\Convolutional - Experiment\\logs"

    print(f'Training "{NAME}"')
    ################################# Create A Model
    # Create a Model

    model = Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))


    model.compile(loss='sparse_categorical_crossentropy', optimizer=CompilerOptimizersMethod, metrics=['accuracy'])

    ################################# Train the Model

    model.fit(X, y, epochs=EpocNum, validation_split=validation_split, callbacks=[TensorBoard])


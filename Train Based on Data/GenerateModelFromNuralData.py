print('Importing...')
import pickle
from CE_Train import TrainWith
# tensorboard --logdir=".\\Code\\Convolutional - Experiment\\logs"

################################# Imports
#######################################################################################
################################# Load in Training Data
print('Loading in Training Data...')

X = pickle.load(open('CapLargeData_X.pickle', 'rb'))/255.0
y = pickle.load(open('CapLargeData_Y.pickle', 'rb'))
print('Training Data Loaded.')



################################# Load in Training Data
#######################################################################################
################################# Training Variations




# ConvKernalSizes = [16, 32, 64, 128, 256]
# ConvStrides = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
# ConvPoolings = [(1, 1), (2, 2), (3, 3)]
# ConvLayers = [0, 1, 2, 3, 4, 5]
# ConvActivationMethods = ['elu', 'exponential', 'gelu', 'hard_sigmoid', 'linear', 'relu', 'selu', 'sigmoid', 'softmax', 'softplus', 'softsign', 'swish', 'tanh']
#
# DenseSizes = [0, 1, 2 ,16, 32, 512]
# DenseLayers = [0, 1, 2, 3, 4, 5]
# DenseActivationMethods = ['relu', 'selu', 'sigmoid']
#
# FinishActivationMethods = ['relu', 'selu', 'sigmoid']
#
# CompilerLossMethods = ['binary_crossentropy']
# CompilerOptimizersMethods = ['Adadelta', 'Adagrad', 'Adam', 'Adamax', 'Ftrl', 'Nadam', 'RMSprop', 'SGD']
# CompilerMetricsMethods = [['accuracy']]
#
# TrainingBatchSizes = [16, 32, 64]
# validation_splits = [0.05, 0.1, 0.2]

TrainingBatchName = 'RecheckEighththBatch'




# Retry Later:
# ConvActivationMethods = ['relu', 'swish', 'hard_sigmoid', 'sigmoid', 'exponential', 'softplus']
# CompilerOptimizersMethods = ['Adam', 'Adamax', 'Nadam', 'RMSprop']







#Decided Settings
EpocNum = 5
ConvKernalSizes = [32]
ConvStrides = [(3, 3)]
ConvActivationMethods = ['relu']
CoveLayerCs = [2]


validation_splits = [0.1]
CompilerOptimizersMethods = ['adam']






TotalVariations = len(ConvKernalSizes) * len(ConvStrides) * len(CoveLayerCs) * len(validation_splits) * len(ConvActivationMethods) * len(CompilerOptimizersMethods)
VariationCounter = 0
for CompilerOptimizersMethod in CompilerOptimizersMethods:
    for ConvActivationMethod in ConvActivationMethods:
        for ConvStride in ConvStrides:
            for validation_split in validation_splits:
                for ConvKernalSize in ConvKernalSizes:
                    for CoveLayerC in CoveLayerCs:
                            VariationCounter += 1
                            print(f'Running TrainSet Num ({VariationCounter}\{TotalVariations}):')
                            TrainWith([X, y], TrainingBatchName, ConvKernalSize, CoveLayerC, EpocNum, validation_split, ConvStride, ConvActivationMethod, CompilerOptimizersMethod)
print(f'VariationCounter = {VariationCounter}')
################################# Training Variations
#######################################################################################

print('Done')

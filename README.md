# CAPTCHA-Convolutional-Nural-Network-Cracker





<p align="center">
   CAPTCHA-Convolutional-Nural-Network-Cracker.
</p>

# Disclaimer
This project was made for Educational Use only. i do not condone these scripts being used to commit any malicious or fraudulent action.

# Configuration&usage
Each folder contains its own script that will require its own "Assets" Folder with different "stages" of image processing.

After you gathered your images. (1000 images minimum for good results)
Example images:
<p align="center">
   <img src="readmeImages\OriginalImages\Image0.jpg">
   <img src="readmeImages\OriginalImages\Image1.jpg">
   <img src="readmeImages\OriginalImages\Image2.jpg">
</p>


## Stage #1: "ImageSplitter":
  - This Script will handle initial images.
  - images under `\Assets\FullImages` will be split into 2 images. (left and right) and placed in `\Assets\SplitImages`.
<p align="center">
   <img src="readmeImages\ImageSplitter\0_1.png">
   <img src="readmeImages\ImageSplitter\0_2.png">
   <img src="readmeImages\ImageSplitter\1_1.png">
   <img src="readmeImages\ImageSplitter\1_2.png">
   <img src="readmeImages\ImageSplitter\2_1.png">
   <img src="readmeImages\ImageSplitter\2_2.png">
</p>


## Stage #2: "ImageIdentity":
  - This Scipt will load up a small application that will display your image in a large scale, awaiting for you to Identity it.
  - Identity each image by clicking the proper key on your keyboard representing the image on screen. then "Enter" to save.
  - If a mistake was made, you can close the application by clicking the X at the top corner or the `Esc` button. 
  once you open the application again it will pick up 1 image before where you last stopped, allowing for error correction.
  - images under `\Assets\SplitImages` will be displayed in the application. And Identified Images will be placed in `\Assets\CharFolders\{Char}`.


<p align="center">
   <img src="readmeImages\ImageIdentity\0.png">
   <img src="readmeImages\ImageIdentity\1.png">
   <img src="readmeImages\ImageIdentity\2.png">
   <img src="readmeImages\ImageIdentity\3.png">
   <img src="readmeImages\ImageIdentity\4.png">
   <img src="readmeImages\ImageIdentity\5.png">
</p>

## Stage #3: "CheckCharImages":
### This stage is optional, but recommended
- This Scipt will go through all your `\Assets\CharFolders\` foldesr and let you know:
  - What chars exist.
  - What chars dont exist.
  - What is the avarage amount of Images of char, per char, of the chars that exist.

## Stage #4: "ImageMultiplier":
- This Script will go through `\Assets\{GivenFolderName}` and will multiply your image data set by small changes and variation such as:
  - Rotation angle.
  - Placement Shift.
  - Color Inversion.
 - with adjustable settings for variation, total file size+amount prediction.
 default settings will turn each image into 126 images. (or 1000 images into 126000 images.)

<p align="center">
   <img src="readmeImages\ImageMultiplier\0.png">
   <img src="readmeImages\ImageMultiplier\0_InvertedColor_rot-5_mov-5.5.png">
   <img src="readmeImages\ImageMultiplier\0_OGColor__rot10_mov5.5.png">
   <img src="readmeImages\ImageMultiplier\1_InvertedColor_rot-15_mov-5.0.png">
   <img src="readmeImages\ImageMultiplier\1_InvertedColor_rot0_mov-5.0.png">
   <img src="readmeImages\ImageMultiplier\1_OGColor__rot10_mov-5.5.png">
</p>

## Stage #5: "CreateDataFromImages":
  - This script will generate Numpy arrays from all the images you have given it, and save them in `.pickle` form. (could take a while)
  *to be used in stage #6. 

## Stage #6: "Train Based on Data":
  ### Substage #6.1: "GenerateModelFromNuralData":
  - This script will contain the model settings you might want to use to generate your model.
  with the following configuration options:
    - ConvKernalSizes = [16, 32, 64, 128, 256]
    - ConvStrides = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    - ConvPoolings = [(1, 1), (2, 2), (3, 3)]
    - ConvLayers = [0, 1, 2, 3, 4, 5]
    - ConvActivationMethods = ['elu', 'exponential', 'gelu', 'hard_sigmoid', 'linear', 'relu', 'selu', 'sigmoid', 'softmax', 'softplus', 'softsign', 'swish', 'tanh']
    - DenseSizes = [0, 1, 2 ,16, 32, 512]
    - DenseLayers = [0, 1, 2, 3, 4, 5]
    - DenseActivationMethods = ['relu', 'selu', 'sigmoid']
    - FinishActivationMethods = ['relu', 'selu', 'sigmoid']
    - CompilerLossMethods = ['binary_crossentropy']
    - CompilerOptimizersMethods = ['Adadelta', 'Adagrad', 'Adam', 'Adamax', 'Ftrl', 'Nadam', 'RMSprop', 'SGD']
    - CompilerMetricsMethods = [['accuracy']]
    - TrainingBatchSizes = [16, 32, 64]
    - validation_splits = [0.05, 0.1, 0.2]
  - You may use, and it is recommended to use more then 1 setting at a time, the script will just generate multible models and train them all.

  ### Substage #6.2: "CE_Train":
  - This Script will train each model given to it by "GenerateModelFromNuralData" (Substage #6.1). and save the results under `\logs\`

## use command `tensorboard --logdir="{LOGS FOLDER HERE}"` to view your results.
note: you can view the results while the model is training.


<p align="center">
   <img src="readmeImages\epoch_accuracy.png">
   <img src="readmeImages\epoch_loss.png">
   <img src="readmeImages\evaluation_accuracy_vs_iterations.png">
   <img src="readmeImages\evaluation_loss_vs_iterations.png">
</p>







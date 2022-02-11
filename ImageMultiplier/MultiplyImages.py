from PIL import Image
import PIL.ImageOps
import os
import glob
from time import sleep as s

import matplotlib.pyplot as plt





print(f'The folloing are ImgRotatAngles:')
ImgRotatAngles = range(-15, 16, 5)
for x in ImgRotatAngles:
    print(f'  - {x}')



print(f'The folloing are ImgMoveCordList:')
MPC = 5 #MovementPixalCount
ImgMoveCordList = [[MPC, MPC], [0, MPC], [MPC*-1, MPC], [MPC*-1, 0], [MPC*-1, MPC*-1], [0, MPC*-1], [MPC, MPC*-1], [MPC, 0], [0, 0]]
for x, y in ImgMoveCordList:
    print(f'  - x={x}, y={y}')

variation = len(ImgRotatAngles) * len(ImgMoveCordList)*2
print(f'The amount of variation per image with the current settings is:{variation}, per image given')



















def ProcessImageTrowMods(OriginalImage, savepath):


    for IRA in ImgRotatAngles:
        # Create a rotated Image
        RotatedImage = OriginalImage.copy().rotate(angle=IRA, resample=Image.BICUBIC)
        # Paste rotated image on original image
        ROTATEDRESULT = OriginalImage.copy()
        ROTATEDRESULT.paste(RotatedImage, (0, 0), RotatedImage)

        ROTATEDRESULT.save(f"{savepath}_rot{IRA}.png")

        ##### SAVE AT THIS STATE
        for IMCx, IMCy in ImgMoveCordList:
            # Paste rotated image on original image with an offset
            MOVEDRESULT = OriginalImage.copy()
            MOVEDRESULT.paste(ROTATEDRESULT, (IMCx, IMCy), MOVEDRESULT)

            ##### SAVE AT THIS STATE
            ROTATEDRESULT.save(f"{savepath}_rot{IRA}_mov{IMCx}.{IMCy}.png")







WorkingDirectory = 'Assets/CharFolders/*'
ImageCount = 0
FS = 0
for CharFolder in glob.glob(WorkingDirectory):
    for ImagePath in glob.glob(f'{CharFolder}/*'):
        ImageCount += 1
        FS += os.path.getsize(ImagePath)

print(f'CurrentImageCount = {ImageCount} totaling {round(FS / 1000000, 1)}MB or {round(FS / 1000000000, 1)}GB in size.')
print(f'TotalExpected = {ImageCount*variation} totaling {round(FS*variation / 1000000, 1)}MB or {round(FS*variation / 1000000000, 1)}GB in size.')
print(f'PerCharExpected = {ImageCount*variation/28} totaling {round(FS*variation/28 / 1000000, 1)}MB or {round(FS*variation/28 / 1000000000, 1)}GB in size.')



for CharFolder in glob.glob(WorkingDirectory):
    print(f'\n\n######################### Starting Work on char {CharFolder} ...')
    for ImagePath in glob.glob(f'{CharFolder}/*'):
        Filepath = f'{ImagePath}'[:-4]
        print(Filepath)


        PIL_image = Image.open(f'{ImagePath}').convert("RGBA")
        ColorInverted_PIL_image = PIL.ImageOps.invert(PIL_image.convert("RGB")).convert("RGBA")
        ProcessImageTrowMods(PIL_image, f'{Filepath}_OGColor_')
        ProcessImageTrowMods(ColorInverted_PIL_image, f'{Filepath}_InvertedColor')
    print(f'\n######################### Done Work on char {CharFolder} ...')










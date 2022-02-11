import PIL
from PIL import Image
import pygame
import glob
import os
from time import sleep


# Window Settings
WIDTH, HEIGHT = 648, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Image Identity 9000')
BG = pygame.transform.scale(pygame.image.load('Assets\Backround.png'), (WIDTH, HEIGHT))
pygame.init()
ImageLabelFont = pygame.font.SysFont('candra', 140)
#################################################### -
##################################################################################################################
#################################################### - Temp Settings

SplitImagePaths = glob.glob('.\\Assets\\SplitImages\\*')

CurImgNum = 0
#Load Latest Image
with open('Assets\\CurrSavedFileNum.txt', 'r') as F:
    CurImgNum = int(F.read())

CurImgPyImg = pygame.transform.scale(pygame.image.load(SplitImagePaths[CurImgNum]), (648, 864))
WChar = 'NONE'


#################################################### - Temp Settings
##################################################################################################################
#################################################### - ImageUnit Class

class ImageUnit:
    def __init__(self):
        # Object Data Display
        self.ImageObject = CurImgPyImg
        self.ImageLabel = ImageLabelFont.render(f'meaningless. will redraw.', 1, (200, 200, 200))


    def draw(self, window):
        self.ImageObject = CurImgPyImg
        self.ImageLabel = ImageLabelFont.render(f"Confirm '{WChar}'?", 1, (200, 200, 200))
        window.blit(self.ImageObject, (5, 100))
        window.blit(self.ImageLabel, (5, 5))


IU = ImageUnit()
#################################################### - ImageUnit Class##################################################################################################################
#################################################### - Save Image

def SaveImageToPath(PIL_Image: PIL.Image.Image):
    SAVEPATH = f'Assets\\CharFolders\\{WChar}'
    if os.path.exists(SAVEPATH) == False:
        os.makedirs(SAVEPATH)

    FileNum = len(glob.glob(f'{SAVEPATH}\\*'))
    print(f'Saving {SplitImagePaths[CurImgNum]} as {SAVEPATH}\\{FileNum}.png')
    PIL_Image.save(f"{SAVEPATH}\\{FileNum}.png", format="png")


    # Update CurrSavedFileNum
    with open('Assets\\CurrSavedFileNum.txt', 'w') as F:
        F.write(str(CurImgNum))

#################################################### - Save Image
##################################################################################################################
#################################################### - Main Loop



# Main Loop
def main():
    global WChar
    global CurImgNum
    global CurImgPyImg



    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        IU.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f'Clicked X, closing program!')
                run = False

            if event.type == pygame.KEYDOWN:
                # Key to reset board
                # print(f'Clicked {event.unicode} {event}')

                # Letter or number key
                if event.unicode.isalnum():
                    if event.unicode.upper():
                        WChar = event.unicode.upper()
                        print(f'Changed WChar to "{WChar}"')


                # Enter Key
                elif event.key == 13:
                    print(f'Clicked Enter. Going Forward.(Done {CurImgNum} out of {len(SplitImagePaths)} only {len(SplitImagePaths)-CurImgNum} left to do.)')
                    PIL_Img = Image.open(SplitImagePaths[CurImgNum])
                    SaveImageToPath(PIL_Img)

                    CurImgNum += 1
                    CurImgPyImg = pygame.transform.scale(pygame.image.load(SplitImagePaths[CurImgNum]), (648, 864))
                    print(f'now at {SplitImagePaths[CurImgNum]}')




main()
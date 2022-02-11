from PIL import Image
import glob
import os


for FullImage in glob.glob('Assets\FullImages\*.*'):
    filename = os.path.basename(FullImage)[:-4][5:]
    print(filename)
    IM = Image.open(FullImage)
    S = IM.size
    Chop1 = IM.crop((0, 0, S[0]/2, S[1]))
    Chop2 = IM.crop((S[0]/2, 0, S[0], S[1]))
    Chop1.save(f"Assets\\SplitImages\\{filename}_1.png", format="png")
    Chop2.save(f"Assets\\SplitImages\\{filename}_2.png", format="png")

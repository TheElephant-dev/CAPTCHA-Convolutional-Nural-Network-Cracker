# import PIL
import glob



AllOptions = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'


ExistingCharCounters = []

MissingChars = []
for Char in AllOptions:
    ImageArray = glob.glob(f'.\\Assets\\CharFolders\\{Char}\\*')

    IA_len = len(ImageArray)
    if not IA_len:
        MissingChars.append(Char)
    else:
        print(f'{Char} = {IA_len}')
        ExistingCharCounters.append(IA_len)

print(f'Chars that have no images({len(MissingChars)}) = {MissingChars}')

ExisingCharNums_Avg =  sum(ExistingCharCounters) / len(ExistingCharCounters)
print(f'Exising Char Nums_Avg = {ExisingCharNums_Avg}')


total = 0
for x in ExistingCharCounters:
    total += x
    print(f'total + {x} = {total}')
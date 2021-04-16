from Easter import Easter
from GreenScale import GreenScale

def makePalette(paletteName, iterations):
    if paletteName == 'default':
        return GreenScale(iterations)
    elif paletteName == 'Easter':
        return Easter(iterations)
    elif paletteName == 'GreenScale':
        return GreenScale(iterations)
    else:
        raise NotImplementedError("The palette you are trying to use does not exist. Please see the Manual for Palette options.")
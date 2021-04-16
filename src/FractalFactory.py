from Mandelbrot import Mandelbrot
from Julia import Julia
from Mandelbrot4 import Mandelbrot4

def makeFractal(path):
    if path == 'default':
        dictionary = defaultFractal()
    else:
        fileObj = open(path)
        required = ['type', 'centerx', 'centery', 'axislength', 'pixels', 'iterations']
        juliaReq = ['creal', 'cimag']
        dictionary = {}

        for line in fileObj:
            if line.startswith("#") or line.isspace():
                continue
            else:
                line = line.strip()
                dictEntry = line.split(": ")
                checkedEntry = checkReqs(dictEntry)
                dictionary[checkedEntry[0]] = checkedEntry[1]


        fileObj.close()

        for entry in required:
            if entry not in dictionary:
                raise NotImplementedError("Invalid fractal configuration file")
        if dictionary['type'] == 'julia':
            for entry in juliaReq:
                if entry not in dictionary:
                    raise NotImplementedError("Invalid fractal configuration file")
        else:
            for entry in juliaReq:
                if entry in dictionary:
                    raise NotImplementedError("Invalid fractal configuration file")

        dictionary = updateDictionary(dictionary, path)

    if dictionary['type'] == 'mandelbrot':
        return Mandelbrot(dictionary)
    elif dictionary['type'] == 'julia':
        return Julia(dictionary)
    elif dictionary['type'] == 'mandelbrot4':
        return Mandelbrot4(dictionary)
    else:
        raise NotImplementedError("This program does not support the fractal you entered. Please see the Manual for fractal options.")


def defaultFractal():
    print("Creating a default fractal")
    dictionary = {
        'type': 'mandelbrot',
        'pixels': 320,
        'axislength': 4.0,
        'pixelsize': 0.00625,
        'iterations': 100,
        'min': {'x': -2.0, 'y': -2.0},
        'max': {'x': 2.0, 'y': 2.0},
        'imagename': 'fullmandelbrot.png'
    }
    return dictionary

def checkReqs(dictEntry):
    if dictEntry[0].lower() == 'type' and not dictEntry[1].isnumeric():
        return 'type', dictEntry[1].lower()
    elif dictEntry[0].lower() == 'pixels' or 'iterations' and dictEntry[1].isnumeric():
        return dictEntry[0].lower(), int(dictEntry[1])
    elif dictEntry[0].lower() == 'centerx' or dictEntry[0].lower() == 'centery' or dictEntry[0].lower() == 'axislength':
        try:
            return dictEntry[0].lower(), float(dictEntry[1])
        except ValueError:
            print("Invalid configuration file")
    elif dictEntry[0].lower() == 'creal' or 'cimag' and dictEntry[1].isnumeric():
        return dictEntry[0].lower(), float(dictEntry[1])
    else:
        raise NotImplementedError("Invalid fractal configuration file")


def updateDictionary(dictionary, path):
    updatedDict = {
        'type': dictionary['type'],
        'pixels': dictionary['pixels'],
        'axislength': dictionary['axislength'],
        'pixelsize': abs(dictionary['axislength'] / dictionary['pixels']),
        'iterations': dictionary['iterations'],
        'min': {'x': dictionary['centerx'] - (dictionary['axislength'] / 2.0),
                'y': dictionary['centery'] - (dictionary['axislength'] / 2.0)},
        'max': {'x': dictionary['centerx'] + (dictionary['axislength'] / 2.0),
                'y': dictionary['centery'] + (dictionary['axislength'] / 2.0)},
        'imagename': path.split("/")[-1].split(".")[0] + "png"
        # This splits the path into its directories, and takes the last one (the file name) and splits it on "." to get rid
        # of the current file type ending to replace it with png
    }
    if updatedDict['type'] == 'julia':
        updatedDict['creal'] = dictionary['creal']
        updatedDict['cimag'] = dictionary['cimag']
    return updatedDict


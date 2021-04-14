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
                dictEntry = line.split(": ")
                checkedEntry = checkReqs(dictEntry, dictionary)
                dictionary[checkedEntry[0]] = checkedEntry[1]
        fileObj.close()

        for entry in required:
            if entry not in dictionary:
                raise NotImplementedError("Invalid fractal configuration file")
        if dictionary['type'] == 'julia':
            for entry in juliaReq:
                if entry not in dictionary:
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
        'pixels': 640,
        'axislength': 4.0,
        'pixelsize': 0.00625,
        'iterations': 100,
        'min': {'x': -2.0, 'y': -2.0},
        'max': {'x': 2.0, 'y': 2.0},
        'imagename': 'fullmandelbrot.png'
    }
    return dictionary

def checkReqs(dictEntry, dictionary):
    if dictEntry[0].lower() == 'type' and not dictEntry[1].isnumeric():
        return 'type', dictEntry[1].lower()
    elif dictEntry[0].lower() == 'pixels' and dictEntry[1].isnumeric() and not dictEntry[1].__contains__("."):
        return'pixels', int(dictEntry[1])
    elif dictEntry[0].lower() == 'centerx' and dictEntry[1].isnumeric():
        return 'centerX', float(dictEntry[1])
    elif dictEntry[0].lower() == 'centery' and dictEntry[1].isnumeric():
        return 'centerY', float(dictEntry[1])
    elif dictEntry[0].lower() == 'axislength' and dictEntry[1].isnumeric():
        return 'axislength', float(dictEntry[1])
    elif dictEntry[0].lower() == 'iterations' and dictEntry[1].isnumeric() and not dictEntry[1].__contains__("."):
        return 'iterations', int(dictEntry[1])
    if dictionary['type'] == 'julia':
        return checkJuliaReqs(dictEntry)
    else:
        raise NotImplementedError("Invalid fractal configuration file")

def checkJuliaReqs(dictEntry):
    if dictEntry[0].lower() == 'creal' and dictEntry[1].isnumeric():
        return 'creal', float(dictEntry[1])
    elif dictEntry[0].lower() == 'cimag' and dictEntry[1].isnumeric():
        return 'cimag', float(dictEntry[1])
    else:
        raise NotImplementedError("Invalid fractal configuration file")

def updateDictionary(dictionary, path):
    return {
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



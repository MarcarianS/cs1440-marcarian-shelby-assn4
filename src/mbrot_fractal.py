#!/bin/env python3

# Mandelbrot Set Visualizer

import sys
from time import time
from tkinter import mainloop
import ImagePainter
import FractalInformation

WHITE = '#ffffff'
IMG_SIZE = 512


def makePicture(fractalInfo, image):
    """Set up all information needed from the Fractal Info
    and send it to the ImagePainter class.
    To change the size of the image printed, change IMG_SIZE at
    top of file."""

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractalInfo['centerX'] - (fractalInfo['axisLen'] / 2.0)
    maxx = fractalInfo['centerX'] + (fractalInfo['axisLen'] / 2.0)
    miny = fractalInfo['centerY'] - (fractalInfo['axisLen'] / 2.0)
    z = fractalInfo['z']

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelSize = abs(maxx - minx) / IMG_SIZE
    image.paint(minx, miny, pixelSize, IMG_SIZE, z)


def mbrot_main(fractalInfo, fractalName):

    # Create an ImagePainter object to deal with
    image = ImagePainter.ImagePainter(IMG_SIZE, WHITE)

    # Call paint, which runs the bulk of the program
    # and time the rendering.
    before = time()
    makePicture(fractalInfo, image)
    after = time()

    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    image.writePNG(fractalName)
    print(f"Wrote image {fractalName}.png")

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program")
    mainloop()


def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels

if __name__ == '__main__':
    fractals = FractalInformation.FractalInformation().getDictionary()
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for i in fractals:
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in fractals:
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in fractals:
            print(f"\t{i}")
        sys.exit(1)

    elif fractals[sys.argv[1]]['type'] != 'mandelbrot':
        print(f"ERROR: You are trying to print a Julia fractal from mbrot_fractal.py")
        input = input("Proceed? (y or n): ")
        if input.lower().startswith("y"):
            mbrot_main(fractals[sys.argv[1]], sys.argv[1])
        else:
            sys.exit(1)

    else:
        mbrot_main(fractals[sys.argv[1]], sys.argv[1])

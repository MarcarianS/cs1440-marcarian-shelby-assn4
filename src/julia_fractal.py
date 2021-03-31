#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time



# This is the color palette, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
GRAD = [
        '#ffe4b5', '#ffe5b2', '#ffe7ae', '#ffe9ab', '#ffeaa8', '#ffeda4',
        '#ffefa1', '#fff29e', '#fff49a', '#fff797', '#fffb94', '#fffe90',
        '#fcff8d', '#f8ff8a', '#f4ff86', '#f0ff83', '#ebff80', '#e7ff7c',
        '#e2ff79', '#ddff76', '#d7ff72', '#d2ff6f', '#ccff6c', '#c6ff68',
        '#bfff65', '#b9ff62', '#b2ff5e', '#abff5b', '#a4ff58', '#9dff54',
        '#95ff51', '#8dff4e', '#85ff4a', '#7dff47', '#75ff44', '#6cff40',
        '#63ff3d', '#5aff3a', '#51ff36', '#47ff33', '#3eff30', '#34ff2c',
        '#2aff29', '#26ff2c', '#22ff30', '#1fff34', '#1cff38', '#18ff3d',
        '#15ff42', '#11ff47', '#0eff4c', '#0bff51', '#07ff57', '#04ff5d',
        '#01ff63', '#00fc69', '#00f970', '#00f677', '#00f27d', '#00ef83',
        '#00ec89', '#00e88e', '#00e594', '#00e299', '#00de9e', '#00dba3',
        '#00d8a7', '#00d4ab', '#00d1af', '#00ceb3', '#00cab7', '#00c7ba',
        '#00c4be', '#00c0c0', '#00b7bd', '#00adba', '#00a4b6', '#009cb3',
        '#0093b0', '#008bac', '#0082a9', '#007ba6', '#0073a2', '#006b9f',
        '#00649c', '#005d98', '#005695', '#004f92', '#00498e', '#00438b',
        '#003d88', '#003784', '#003181', '#002c7e', '#00277a', '#002277',
        ]
WHITE = '#ffffff'
IMG_SIZE = 512

global photo

def getColorFromPalette(z, GRAD):
    """Return the index of the color of the current pixel within the Julia set
    in the palette array"""

    # c is the Julia Constant; varying this value can yield interesting images
    c = complex(-1.0, 0.0)

    # loop through each color in the palette
    for i in range(len(GRAD)):
        z = z * z + c  # Iteratively compute z1, z2, z3 ...
        if abs(z) > 2:
            return GRAD[i]  # The sequence is unbounded
    return GRAD[77]         # Else this is a bounded sequence


photo = None

def makePicture(fractalInfo, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 512x512 pixels."""


    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
    min = ((fractalInfo['centerX'] - (fractalInfo['axisLength'] / 2.0)),
           (fractalInfo['centerY'] - (fractalInfo['axisLength'] / 2.0)))

    max = ((fractalInfo['centerX'] + (fractalInfo['axisLength'] / 2.0)),
           (fractalInfo['centerY'] + (fractalInfo['axisLength'] / 2.0)))


    # Display the image on the screen
    canvas = Canvas(window, width=IMG_SIZE, height=IMG_SIZE, bg=WHITE)
    canvas.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?
    canvas.create_image((256, 256), image=photo, state="normal")

    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    pixSize = abs(max[0] - min[0]) / 512.0

    for r in range(IMG_SIZE, 0, -1):
        for c in range(IMG_SIZE):
            x = min[0] + c * pixSize
            y = min[1] + r * pixSize
            c2 = getColorFromPalette(complex(x, y), GRAD)
            photo.put(c2, (c, IMG_SIZE - r))
        window.update()  # display a row of pixels

# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# the configuration dictionary instead of hardcoding it into this program?


def julia_main(fractalInfo, fractalName):

    global photo

    # Set up the GUI so that we can display the fractal image on the screen
    before = time()
    window = Tk()

    photo = PhotoImage(width=IMG_SIZE, height=IMG_SIZE)
    makePicture(fractalInfo, window)

    print(f"Done in {time() - before:.3f} seconds!", file=sys.stderr)
    # Output the Fractal into a .png image
    photo.write(fractalName + ".png")
    print("Wrote picture " + fractalName + ".png")

    print("Close the image window to exit the program")
    # Call tkinter.mainloop so the GUI remains open
    mainloop()


# if __name__ == '__main__':
#     # Process command-line arguments, allowing the user to select their fractal
#     if len(sys.argv) < 2:
#         print("Please provide the name of a fractal as an argument")
#         for i in f:
#             print(f"\t{i}")
#         sys.exit(1)
#
#     elif sys.argv[1] not in f:
#         print(f"ERROR: {sys.argv[1]} is not a valid fractal")
#         print("Please choose one of the following:")
#         for i in f:
#             print(f"\t{i}")
#         sys.exit(1)
#
#     else:
#         # fractal_config = getFractalName(sys.argv[1])
#         julia_main(sys.argv[1])

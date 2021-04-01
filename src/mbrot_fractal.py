#!/bin/env python3

# Mandelbrot Set Visualizer


import sys
from time import time
from tkinter import Tk, Canvas, PhotoImage, mainloop

# This color palette contains 96 color steps.
palette = [
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




def colorOfThePixel(c, palette):
    """Return the color of the current pixel within the Mandelbrot set"""
    z = complex(0, 0)

    for i in range(len(palette)):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            return palette[i]  # The sequence is unbounded
    return palette[len(palette) - 1]   # Indicate a bounded sequence


img = None


def paint(fractalInfo, window):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 512x512 pixels in size.
    To change this size, change IMG_SIZE at top of file."""


    global img


    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractalInfo['centerX'] - (fractalInfo['axisLen'] / 2.0)
    maxx = fractalInfo['centerX'] + (fractalInfo['axisLen'] / 2.0)
    miny = fractalInfo['centerY'] - (fractalInfo['axisLen'] / 2.0)
    #z = fractalInfo['z']

    # Display the image on the screen
    canvas = Canvas(window, width=IMG_SIZE, height=IMG_SIZE, bg=WHITE)
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelSize = abs(maxx - minx) / IMG_SIZE
    #imagePainter.paint(minx, miny, pixelSize, IMG_SIZE, z)

    for row in range(IMG_SIZE, 0, -1):
        for col in range(IMG_SIZE):
            x = minx + col * pixelSize
            y = miny + row * pixelSize
            color = colorOfThePixel(complex(x, y), palette)
            img.put(color, (col, IMG_SIZE - row))
        window.update()  # display a row of pixels


def mbrot_main(fractalInfo, fractalName):
    global img
    # Set up the GUI so that we can paint the fractal image on the screen
    before = time()
    window = Tk()
    img = PhotoImage(width=IMG_SIZE, height=IMG_SIZE)
    paint(fractalInfo, window)
    #definePicture(fractalInfo)
    #paint(minX, minY, pixelSize, IMG_SIZE, z)
    # Save the image as a PNG
    after = time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{fractalName}.png")
    print(f"Wrote image {fractalName}.png")

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program")
    mainloop()


def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels

# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("Please provide the name of a fractal as an argument")
#         for i in images:
#             print(f"\t{i}")
#         sys.exit(1)
#
#     elif sys.argv[1] not in images:
#         print(f"ERROR: {sys.argv[1]} is not a valid fractal")
#         print("Please choose one of the following:")
#         for i in images:
#             print(f"\t{i}")
#         sys.exit(1)
#
#     else:
#         mbrot_main(sys.argv[1])

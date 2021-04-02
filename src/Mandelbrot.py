import sys
from tkinter import mainloop
from time import time
from ImagePainter import ImagePainter
from Palette import Palette

WHITE = '#ffffff'
IMG_SIZE = 512

class Mandelbrot:

    def getIteration(self, c, z, paletteSize):
        for i in range(paletteSize):
            z = z * z + c
            if abs(z) > 2:
                return i
        return paletteSize - 1

    def mbrot_main(self, fractalInfo, fractalName):

        # Create an ImagePainter object to deal with
        image = ImagePainter(IMG_SIZE, WHITE)

        # Correlate the boundaries of the PhotoImage object to the complex
        # coordinates of the imaginary plane
        minX = fractalInfo['centerX'] - (fractalInfo['axisLen'] / 2.0)
        maxX = fractalInfo['centerX'] + (fractalInfo['axisLen'] / 2.0)
        minY = fractalInfo['centerY'] - (fractalInfo['axisLen'] / 2.0)
        z = fractalInfo['z']
        paletteSize = Palette().getSize()
        pixelSize = abs(maxX - minX) / IMG_SIZE

        before = time()
        for row in range(IMG_SIZE, 0, -1):
            for col in range(IMG_SIZE):
                x = minX + col * pixelSize
                y = minY + row * pixelSize
                index = self.getIteration(complex(x, y), z, paletteSize)
                image.paint(index, row, col, IMG_SIZE)
            image.update()
        after = time()

        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        image.writePNG(fractalName)
        print(f"Wrote image {fractalName}.png")
        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program")
        mainloop()

    def pixelsWrittenSoFar(self, rows, cols):
        pixels = rows * cols
        print(f"{pixels} pixels have been output so far")
        return pixels


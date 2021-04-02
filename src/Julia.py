import sys
from tkinter import mainloop
from time import time
from ImagePainter import ImagePainter
from Palette import Palette


WHITE = '#ffffff'
IMG_SIZE = 512

class Julia:

    def getIteration(self, c, z, paletteSize):
        for i in range(paletteSize):
            c = c * c + z
            if abs(c) > 2:
                return i
        return 77


    def julia_main(self, fractalInfo, fractalName):
        # Create an ImagePainter object to work with later
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
        # Output the Fractal into a .png image
        image.writePNG(fractalName)
        print(f"Wrote picture {fractalName}.png")

        print("Close the image window to exit the program")
        # Call tkinter.mainloop so the GUI remains open
        mainloop()


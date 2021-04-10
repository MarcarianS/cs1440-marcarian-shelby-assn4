from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time
import sys

from Palette import Palette
import Julia
import Mandelbrot

IMG_SIZE = 512
BG = '#ffffff'

class ImagePainter:
    '''
    The constructor sets up the window for an entire fractal picture;
    it only needs to be called once in teh program if you only want one
    picture.
    '''
    def __init__(self):
        self.__window = Tk()
        self.__canvas = Canvas(self.__window, width=IMG_SIZE, height=IMG_SIZE, bg=BG)
        self.__canvas.pack()
        self.__image = PhotoImage(width=IMG_SIZE, height=IMG_SIZE)
        self.__canvas.create_image((IMG_SIZE / 2, IMG_SIZE / 2), image=self.__image, state="normal")

    def paint(self, imageName, fractalInfo):
        '''
        Bulk of the rendering; uses information from the fractal to
        render the image.
        '''
        before = time()

        minX = fractalInfo['centerX'] - (fractalInfo['axisLen'] / 2.0)
        maxX = fractalInfo['centerX'] + (fractalInfo['axisLen'] / 2.0)
        minY = fractalInfo['centerY'] - (fractalInfo['axisLen'] / 2.0)
        z = fractalInfo['z']
        max_iter = Palette().getSize() - 1
        pixelSize = abs(maxX - minX) / IMG_SIZE

        if fractalInfo['type'] == 'julia':
            count = Julia.count
        elif fractalInfo['type'] == 'mandelbrot':
            count = Mandelbrot.count

        for row in range(IMG_SIZE, 0, -1):
            for col in range(IMG_SIZE):
                x = minX + col * pixelSize
                y = minY + row * pixelSize
                color = Palette().getColor(count(complex(x, y), max_iter, z))
                self.__image.put(color, (col, IMG_SIZE - row))
            self.__window.update()

        after = time()

        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        # Output the Fractal into a .png image
        self.__image.write(f"{imageName}.png")
        print(f"Wrote picture {imageName}.png")

        print("Close the image window to exit the program")
        # Call tkinter.mainloop so the GUI remains open
        mainloop()


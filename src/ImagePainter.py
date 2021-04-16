from tkinter import Tk, Canvas, PhotoImage, mainloop

import FractalFactory
import PaletteFactory

BG = '#ffffff'

class ImagePainter:
    def __init__(self):
        pass
    def paint(self, fractalPath, paletteName):
        fractal = FractalFactory.makeFractal(fractalPath)
        fractalInfo = fractal.getDictionary()
        paletteSize = fractalInfo['iterations']
        palette = PaletteFactory.makePalette(paletteName, paletteSize)
        pixelSize = fractalInfo['pixelsize']

        imageSize = fractalInfo['pixels']
        window = Tk()
        canvas = Canvas(window, width=imageSize, height=imageSize, bg=BG)
        image = PhotoImage(width=imageSize, height=imageSize)
        canvas.create_image((imageSize / 2, imageSize / 2), image=image, state="normal")
        canvas.pack()

        for row in range(imageSize, 0, -1):
            for col in range(imageSize):
                x = fractalInfo['min']['x'] + col * pixelSize
                y = fractalInfo['min']['y'] + row * pixelSize
                color = palette.getColor(fractal.count(complex(x, y)))
                image.put(color, (col, imageSize - row))
            window.update()

        image.write(fractalInfo['imagename'])
        print(f"Wrote picture {fractalInfo['imagename']}")
        mainloop()

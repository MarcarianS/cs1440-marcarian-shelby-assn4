from tkinter import Tk, Canvas, PhotoImage, mainloop
import Palette

class ImagePainter:
    def __init__(self, IMG_SIZE, bg):
        self.__window = Tk()
        self.__canvas = Canvas(self.__window, width=IMG_SIZE, height=IMG_SIZE, bg=bg)
        self.__canvas.pack()
        self.__image = PhotoImage(width=IMG_SIZE, height=IMG_SIZE)
        self.__canvas.create_image((256, 256), image=self.__image, state="normal")

    def paint(self, minX, minY, pixelSize, IMG_SIZE, z):
        for row in range(IMG_SIZE, 0, -1):
            for col in range(IMG_SIZE):
                x = minX + col * pixelSize
                y = minY + row * pixelSize
                color = self.calculateColor(complex(x, y), z)
                self.__image.put(color, (col, IMG_SIZE - row))
            self.__window.update()


    def calculateColor(self, complex, z):
        palette = Palette.Palette()
        for i in range(palette.getSize()):
            z = z * z + complex
            if abs(z) > 2:
                return palette.getColor(i)
        return palette.getColor(palette.getSize() - 1)


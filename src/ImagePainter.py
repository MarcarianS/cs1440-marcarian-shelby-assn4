from tkinter import Tk, Canvas, PhotoImage
from Palette import Palette

class ImagePainter:
    '''
    The constructor sets up the window for an entire fractal picture;
    it only needs to be called once in teh program if you only want one
    picture.
    '''
    def __init__(self, IMG_SIZE, bg):
        self.__window = Tk()
        self.__canvas = Canvas(self.__window, width=IMG_SIZE, height=IMG_SIZE, bg=bg)
        self.__canvas.pack()
        self.__image = PhotoImage(width=IMG_SIZE, height=IMG_SIZE)
        self.__canvas.create_image((IMG_SIZE / 2, IMG_SIZE / 2), image=self.__image, state="normal")

    def paint(self, index, row, col, IMG_SIZE):
        '''
        Bulk of the rendering; uses information from the fractal to
        render the image.
        '''
        color = Palette().getColor(index)
        self.__image.put(color, (col, IMG_SIZE - row))

    def update(self):
            self.__window.update()

    def writePNG(self, name):
        self.__image.write(f"{name}.png")

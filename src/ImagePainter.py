from tkinter import Tk, Canvas, PhotoImage
import Palette

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

    def paint(self, minX, minY, pixelSize, IMG_SIZE, z):
        '''
        Bulk of the rendering; uses information from the fractal to
        render the image.
        '''
        for row in range(IMG_SIZE, 0, -1):
            for col in range(IMG_SIZE):
                x = minX + col * pixelSize
                y = minY + row * pixelSize
                color = self.calculateColor(complex(x, y), z)
                self.__image.put(color, (col, IMG_SIZE - row))
            # makes it update line by line
            self.__window.update()


    def calculateColor(self, c, z):
        palette = Palette.Palette()

        # If the fractal is from mandelbrot, z is the complex that iterates
        if z == complex(0.0, 0.0):
            for i in range(palette.getSize()):
                z = z * z + c
                if abs(z) > 2:
                    return palette.getColor(i)
            return palette.getColor(palette.getSize() - 1)

        # If the fractal is from julia, z is te complex that remains constant
        elif z == complex(-1.0, 0.0):
            for i in range(palette.getSize()):
                c = c * c + z
                if abs(c) > 2:
                    return palette.getColor(i)
            return palette.getColor(77)



    def writePNG(self, name):
        self.__image.write(f"{name}.png")

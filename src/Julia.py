import sys
from tkinter import mainloop
from time import time
import ImagePainter
import FractalInformation

WHITE = '#ffffff'
IMG_SIZE = 512

class Julia:

    def __makePicture(self, fractalInfo, image):
        # Correlate the boundaries of the PhotoImage object to the complex
        # coordinates of the imaginary plane
        minX = fractalInfo['centerX'] - (fractalInfo['axisLen'] / 2.0)
        maxX = fractalInfo['centerX'] + (fractalInfo['axisLen'] / 2.0)
        minY = fractalInfo['centerY'] - (fractalInfo['axisLen'] / 2.0)
        z = fractalInfo['z']

        pixelSize = abs(maxX - minX) / IMG_SIZE
        image.paint(minX, minY, pixelSize, IMG_SIZE, z)

    def julia_main(self, fractalInfo, fractalName):
        # Create an ImagePainter object to work with later
        image = ImagePainter.ImagePainter(IMG_SIZE, WHITE)

        before = time()
        self.__makePicture(fractalInfo, image)
        after = time()

        print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)
        # Output the Fractal into a .png image
        image.writePNG(fractalName)
        print(f"Wrote picture {fractalName}.png")

        print("Close the image window to exit the program")
        # Call tkinter.mainloop so the GUI remains open
        mainloop()

    # if __name__ == '__main__':
    #     fractals = FractalInformation.FractalInformation().getDictionary()
    #     import Julia
    #     # Process command-line arguments, allowing the user to select their fractal
    #     if len(sys.argv) < 2:
    #         print("Please provide the name of a fractal as an argument")
    #         for i in fractals:
    #             print(f"\t{i}")
    #         sys.exit(1)
    #
    #     elif sys.argv[1] not in fractals:
    #         print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    #         print("Please choose one of the following:")
    #         for i in fractals:
    #             print(f"\t{i}")
    #         sys.exit(1)
    #
    #     elif fractals[sys.argv[1]]['type'] != 'julia':
    #         print(f"ERROR: You are trying to print a Mandelbrot fractal from Julia.py")
    #         input = input("Proceed? (y or n): ")
    #         if input.lower().startswith("y"):
    #             Julia.Julia().julia_main(fractals[sys.argv[1]], sys.argv[1])
    #         else:
    #             sys.exit(1)
    #
    #     else:
    #         Julia.Julia().julia_main(fractals[sys.argv[1]], sys.argv[1])

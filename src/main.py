import sys

from FractalInformation import FractalInformation
from Julia import Julia
from Mandelbrot import Mandelbrot
from ImagePainter import ImagePainter


fractals = FractalInformation().getDictionary()

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in fractals:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in fractals:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in fractals:
        print(f"\t{i}")
    sys.exit(1)

else:
    ImagePainter().paint(sys.argv[1], fractals[sys.argv[1]])
    #
    # if fractals[sys.argv[1]]['type'] == 'julia':
    #     Julia().julia_main(fractals[sys.argv[1]], sys.argv[1])
    #
    # elif fractals[sys.argv[1]]['type'] == 'mandelbrot':
    #     Mandelbrot().mbrot_main(fractals[sys.argv[1]], sys.argv[1])
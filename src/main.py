import sys

import FractalInformation
import Julia
import Mandelbrot


FRACTALS = FractalInformation.FractalInformation().getDictionary()

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in FRACTALS:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in FRACTALS:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in FRACTALS:
        print(f"\t{i}")
    sys.exit(1)

else:

    if FRACTALS[sys.argv[1]]['type'] == 'julia':
        Julia.Julia().julia_main(FRACTALS[sys.argv[1]], sys.argv[1])

    elif FRACTALS[sys.argv[1]]['type'] == 'mandelbrot':
        Mandelbrot.Mandelbrot().mbrot_main(FRACTALS[sys.argv[1]], sys.argv[1])

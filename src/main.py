import sys

import julia_fractal, mbrot_fractal
import FractalInformation


FRACTALS = FractalInformation.FractalInformation().getDictionary()
FRACTAL_NAMES = ['mandelbrot', 'spiral0', 'spiral1', 'seahorse', 'elephants', 'leaf', 'fulljulia', 'hourglass', 'lakes']

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in FRACTAL_NAMES:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in FRACTAL_NAMES:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in FRACTAL_NAMES:
        print(f"\t{i}")
    sys.exit(1)

else:
    # Get the name of the fractal
    fractal = ''
    for i in FRACTAL_NAMES:
        if sys.argv[1] == i:
            fractal += i

    if FRACTALS[sys.argv[1]]['type'] == 'julia':
        julia_fractal.julia_main(FRACTALS[sys.argv[1]], fractal)

    elif FRACTALS[sys.argv[1]]['type'] == 'mandelbrot':
        mbrot_fractal.mbrot_main(FRACTALS[sys.argv[1]], fractal)

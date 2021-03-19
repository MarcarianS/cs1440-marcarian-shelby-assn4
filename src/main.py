import sys

import julia_fractal, mbrot_fractal


JULIAS = [ 'fulljulia', 'hourglass', 'lakes' ]
MBROTS = [ 'mandelbrot', 'spiral0', 'spiral1', 'seahorse', 'elephants', 'leaf' ]

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in JULIAS + MBROTS:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in MBROTS + JULIAS:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    all_of_the_fractals = MBROTS
    all_of_the_fractals.extend(JULIAS)
    for i in all_of_the_fractals:
        print(f"\t{i}")
    sys.exit(1)

else:
    fracal = sys.argv[1]
    if sys.argv[1] in JULIAS:
        julia_fractal.julia_main(sys.argv[1])
    elif sys.argv[1] in MBROTS:
        fratcal = sys.argv[1]
        mbrot_fractal.mbrot_main(fratcal)
        

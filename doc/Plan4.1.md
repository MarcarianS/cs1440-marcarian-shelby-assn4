# 0. From Problem Analyisys to Data Definitions

Transform the maintainable program into an easily extensible program.

Create new classes to store different color palettes (at least 3) and store each fractal's information in its own frac file. Create different files to store the algorithms for each kind of fractal (at least 3).
* Command line arguments are given to main.py, whic processes them
to decide what to do
* The fractal information file's path and palette name are sent to ImagePainter
* ImagePainter calls makeFractal() from FractalFactory
* makeFractal() reads the .frac file (don't enforce .frac) and creates a dictionary of information.
* Some of the information needs to be calculated. Do this in makeFrac if it's simple, antoher function if it gets messy.
* FractalFactory imports Fractal, uses polymorphism to call count for the correct fractal
* The iteration will be the return value of count, called in ImagePainter
* ImagePainter calls makePalette() from PaletteFactory
* paletteFactory creates a palette object from the palette and iterations of fractal
* Once Palette and Fractal are created, use their information/attributes to call the for loop that will .put the color on the canvas.



# 1. System Analysis

## main.py
* If there are an appropriate numebr of arguments given, main will
call Fractal Factory with the relative path to the .frac file

## Image Painter Class

## Fractal Class
* Has init and count methods, both raise an exception when called.
* This is an abstract class.

## Julia Class
* uses the fulljulia file
* overrides init and count
* count will be given a complex number and returns iterations

## Mandelbrot Class

## Phoenix Class

## Fractal Factory Class

## Palette Class

## Easter Palette Class
will use pastel pink, purple, blue, green, yellow, and orange
with black between. Overall 12 colors
palette : ffb0f8, d58ff, a8e1ff, a6ffa7, fffeb8, ffd699
is iteration returned is divisable by 12, take black
11, orange
10, black
9, yellow
etc

## Green scale/ St. Patrick Class
use shades from green to black to green to white.
range from #00ff00 to #002600
range from #002700 to #00ff00
range from #01ff01 to #e3ffe3

## Blurry Class
range fom white to black, increment by 256

## Palette Factory Class

# 2. Functional Examples


# 3. Function Template

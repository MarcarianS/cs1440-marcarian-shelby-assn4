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

## main.py
* If there are an appropriate numebr of arguments given, main will
call Fractal Factory with the relative path to the .frac file
* if 1 arg given, use default frac and palette
* if 2 arg give, use second one as frac file name, use default palette
* if 3 arg given, use second as frac file, third as palette
* if defaults are begin used, alert the user
* invalid files lets open() fail
* Invalid palettes rasies NotImplemeted exception

## Image Painter Class
* init method creates Tk window, canvas, and image. packs the canvas.
* Has one method paint, called from main.py, takes the frac path and palette name
* paint will call makeFractal(.frac path) from fractalFactory
* MakeFractal calls Fractals constructor, makeFractal should return the Fractal object to ImagePainter
* call PaletteFactory, creates a Palette object to reference later
* use the dictionary created in fractalFactory to get the complex number to send to count()
* ImagePainter will use Fractal.count() in a for loop.
* get the color from the palette object, .put() that color at the pixel.
* update the image every row
* After the picture is done, mainloop() keeps it open and a png file is written.

## Fractal Factory Class
* has a makeFractal() method that takes the path of the frac file 
* translates the .frac file into a dictionary. The 
dictionary contains:
	* type
	* pixles (width and height of the image)
	* axis length
	* pixelSize (calculated abs(maxX - minX) / pixels)
	* iterations
	* min (calc from centerX - (axis length / 2), centerY - axislen / 2)
	* max (centerX + (axis length / 2), centerY + asixlen / 2)
	* imageName
* Julia fractals only:
	* creal
	* cimag
## Fractal Class
* Has init and count methods, both raise an exception when called.
* This is an abstract class, empty

## Julia Class
* uses the fulljulia file's dictionary
* overrides init and count
* count will be given a complex number and returns iterations
* 

## Mandelbrot Class

## Phoenix Class


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

# 1. System Analysis

# 2. Functional Examples


# 3. Function Template

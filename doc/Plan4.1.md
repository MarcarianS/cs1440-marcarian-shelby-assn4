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
* Based of the 'type', use if then else to return type.type() object

## Fractal Class
* Has init and count methods, both raise an exception when called.
* This is an abstract class, empty

## Julia Class
* uses the fulljulia file's dictionary
* overrides init and count
* count will be given a complex number and returns iterations
* init will set self.thrshhold = 2 and the complex c = complex(creal, ciamg)
* count will take the complex number from creal, cimag and complex from the for loop in imagepainter
* It will also take the max iterations from the dictionary key 'iterations'

## Mandelbrot Class
* Very similar to Julia, except c = complex(0, 0)

## Phoenix Class
* Similar structure to Julia and Mbrot, different numbers and equation

## Palette Factory Class
* implements makePalette which takes the palette name from imagePainter
* Using if then else logic, creates a palette object by calling the correct palette.

## Palette Class
* has an init and getColor function, both abstract

## Easter Palette Class
will use pastel pink, purple, blue, green, yellow, and orange
with black between. Overall 12 colors
palette : ffb0f8, d58ff, a8e1ff, a6ffa7, fffeb8, ffd699
is iteration returned is divisable by 12, take black
11, orange
10, black
9, yellow
etc
* init will create a self.palette using those colors
* getcolor(n) returns the corressponding color

## Green scale/ St. Patrick Class
use shades from green to black to green to white.
range from #00ff00 to #002600
range from #002700 to #00ff00
range from #01ff01 to #e3ffe3
* similar implementation to Easter


# 1. System Analysis
## Main.py (Static)
* Input: command line arguments (strings)
* Internal Data:
	* if sys.argv length is 1, call ImagePainter.paint(defaultFractal, defaultPalette)
	* elif sys.argv length is 2, call ImagePainter.paint(sys.argv[1], defaultPalette)
	* elif sys.argv lenth is 3, call ImagePainter.paint(sys.argv[1], sys.argv[2])
	* else, print (too many arguemnts, only give a fractal and palette at most)
	* whenever a default is used, print a message.
* Output: Potential to print messages, calls paint from ImagePainter.
* Function Stub:
```
import sys
import ImagePainter

if len(sys.argv) == 1: 
	ImagePainter.paint(defaultFractal, defaultPalette)
elif len(sys.argv) == 2: 
	paint.(sys[1], defaultPalette)
elif len(sys.argv) == 3:
	paint(sys[1], sys[2]
else:
	print(Too many arguments: You can optionally give a fractal and a palette)
	sys.exit(1)
```


## ImagePainter (Static)

### Paint(fractalPath, paletteName)
* Input: strings, the path to the .frac file and the name of the palette class
* Internal Data: 
	* One named Constant BG = white
	* calls fractal = FractalFactory.makeFractal(fractalPath), makes a fractal object
	* iterations from the fractal dict are used to determine the size of the palette. 
	* call palette = PaletteFactory.makePalette(paletteName, paletteSize), makes a palette Object
	* use dictionary = fractal.getDict() to make variables for minX, maxX, minY, pixelSize, iterations, and pixels
	* create the window, canvas, and image
	* canvas.create_image, and canvas.pack()
	* use the for loop to determine x and y of the complex numebr to give to count
	* color = palette.getColor(count(complex(x, y)))
	* image.put the color in the right pixel
	* after each row, update() the window
	* write() the image to a png and call mainloop()
* Output: prints a message and creates a .png 
* Function Stub:
```
import Fractal, Palette Factories
import Tkinter
BG = '#ffffff'

fractal = FractalFactory.makeFractal(fractalPath)
fractalInfo = fractal.getDictionary()
paletteSize = fractalInfo['iterations']
palette = PaletteFactory.makePalette(paletteName, paletteSize)
imageSize = fracInfo[pixels]
window = Tk()
canvas = Canvas(window, width, height, bg)
image = PhotoImage(width, height)
canvas.create_image((imageSize / 2, imageSize / 2), image, normal)
canvas.pack()
pixelSize = fractalInfo[pixelSize]
for row in imageSize, 0, -1:
	for col in imageSize:
		x = fractalInfo[min][x] + col * pixelSize
		y = fractalInfo[min][y] + row * pixelSize
		color = palette.getColor(fractal.count(complex(x, y)))
		image.put(color, (col, imageSize - r)
	window.update()
image.write(fractalInfo[imageName].png)
print(wrote imageName)
mainloop()
```

## Fractal Factory (Static)

### makeFractal(path)
* Input: string, path to the file to read into a dictionary
* Internal Data:
	* If the file doesn't exist or otherwise fails to open(), let python crash
	* Read the file into a dictionary line by line. Lines must include:
		* type, centerx, centery, axislength, pixels, iterations.
	* If any of those aren't present or are the wrong data type, raise notimplementError
	* Check if julia or burning ship julia
		* must have creal and cimag
	* ignore empty lines and # lines
	* Other wise add the line up to : as the key and the word following the space as the value, both toLowerCase if string
	* Once the dictionary is created, use if logic on the 'type' to decide which Fractal to make.
	* return Fractal.Fractal(dictionary)
* Output: Fractal object, which one depends on the type from the config file
* Function Stub:
```
if path = 'defaultFractal'
	fileObj.open('mandelbrot.frac')
	printcreating a default fractal
else:
	fileObj = open("path")
dictionary = {}
for line in fileObj:
	if line.startsWith('#') or line.isspace()
		continue
	else:
		dictEntry = line.split(": ")
		if dictEntry[0] == type and not dictEntry[1].isNumeric()
			dictionary['type'] = dictEntry[1]
		elif dictEntry[0] == pixels and not dictEntry[1].contains"."
			dictionary['pixels'] = dictentry[1]
		etc for rest of lines
keys = [list the keys]
for key in keys
	if key ! in dictionary
		raise notImplementedError
if dictionary[type] == julie and creal or cimag not in dictionary
	raise notImplementedError
if type == julia
	return Julia.Julia(dictionary, complex(creal, cimag))
elif type == Mandelbrot
	return Mandelbrot.Mandelbrot(dictionary)
elif type == burningship
	return BurningShip.BurningShip(dictionary)
```

## Fractal (Nonstatic)

### init()
* Input:
* Internal Data: Raise error
* Output: Prints error
* Function Stub: 
```
raise NotImplementedError("Concrete subclass of Fractal must implemnt __init__")
```

### count(n)
* Input:
* Internal Data: Raise error
* Output: Prints error
* Function Stub:
```
raise NotImplementedError("Concrete subclass of Fractal must implemnt count")
```

## Julia (Nonstatic)

### init(dictionary, c)
* Input: dictionary of the config file, info, complex number -1, 0 
* Internal Data:
	* self.__dictionary = dictionary
	* self.__c = c
* Output: 
* Function Stub:
```
self.__dictionary = dictionary
self.__c = c

```

### count(n)
* Input: n the complex numeber based on what pixel is being counted for
* Internal Data:
	* for i in dictionary[iterations], n = n * n + sefl.__c
	* if abs of n > THRESHHOLD return i
	* else return iterations
* Output: integer iteration where the complex exceeded 2 or trended to infinity * Function Stub: 
``` 
for i in range(self.__dictionary[iterations] - 1): 
	n = n * n + self.__c
	if abs(n) > 2
		return i
return dictionary[iterations] - 1
```
## Mandelbrot (Nonsttic)

### init(dictionary)
* Input: dictionary of fractal information
* Internal Data: 
	* define dictionary attribute and c
* Output:
* Function Stub:
```
self.__dictionary = dictionary
self.__c = complex(0.0, 0.0)
```

### count(n)
* Input: complex numebr calculated from what pixel is being determined
* Internal Data:
	* use the manbrot equation to find when c goes over 2
* Output: the iteration where c exceeds 2
* Function Stub:
```
for i in range(dictionary[iterations] - 1):
	c = c * c + n
	if abs of c > 2
		return i
return dictionary[iterations]- 1
```

## BurningShip (Nonstatic)

### init(dictionary)
* Input: dictionary of fractal info
* Internal Data: initialize dictionary and complex c = (0.0, 0.0)
* Output:
* Function Stub:
```
self.__dictionary = dictionary
self.__c = complex(0.0, 0.0
```

### count(n)
* Input: complex number from ImagePainter
* Internal Data: use burning ship equation to find when c goes over 2
* Output: returns integer of the iteration that exceeded 2
* Function Stub: 
```
for i in range(dictionary[iterations] - 1)
        c = (abs(real(c)) + abs(imag(c)) * sqrt(-1)) ^ 2 - n
        if abs c > 2
                rturn i
return dictionary[iterations] - 1

```

## Palette Factory (Static)

### makePalette(paletteName, iterations)
* Input: paletteName, given from main, string. iterations, from fractal information, integer.
* Internal Data: 
	* if paletteName = defaultPalette, call Easter(iterations)
	* use elif to figure out if the palette is Easter or GreenScale, or invalid
	* if invalid, call notimplemented.
	* else return Palette.Palette(iterations)
* Output: returns a palette object to ImagePainter
* Function Stub:
```
if paletteName = defaultPalette
	return Easter.Easter(iterations)
elif paletteName = Easter
	return Easter.Easter(iterations)
elif paletteName = GreenScale
	return GreenScale.GreenScale(iterations)
else
	raise notimplemented error
```

## Palette (Nonstatic)

### init()
* Raise not implemented error
### getColor(n)
* Raise not implemented error

## Easter (Nonstatic)

### init(iterations)
* Input: iterations, the size of the color list
* Internal Data: 
	* define the list full of pastels with black between each
	* use iteratiosn to determine how many entrues are in the palette
* Output
* Function Stub:
```
originalColors =  [ffb0f8, 000000, d158ff, 000000, a8e1ff, 000000, a6ffa7, 000000, fffeb8, 000000, ffd699, 000000]
step = iterations / len(originalColors)
self.__palette = (list(ffb0f8.range_to(black, step)) + list(d158ff.range_to(black, step) + etc
for c in self.__palette:
	c.hex_l()
```

### getColor(n)
* Input: n is the integer index of the list to return
* Internal Data: 
	* return self.__palette[n]
* Output: return a color code in #rrggbb format.
* Function Stub:
```
return self.__palette[n]
```
## GreenScale (Nonstatic)

### init(iterations)
* Input: integer iterations determines the size of steps between each shade of green
* Internal Data:
	* define the list of colors for self.__palette with different shades of green
* Output: 
* Function Stub:
```
step = iterations / 4
self.__palette = list(green.range_to(002600, step) + list(002700.range_to(green, step) + etc
for c in palette:
	c.hex_l()
```
### getColor(n)
* Input: n is the integer index of the list to return
* Internal Data:
        * return self.__palette[n]
* Output: return a color code in #rrggbb format.
* Function Stub:
```
return self.__palette[n]
```

# 2. Functional Examples


# 3. Function Template

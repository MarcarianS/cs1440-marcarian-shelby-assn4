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

## mandel4 Class
* Similar structure to Julia and Mbrot, different numbers and equation

## Palette Factory Class
* implements makePalette which takes the palette name from imagePainter
* Using if then else logic, creates a palette object by calling the correct palette.

## Palette Class
* has an init and getColor function, both abstract

## Easter Palette Class
* will use pastel pink, purple, blue, green, yellow, and orange
* with black between. Overall 12 colors
* palette : ffb0f8, d58ff, a8e1ff, a6ffa7, fffeb8, ffd699
* creates a palette with steps between each color determined by number of iteratons
* init will create a self.palette using those colors
* getcolor(n) returns the corressponding color

## Green scale/ St. Patrick Class
* use shades from green to black to green to white.
* range from black to green
* range from #002600 to green
* range from #e3ffe3 to green
* range from white to green
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

## Fractal Factory (Module)

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
	dictionary = defaultFractal()
else:
	fileObj = open("path")
keys = [list the keys]
dictionary = {}
for line in fileObj:
	if line.startsWith('#') or line.isspace()
		continue
	else:
		dictEntry = line.split(": ")
		checkEntry = checkReqs(dictEnry, dictionary)
		dictionary[checkedEntry[0]] = checkedEntry[1]
close file
for key in keys
	if key ! in dictionary
		raise notImplementedError
if dictionary[type] == julie and creal or cimag not in dictionary
	raise notImplementedError
dictionary = updatedictionary(dictionary, path)

if type == julia
	return Julia.Julia(dictionary)
elif type == Mandelbrot
	return Mandelbrot.Mandelbrot(dictionary)
elif type == mandelbrot4
	return Manelbrot4.Mandelbrot4(dictionary)
```

### defaultFractal()
* Input: nothing
* Internal data:
	* print message to let the user know a default is being created
	* create a hardcoded dictionary of values and return it
* Output: fractal dictionary for mandelbrot
* Function Stub:
```
print(creating a default fractal
dictionary = {all mandelbrot info goes here}
return dictionary
```
### checkReqs(dictEntry, dictionary) 
* Input: dict entry is a list of the key value pair for 
the current line, dictionary is the info dictionary to update 
* Internal Data:
	* translate each key to lowercase, perform basic checks for each
	* if entry 0 and 1 of dictEntry are valid keys and values, add it to the dictionary
	* return the tuple of key and value, formatted to lowercase and integer or float
	* If the type is julia, check julia reqs as well. Assumes that type is higher in the file than creal and cimag.
* Output: return tuple
* Function Stub:
```
if dictentry = type and is not numeric
	return type, dictEntry[1]
if dictentry = pixels, is numeric, and has no decimal
	return pixels, int(dictentry[1]
so on for each required datafield
if type == julia
	return checkJuliaReqs(dictEntry)
else: raise not implemented error
```

### checkJuliaReqs(dictEntry)
* Input: list of possible key and value
* Internal Data: same as check Reqs
* Output: tuple of key and value pair
* Function Stub:
```
same as checkReqs, just for creal and cimag
```

### updateDictionary(dictionary, path)
* Input: dictionary that just holds the information from the file. Path that contains the imageName
* Internal Data:
	* set the final keys and values needed for each fractal
	* calculate pixelsize, mins and maxes, and gets just the image name with png.
* Output: returns the updated dictionary
* Function Stub: 
```
return {
type = type,
pixels = pixels,
axislength = axilength
pixelSize = axislength / pixels
Iterations = iterations
min: {x: centerx - axislength / 2, y: centerY - axislength / 2},
max: {x: centerx + axislength / 2, y: centerY + axislength / 2}, 
imagename = path.split("/")[-1].split(".")[0] + "png"
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

## Mandelbrot4 (Nonstatic)

### init(dictionary)
* Input: dictionary of fractal info
* Internal Data: initialize dictionary and complex c = (0.0, 0.0)
* Output:
* Function Stub:
```
self.__dictionary = dictionary
self.__c = complex(0.0, 0.0)
```

### count(n)
* Input: complex number from ImagePainter
* Internal Data: use burning ship equation to find when c goes over 2
* Output: returns integer of the iteration that exceeded 2
* Function Stub: 
```
for i in range(dictionary[iterations] - 1)
	c = c * c * c + n
        if abs c > 2
                rturn i
return dictionary[iterations] - 1

```

## Palette Factory (Module)

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
	return Easter(iterations)
elif paletteName = Easter
	return Easter(iterations)
elif paletteName = GreenScale
	return GreenScale(iterations)
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
self.__originalColors =  [ffb0f8,  d158ff,  a8e1ff,  a6ffa7,  fffeb8,  ffd699, 000000]
self.__step = iterations / len(originalColors)
self.__palette = self.__makePalette()
```
### __makepalette()
* Input : nothing
* Internal Data:
        * create an empty list
        * for color in original, add makeColor(color) >
        * return palette
* Ouput: list of hex colors
* Function Stub:
```
palette = []
for colorCode in originalColors
        palette += makeColors(colorCode)
return palette
```
### __makeColor(colorCode)
* Input: color code, string of hex
* Internal Data:
        * create Color object
        * create a list of color objects from the colo>
        * convert each entry to hex
        * return the color list
* Output: list of hex colors
* Function Stub:
```
color = COlor(colorCode)
colors = list(color.rangeto(green, slef.__step)
for i in range(lencolors)
        colors[i] = colors[i].hex_l
return colors
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
self.__originalColors = [black, 002600, e3ffe3, white]
self.__step = iterations / len(orignalColors) + 1
sel.f__palette = makePalette()

```

### __makepalette()
* Input : nothing
* Internal Data:
	* create an empty list
	* for color in original, add makeColor(color) to the list
	* return palette
* Ouput: list of hex colors
* Function Stub:
```
palette = []
for colorCode in originalColors
	palette += makeColors(colorCode)
return palette
```
### __makeColor(colorCode)
* Input: color code, string of hex
* Internal Data:
	* create Color object 
	* create a list of color objects from the color to green
	* convert each entry to hex
	* return the color list
* Output: list of hex colors
* Function Stub:
```
color = COlor(colorCode)
colors = list(color.rangeto(green, slef.__step)
for i in range(lencolors)
	colors[i] = colors[i].hex_l
return colors
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

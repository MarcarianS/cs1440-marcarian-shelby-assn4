
# Note on Testing folder
I'm sorry in advance, but the unit tests are a bit funky to run. I spoke with Professor
Falor about it and spent an unhealthy amount of time trying to get them to import properly, 
but python refuses to recognize my modules unless the tests are run in PyCharm or with 
the command 
```
$ PYTHONPATH=$PWD python runTests.py
```
from the src directory. Not pretty, but the only solution that works (short of doing away
with the Testing directory altogether and putting it all in src, which is not my favorite 
solution either).
Professor Falor told me that if I put a note
in here that whoever ends up grading this should see it, but I am sorry for the inconvenience!

# 0.  From Problem Analysis to Data Definitions

files needed: main.py, mbrot, julia, makePicture

- main will have a list or dictionary of the different fractal types
- depending on what name is entered into the command line, either mbrot class or julia class will be called
- each will have an iterative function, returns a number that is then sent to a function to choose a pixel color
- the color of the pixel function will return a color value to the paint/makepicture function
- the paint function will put the color on the specific pixel
- Update will show one row at a time
 
# 1.  System Analysis

## Main Class
- Import mandelbrot and julia
- contains if checks for command line arguments, import FracInfo to get the dictionary 
- sends sys.argv[1] to whichever fractal is appropriate

## FractalInformation Class
- defines the dictionary with the fractal names and important info
	- Important info being coordinates, axis length, its constant complex number, and whether it's julia or mbrot
- getDictionary will return the dictionary
- getFractal will return one of the fractals names

## Mandelbrot Class
- given a complex number determined from which fractal is being used
- returns the iteration from 0 to  size of the palette - 1 for which iteration gives the complex bigger than 2
- based on the computation of another complex  iteratively
- will have an originalComplex constant = (-1, 0)
- iterativeComplex is the one generated for each iteration

## Julie Class
- given a fractal, find the complex number that corresponds to each iteration
- for the iteration, return what iteration gives the complez number abs(greater than 2)
- iteration goes for as long as the size of the palette - 1
- original complex constant = (0, 0)

## Palette Class
- has an array Palette of N colors (96 for now)
- getColor returns color code at index given to it 
- getSize returns the length of the array

## ImagePainter Class
- creates everything to do with Tk and PhotoImage
- store pixels in PhotoImage
- create png for the picture
- this is where the color will be .put() for each pixel. 
### paint(index, row, col, imgsize)
```
color = palette.getCOlor(index)
img.put(color, (col, imageSize - row)
```
### update()
```
window.update()
```
# 2.  Functional Examples

## Main:

* Input: The name of a fractal from the command line (a string)
* Internal Data: 
	* Import sys, FractalInformation, Julia, Mandelbrot
	* create a fractal information object
	* if sys.argv is shorter than 2 strings ask the user to enter a fractal name and exit the program
	* if the user enters a name not in the fractal dict, ask them the enter a valid name and exit the program
	* In both cases, print a list of the valid fractal names
	* Otherwise, check if the fractal name has type julia or mandelbrot, and send it to the appropriate module.
* Output: Nothing, just a runner class
* Function Stub:
```
fractals = fractalInfo.fractalInfo.getDictionary()
if len(sys.argv) < 2
	print(Please give the name of a fractal)
	for i in fractals
		print the fractal name
	sys.exit
elis sys.argv[1] not in fractals:
	print(not a valid fractal)
	print(Please enter a valid fractal name from teh following:)
	for i in fractals:
		print fractal name
	sys.exit
else:
	if fractals[sys.argv[1]][type] == julia:
		Julia.Julia().juliamain(fractals[sys.argv[1]], sys.argv[1])
	elif type == mandelbrot:
		Mandelbrot.Mandelbrot().mbrotmain(fractals[sys,argv[1]], sys.argv[1])
```
## Julia and Mandelbrot
* Import: sys, tkinter mainloop, time, ImagePainter, FractalInformation
* global constants are imageSize=512 and white='#ffffff'

### getIteration(c, z, paletteSize)
* Input: c is a complex gotten from ImagePainter.paint, z is the constant
	* z is (0.0, 0.0) for mbrot 
	* z is (-1.0, 0.0) for Julia)
* Internal Data: 
	* Iterate through paletteSize
	* if abs(z) > 2 return i
	* if it never reaches 2, return paletteSIze - 1
* Output: integer i, index at which z exceeded 2
* Function Stub (MandelBrot): 
```
for i in range(paletteSize):
	z = z * z + c 
	if abs(z) > 2:
		return i
return paletteSize - 1
```
* Function Stub (Julia):
```
for i in range(paletteSize):
	c = c * c + z
	if abs(c) > 2
		return i
return 77
```

### pixelsWrittenSoFar(rows, cols)
* Input: rows and columns, both integers * Internal Data: 
mulitplies rows by columns and reports to console * Output: 
returns number of pixels and prints messsage to console * 
Functions Stub:
```
pixles = rows * cols
print({pixels} have been printed so far)
return pixels
```

### main(fractalInfo, fractalName)
* Input: fractalInfo is the sub dictionary containing info for one fractal, fractalName is the string form of the fractal's name.
* Internal Data: 
	* Creates an image painter object with the size and background determined by the global constants
	* takes the time before and after the image is rendered
	* calls __makePicture and prints a message when it's done
	* calls image.writePNG to create a png file of the rendered image
	* calls the mainloop to keep the image open
* Output: Nothing
* Function Stub:
```
image = ImagePainter.ImagePainter(imageSize, white)
minX = fractalInfo[centerX] - fractalInfo[axisLen] / 2
maxX = fractalInfo[centerX] + fractalInfo[axisLen] / 2
minY = fractalInfo[centerY] - fractalInfo[axisLen] / 2
z = fractalInfo[z]
paletteSize = Palette.getSize()

pixelSize = abs(maxX - minX) / imageSize

before
for row in IMGSIZE, 0 , -1
	for col in IMGSIZE
		x = minX + col * pixelSize
                y = minY + row * pixelSize
		index = getIteration(complex(x, y), z, paletteSize)
		ImagePainter.paint(index, row, col, IMGSize)
	ImagePainter.update()
after

print( done in (before - after) seconds) to sys.stderr
image.writePNG(fractalName)
print(wrote fractalName to fractalName.png)

print(close the image window to end the program)

mainloop()
```


## ImagePainter
* Import Tk, Canvas, PhotoImage from tkinter, import Palette
### ImagePainter(IMGSIZE, bg)
* Input: IMG_SIZE is the integer that gives the size of the window and therefore image in pixels. bg is background color, given as a string.
* Internal Data:
	* define window, canvas, and image
	* pack the canvas and use canvas to create an image from tkinter
* Output: Nothing 
* Function Stub:	
```	
__window = Tk()
__canvas = Canvas(__window, width=IMGSIZE, height=IMGSIZE, bg=bg)
__canvas.pack()
__image = PhotoImage(width=IMGSIZE, height=IMGSIZE)
__canvas.create_imgae((IMGSIZE /2, IMGSIZE/2), image=__image, state='normal')
```

### paint(index, row, col, IMGSIZE)
* Input: index, row, and col are integers determined by what pixel is being colored. IMGSIZE is the integer size of the window.
* Internal Data: 
	* color is determined by palette at index given
	* __image will .put() the color at the correct pixel.
* Output: Returns nothing, renders the image.
* Function Stub:
```

color = palete.getColor(index)
__image.put(color, col, IMGSize - row)

```

### update():
* Input: Nothing
* InternalData: self.__window.update()
* Output: Nothing
* Function Stub:
```
self.__window.update()
```

### writePNG(name)
* Input : name of fractal as a string
* Internal Data: 
	* writes the fractal image to a png with its name
* Output: creates a PNG file
* Function Stub: 
```
self.___image.write(f"{name}.png")
```
## FractalInformation

### Constructor
* Input: Nothing
* Internal Data: 
	* creates an instance of the dictionary
* Output: Nothing
* Function Stub: Initializes the dictionary of fractals

### GetDictionary()
* Input: Nothing
* INternal Data: 
	* return self.fractalDictionary
* Output: returns dictionary
* Function Stub: 
``` 
return fractal dictionary
```

### getFractal(key)
* Input: key as a string. this is the name of the fractal to return
* Internal data:
	* If the key is in the dictionary, return the key
* Output: key as a string
* Function Stub: 
```
if key in fractalDictionary:
	return key
```


## Palette

### Constructor()
* Input: Nothing
* Internal Data: defines list of colors as strings
* Putput: Nothing
* Function Stub: Defines palette

### getSize()
* Input: Nothign
* INternal Data: 
	* returns size of the list
* Output: size of the list, integer
* Function Stub:
```
return len(self.__palette)
```

### getColor(index)
* Input: index of the list as an integer to return
* Internal Data: 
	* return palette at index givem
* Output: string at the index provided
* Function Stub:
```
return self.__palette[index]
```

 
# 3.  Function Template



# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

- If the image rendered comes out as a solid background color, make sure you're checking the right complex against 2
	- Julia should compare abs of c
	- mbrot should compare abs of z
- If mandelbrot looks way too detailed on teh edges and looks smudged to the left
	- make sure you're passing the correct variables to getIteration (second one should be z, not x)
- Python plays nicer with imports that are formatted "from... import..."
	- this is not working for the Testing folder
	- to run tests, see top of document

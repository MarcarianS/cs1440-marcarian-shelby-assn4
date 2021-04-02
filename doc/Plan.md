
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
### paint(minX, minY, pixelSize)
```for row in imagesize counting backwards
	for col in imagesize
		x = minX + col * pixelSize
		y = minY + row * pixelSize
		color = calculateColor(complex(x, y))
		img.put(color, (col, imageSize - row)
```
### calculateColor(complex)
```
z = complex(-1.0, 1.0) #for julia
for i in range(palette.getSize())
	z = z * z + complex
	if abs(z) > 2:
		return Palette.Palette.getColor(i)
return palette.palette.getColor(Palette.palette.getSize() - 1)	
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
### __makePicture(fractalInfo, image)
* Input: fractal info is the sub dictionary of fractalInformation that has info on one specific fractal. Image is the image object
* Internal Data: 
	* defines minimum x and y and maximum x, which are used to find the iterative complex number
	* defines z, which is the constant complex number
	* calculates pixleSize
	* Calls paint from the ImagePainter class with all the information just defined
* Output: Nothing, just calls the ImagePainter 
* Function Stub:
```
minX = fractalInfo[centerX] - fractalInfo[axisLen] / 2
maxX = fractalInfo[centerX] + fractalInfo[axisLen] / 2
minY = fractalInfo[centerY] - fractalInfo[axisLen] / 2
z = fractalInfo[z]

pixelSize = abs(maxX - minX) / imageSize
image.paint(minX, minY, PixSize, imageSize, z
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

before
makePicture(fractalInfo, image)
after

print( done in (before - after) seconds) to sys.stderr
image.writePNG(fractalName)
print(wrote fractalName to fractalName.png)

print(close the image window to end the program)

mainloop()
```
# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


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

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**

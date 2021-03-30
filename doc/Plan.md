
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
- defins the dictionary with the fractal names and important info
- getDictionary will return the dictionary
- getFractal will return one of the fractals with its info

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
- returns color code at index given to it (called from imagePainter

## ImagePainter Class
- creates everything to do with Tk and PhotoImage
- store pixels in PhotoImage
- create png for the picture
- this is where the color will be .put() for each pixel. 


# 2.  Functional Examples

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


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

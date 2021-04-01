# Code Smells Report

## Smells

*       Where you found it (filename + line number)
*       Copy the offensive code
*       Explain why the smell is a problem
*       Describe how you fixed it

# Where: main.py line 11 and 18
* Copy: ```     for i in JULIAS + MBROTS:
        print(f"\t{i}")```
	``` all_of_the_fractals = MBROTS
	    all_of_the_fractals.extend(JULIAS)
	    for i in all_of_the_fractals:
        print(f"\t{i}")```
* Why: Alternative Functions 
	* Not functions, but there are two ways to iterate throught the two lists in main.py
* Remedy: Make Julie and Mbrots lists into one list and just use for i in...

# Where: julie Fractal line 23
* Copy: ```# Here 76 refers to the number of colors in the palette
    for i in range(78):```
* Why: Comment lies, magic number
* Remedy: delete the comment, change range to len(grad) so it self documents

# Where: julie fractal line 27 and 30
* Copy: ```if abs(z) > 2:
           return grad[i]  # The sequence is unbounded
           z += z + # 
TODO: One of these return statements makes the program crash sometimes
    return grad[77]         # Else this is a bounded sequence
    return grad[78]```
* Why: Dead code
* Remedy: delete z += z + c and return grad[78]

# Where: julie fractal line 19
* Copy:```global grad
    global win
```
* Why: unnecessary globals
* Remedy: Make grad a local variable to makePicture, pass in as argument everywhere else it's used

Only use win in main


# Where: julie fractal lines 55 56 159
* Copy: all are copies of already defined globals
* Why: dead Code
* Remedy: delete them

# Where: julie fractal line 33
* Copy: ```getFractalConfigurationDataFromFractalRepositoryDictionary```
* Why: ridiculous method name
* Remedy: rename to getFractalName

# Where: julie fractal line 42-46
* Copy: ```  for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key
```
* Why: clunky code
* Remedy: rewrite to if name in dictionary, return dictionary[name]

# Where: julie fractal, all over
* Copy: random globals everywhere
* Why: messy code, confusing to look through
* Remedy: put all globals at top of document before deciding what to do to them

# Where: julie fractal line 74
* Copy: canvas.pack()
* Why: dead code
* Remedy: only call pack once

# Where: julie fractal line 79
* Copy:```    area_in_pixels = 512 * 512```
* Why: dead code
* Remedy: this varaible is never used

# Where: julie fractal line 87
* Copy:```    fraction = int(512 / 64)```
* Why: dead code
* Remedy: fraction is never used, delete it

# Where: julie fractal line 153
* Copy: WHITE = '#ffffff'
* Why: bad global
* Remedy: define white at the top of the program as a constant

# Where:julie fractal line 161
* Copy:	```b4 = time()
    win = Tk()```
* Why: bad variable names
* Remedy: change b4 to before, win to window

# Where: julia fractal line 156
* Copy:```def julia_main(i):```
* Why: ambiguous parameter
* Remedy: rename i to fractalName

# Where: julia fractal line 171
* Copy:```    photo.write(i + ".png")```
* Why: call photo.write twice; why are there two?
* Remedy: delete the second one and see what happens

# Where: Julia fractal line 51
* Copy:```def makePicture(f, i, e)```
* Why: dead parameter
* Remedy: delete i and e from parameter list

# Where: mbrot fractal line 12
* Copy: # This color palette contains 100 color steps.
* Why: incorrect comment, palette has 96 colors
* Remedy: delete the unnecessary comment

# Where: mbrot fractal line 13...
* Copy: the pallete list
* Why: it is the same as the julia palette. lots of the code is replicated
* Remedy: create palette class and store it there

# Where: mbrot fractal line 33
* Copy:```
z = 0
seven = 7.0
TWO = sqrt(4)```
* Why: useless code
* Remedy: delete seven and TWO, remove math from import block

# Where: mbrot fractal line 42
* Copy: global z
* Why: global could just be a parameter to colorOfTheOixel
* Remedy: remove this line, add z to the parameter listhjb

# Where: mbrot fractal line 43
* Copy: #z0
* Why: TMI comment
* Remedy: code is self documenting, obviously z is just 0

# Where: mbrot fractal line 45
* Copy: ```  global MAX_ITERATIONS
    global i
```
* Why: global variables
* Remedy: make them into parameters, i is never defined used so delete it

# Where: mbrot fractal line 50
* Copy:``` global TWO
        if abs(z) > TWO:
            z = float(TWO)
            return palette[i] ```
* Why: global and dead code
* Remedy: remove TWO and the line defining z

# Where: mbrot line 55
* Copy:```  return palette[MAX_ITERATIONS - 1]   # Indicate a bounded sequence
    return palette[MAX_ITERATIONS]```
* Why: dead code
* Remedy: delete the second return statement

# Where: mbrot line 72, julia line 61
* Copy:```    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
```
```    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))```
* Why: two ways to do the same thing. 
* Remedy: change julia to match mbrot, remove maxy. It is never used.

# Where: mbrot line 78
* Copy:```    canvas = Canvas(window, width=512, height=512, bg='#ffffff')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 512
```
* Why: magic numbers
* Remedy: have a named constant WINDOW_SIZE = 512

# Where: mbrot line 86
* Copy:```  portion = int(512 / 64)
    total_pixels = 1048576```
* Why: dead code, never use variables
* Remedy: delete both of them

# Where: mbrot line 96
* Copy:```
def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels```
* Why: disorganised code; not immediately obvious that this is needed for the tests
* Remedy: move the function to the testing module or delete, the test is redundant anyway.

# Where: main.py line 11
* Copy:``` for i in JULIAS + MBROTS```
* Why: Inconsistent with rest of code
* Remedy: for i in mbrots and julias to match the other if condition

# Where: main.py line 23
* Copy: ```fratcals = sys.argv[1]```
* Why: dead code, never used
* Remedy: delete it

# Where: Julia line 55, 63- 67
* Copy:``` min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))
```
* Why: Bad varaible name 'f'
* Remedy: rename f to fractalInfo

# Where: Julia line 70
* Copy:```canvas = Canvas(window, width=512, height=512, bg=WHITE)```
* Why: Magic numbers
* Remedy: create named constant SIZE=512

# Where: mbrot line 44
* Copy:``` MAX_ITERATIONS = len(palette)

    for i in range(MAX_ITERATIONS):```
* Why: Inconsistent with julia.py
* Remedy: delete max iterations, make it fo ri in range len(palette)

# Where:
* Copy:
* Why:
* Remedy:

# Where:
* Copy:
* Why:
* Remedy:

# Where:
* Copy:
* Why:
* Remedy:


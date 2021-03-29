# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each instance of a code smell you find in the starter code report:

*	Where you found it (filename + line number)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you fixed it

These are the code smells that you can expect to find in the starter code.

0.  Dead Code
    * A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
1.  Magic Numbers
    * Numeric literals that appear in critical places but without any apparent meaning
    * "When I see the number `214` here, does it have the same meaning as the `214` over there?"
2.  Global Variables
    * A global is being used to avoid passing a parameter into a function
    * A global is being used to return an extra value from a function
3.  TMI Comments (Too Much Information)
    * A function or method is filled with many explanatory comments
4.  Too Long Parameter List
    * More than three or four parameters for a method
5.  Too Long Function/Method
    * A method contains too many lines of code
    * Generally, any method longer than ten lines should make you start asking questions
6.  Complex decision trees
    * Long or deeply nested trees of `if/elif/else`
    * Complex `switch` operators
7.  Shotgun Surgery
    * Making any modifications requires that you make many small changes to many different functions/classes
8.  Alternative Classes/Functions with Different Interfaces
    * Two classes perform identical functions but have different method names
    * Two functions perform identical functions but have different names
    * Two functions perform identical functions but take different parameters
9.  Spaghetti Code
    * Lots of meandering code without a clear goal
    * Many functions/objects used in inconsistent ways
    * All code is contained in one giant function/method with huge `if/else` branches
    * "It would be easier to rewrite this than to understand it"

Other code smells may also be identified; list them as well.


## Smells

*       Where you found it (filename + line number)
*       Copy the offensive code
*       Explain why the smell is a problem
*       Describe how you fixed it

* Where: main.py line 11 and 18
* Copy: ```     for i in JULIAS + MBROTS:
        print(f"\t{i}")```
	``` all_of_the_fractals = MBROTS
	    all_of_the_fractals.extend(JULIAS)
	    for i in all_of_the_fractals:
        print(f"\t{i}")```
* Why: Alternative Functions 
	* Not functions, but there are two ways to iterate throught the two lists in main.py
* Remedy: Make Julie and Mbrots lists into one list and just use for i in...

* Where: julie Fractal line 23
* Copy: ```# Here 76 refers to the number of colors in the palette
    for i in range(78):```
* Why: Comment lies, magic number
* Remedy: delete the comment, change range to len(grad) so it self documents

* Where: julie fractal line 27 and 30
* Copy: ```if abs(z) > 2:
           return grad[i]  # The sequence is unbounded
           z += z + # 
TODO: One of these return statements makes the program crash sometimes
    return grad[77]         # Else this is a bounded sequence
    return grad[78]```
* Why: Dead code
* Remedy: delete z += z + c and return grad[78]

* Where: julie fractal line 19
* Copy:```global grad
    global win
```
* Why: unnecessary globals
* Remedy: Make grad a local variable to makePicture, pass in as argument everywhere else it's used

Only use win in main


* Where: julie fractal lines 55 56 159
* Copy: all are copies of already defined globals
* Why: dead Code
* Remedy: delete them

* Where: julie fractal line 33
* Copy: ```getFractalConfigurationDataFromFractalRepositoryDictionary```
* Why: ridiculous method name
* Remedy: rename to getFractalName

* Where: julie fractal line 42-46
* Copy: ```  for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key
```
* Why: clunky code
* Remedy: rewrite to if name in dictionary, return dictionary[name]

* Where: julie fractal, all over
* Copy: random globals everywhere
* Why: messy code, confusing to look through
* Remedy: put all globals at top of document before deciding what to do to them

* Where: julie fractal line 74
* Copy: canvas.pack()
* Why: dead code
* Remedy: only call pack once

* Where: julie fractal line 79
* Copy:```    area_in_pixels = 512 * 512```
* Why: dead code
* Remedy: this varaible is never used

* Where: julie fractal line 87
* Copy:```    fraction = int(512 / 64)```
* Why: dead code
* Remedy: fraction is never used, delete it

* Where: julie fractal line 131...
* Copy:```f = {
        'fulljulia': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  4.0,
            },
```
* Why: bad variable name
* Remedy: rename f to fractalDict

* Where: julie fractal line 153
* Copy: WHITE = '#ffffff'
* Why: bad global
* Remedy: define white at the top of the program as a constant

* Where:julie fractal line 161
* Copy:	```b4 = time()
    win = Tk()```
* Why: bad variable names
* Remedy: change b4 to before, win to window

* Where: julia fractal line 156
* Copy:```def julia_main(i):```
* Why: ambiguous parameter
* Remedy: rename i to fractalName

* Where: julia fractal line 171
* Copy:```    photo.write(i + ".png")```
* Why: call photo.write twice; why are there two?
* Remedy: delete the second one and see what happens

* Where: Julia fractal line 51
* Copy:```def makePicture(f, i, e)```
* Why: dead parameters
* Remedy: delete i and e from parameter list

* Where: mbrot fractal line 12
* Copy: # This color palette contains 100 color steps.
* Why: incorrect comment, palette has 96 colors
* Remedy: delete the unnecessary comment

* Where: mbrot fractal line 13...
* Copy: the pallete list
* Why: it is the same as the julia palette. lots of the code is replicated
* Remedy: combine julia and mbrot

* Where: mbrot fractal line 33
* Copy:```
z = 0
seven = 7.0
TWO = sqrt(4)```
* Why: useless code
* Remedy: delete seven and TWO, remove math from import block

* Where:
* Copy:
* Why:
* Remedy:

* Where:
* Copy:
* Why:
* Remedy:

* Where:
* Copy:
* Why:
* Remedy:

* Where:
* Copy:
* Why:
* Remedy:





# Fractal Visualizer User Manual

## Running the Fractal Visualizer

* To run the program, navigate to the src folder containing main.py of the project and run the following commands in your Command Line:
	* python main.py [FRACTAL NAME]

## What You Should See

### Valid Fractal Names

* If you have entered a fractal name recognized by the program, an image of that fractal should begin printing to the screen automatically.
* The fractal will appear line by line, from top to bottom.
* The image window will remain open until you close it, and the command line will remind you of that with a short message.

### Invalid Fractal Names

* If you have entered a fractal name that the program does not recognize, an error message will print to the screen.
* You should see a message similar to the following: 
	* ERROR: [YOUR FRACTAL] is not a valid fractal.
	* Please choose one of the following:
	* mandelbrot
	* spiral0
	* spiral1
	* seahorse
	* elephants
	* leaf
	* fulljulia
	* hourglass
	* lakes
* After reporting the message, the program will close.

### No Fractal Name Given

* If you do not enter anything after main.py, the program will remind you of the valid fractals and close.



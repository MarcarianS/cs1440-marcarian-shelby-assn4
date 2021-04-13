# Fractal Visualizer User Manual

## Running the Fractal Visualizer

* To run the program, navigate to the src folder containing main.py of the project and run the following commands in your Command Line:
	* python main.py [FRACTAL PATH [PALETTE NAME]]
* Fractal Path is the path from your current working directory to your fractal configuration file. Options include:
	* No fractal specified (will print the default Madelbrot Fractal)
		* Note: If no fractal is specfied, you cannot specify a palette, or the program will attempt to read the palette file as a fractal configuration file.
	* mandelbrot.frac
	* fuljulia.frac
	* burningship.frac
		* Note: for any file path given, remember to enter the path from your current working directory to these files. 
* Palette Name is the name of the Palette you want to run. Options include:
	* No palette specified (will choose the default palette, Easter)
	* Easter
	* GreenScale

## What You Should See

### Valid Fractal Names

* If you have entered a valid fractal path recognized by the program, an image of that fractal should begin printing to the screen automatically.
* The fractal will appear line by line, from top to bottom.
* The image window will remain open until you close it.
* A message will print telling you the name of the .png file your image was written to.

### Invalid Fractal Names

* If you have entered an invalid file or incorrect file path, the file will fail to open.
* After reporting the message, the program will close.

### Invalid Fractal Configurations

* If the file your provided path leads to is not a valid fractal configuration, a NotImplementedError and close the program.

### Invalid Palette Name

* If you enter a palette option that is not blank, Easter, or GreenScale, a NotImplementedError will be raised and the program will quit.


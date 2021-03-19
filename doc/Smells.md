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

*TODO: write your report here*

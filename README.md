# Color_Console

This module is used to change the color of text and background of the python console designed for Windows Operating System.

"from Color_Console import color" statement is used to import color function from Color_Console module.

### The permitted colors are:
* black
* blue
* green
* aqua
* red
* purple
* yellow
* white
* gray
* light blue
* light green
* light aqua
* light red
* light purple
* light yellow
* bright white

**None of the arguement are case sensitive. Text color and background color cannot be the same.**

### "color ( text , bg , delay , repeat ) " is how this function can be called in a program.
color function is used to change the text color and background color of the python console.

**"text"** is used to specify the color of the text.
**"bg"** is used to specify the color of the background.
#### **Note that both background color and text color can't be the same.**

If a **list** of permitted colors is passed to either "text" or "bg", the colors change in accordance to their position in the list.
"delay" parameter is used to specify the time between two transitions.The default value is set to 0.67 seconds which can be changed.
"repeat" parameter is used to specify the number of times the list of colors has to be repeated. The default value is -1 which makes the color transition occur indefinitely.
"delay" and "repeat" are optional parameters.
### Eg:
#### color( ['purple','black','red','blue'] , 'white' ) will result in text color changing from purple to black and so on with background color as white.
#### color( 'white' , ['purple','black','red','blue'] ) will result in background color changing from purple to black and so on with text color as white.

When the parameters of both "text" and "bg" are lists, the color transition is as follows:
### Eg:
####    color(['green','black','red'],['blue','aqua','bright white'])

**This will result in:
green text with blue         background
black text with aqua         background
red   text with bright white background**
in which the color transition takes 0.67 seconds and this is repeated indefinitely since repeat value is set to a default of -1.
Note that if the size of two lists are different, an error will be thrown.

**If the above code is not working try passing the arguements with their parameter names**
**Eg:**
**color(text=['green','black','red'],bg=['blue','aqua','bright white'],delay=0.5,repeat=5)**

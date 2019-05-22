import time
import os
__li1__=["blue","green","black","purple","blue","red"]

def __lidict__(dict):
    return([i for i in dict],[dict[j] for j in dict])

def __cmd__(command):
    os.system(command)

__color_dict__={
"black":0,
"blue":1,
"green":2,
"aqua":3,
"red":4,
"purple":5,
"yellow":6,
"white":7,
"gray":8,
"light blue":9,
"light green":"A",
"light aqua":"B",
"light red":"C",
"light purple":"D",
"light yellow":"E",
"bright white":"F",
}

def __caps__(phrase):
    return(phrase.lower())

def __C__(text_color,bg_color):
    if(text_color==bg_color):
        print("Your text color and background color are the same")
        raise AssertionError
    else:
        pass
    try:
        __cmd__("color {0}{1}".format(__color_dict__[bg_color.lower()],__color_dict__[text_color.lower()]))
    except Exception as e:
        print(e)
        print("""
        This color combination is unavailable.
        To know more about the color combinations for color and ctext use the following fucntion:
        help()
        ;)
        """)

def __installationCheck__():
    try:
        import colorama
        Module_1=True
    except Exception:
        Module_1=False
    try:
        import termcolor
        Module_2=True
    except Exception:
        Module_2=False
    return(1 if (Module_1 & Module_2)==True else 0)

def __installModules__():
    try:
        __cmd__("pip install colorama")
        __cmd__("pip install termcolor")
    except Exception:
        pass

def __ctextInitialization__():
    n=1
    while(__installationCheck__()!=1):
        __installModules__()
        if(n>3):
            print("This module consists auto-pip package installation yet unable to download 'colorama' and 'termcolor'")
            print("Try switching on your internet connection or download those two modules via pip manually")
            raise ModuleNotFoundError
            break
        n+=1
    return

def __ctxt__(String,text,bg="black"):
    __ctextInitialization__()
    from colorama import init
    from termcolor import colored
    init()
    try:
        if(bg.lower()=="black"):
            print(colored('{0}'.format(String),'{0}'.format(text)))
        elif(text.lower()=="black"):
            print("Black text not possible!!")
        else:
            print(colored('{0}'.format(String), '{0}'.format(__caps__(text)), 'on_{0}'.format(__caps__(bg))))
    except Exception as e:
        print(e)
        print("The given colour combination is not possible")
        print("""
        The possible color combinations for ctext is
        RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE for text color
        and
        RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE for background color""")
        raise AssertionError

def hackerMan():
    color('light green','black')

def color(text="bright white",bg="black",delay=0.67,repeat=-1,dict={}):
    delay=int(delay)
    repeat=int(repeat)
    #If a dictionary is passed.
    if(dict!={}):
        text,bg=__lidict__(dict)
        if((len(dict)!=len(text))&(len(dict)!=len(bg))):
            print("A color in dictionary key cannot be present in the dictionary as a value\nDon't mix keys and values of a dictionary\n:(")

    #both are not lists and hence usual coloring is done !!
    if(type(text)!=type([]))&(type(bg)!=type([])):
        __C__(text,bg)

    #both are lists with only one color and hence are equivalent to the first if statement !!!
    elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)==1)&(len(bg)==1):
        __C__(text[1],bg[1])

    #both are list but number of elements in both of them are not equal !!!
    elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)!=len(bg)):
        print("Length of the two lists are different !!")
        return


    elif(type(text)==type([]))&(type(bg)!=type([])):
        n=1
        while(1):
            for color in range(len(text)):
                __C__(text[color],bg)
                time.sleep(delay)
            if(n>=repeat)&(repeat!=-1):
                break
            n+=1


    elif(type(text)!=type([]))&(type(bg)==type([])):
        n=1
        while(1):
            for color in range(len(bg)):
                __C__(text,bg[color])
                time.sleep(delay)
            if(n>=repeat)&(repeat!=-1):
                break
            n+=1

    elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)==len(bg)):
        n=1
        while(1):
            for color in range(len(text)):
                __C__(text[color],bg[color])
                time.sleep(delay)
            if(n>=repeat)&(repeat!=-1):
                break
            n+=1


    else:
        try:
            __C__(text,bg)
        except Exception as e:
            print(str(e))
            print("""
            Maybe your arguement was not a list, dictionary or a string.
            Try again ;)
            """)       # No need to hide

def help(c=True):
    print('''

    COLOR CONSOLE 10.0
--------------------------------
This module is used to change the color of text and background of the python console designed for 'Windows Operating System.'
===================
What's New ?
=> Easier importing of functions.
=> Functions updated to work with Dictionaries.
=> 4 more functions added.
=> Automatic package installation for unavailable libraries.
=> Arguements are Case Insensitive.
=> Increased error tolerance.
===================
Importing Functions:
'from Color_Console import *' statement is used to import all necessary functions from Color_Console module.
This version contains the following functions which we'll be discussing shortly.
⦿ color()
⦿ ctext()
⦿ transTime()
⦿ hackerMan()
⦿ help()
===================
Color()
--------------------------------
'color()' is used to change the text color and background color of the whole python console.
'color ( text = "bright white" , bg = "black" , delay = 0.67 , repeat = -1 , dict = {} )' is the function header.
'text' is used to specify the color of the text.
'bg' is used to specify the color of the background.
The permitted colors are:
1.  Black
2.  Blue
3.  Green
4.  Aqua
5.  Red
6.  Purple
7.  Yellow
8.  White
9.  Gray
10. Light Blue
11. Light Green
12. Light Aqua
13. Light Red
14. Light Purple
15. Light Yellow
16. Bright White
None of the arguements are case sensitive. Text color and background color cannot be the same.
--------------------------------
If a list of permitted colors is passed to either 'text' or 'bg', the colors change in accordance to their position in the list.
--------------------------------Eg:
# Constant background color with altering text color:
li = [ 'black','bright white' ]
print("Hello World !")
color( li , 'aqua' )
# This will make the text color of the console change to black and bright white alternatively and indefinitely
# with it's background color set to aqua
--------------------------------
--------------------------------Eg:
# Constant text color with altering background color:
li = [ 'black','bright white' ]
print("Hello World !")
color( 'aqua' , li )
# This will make the background color of the console change to black and bright white alternatively and indefinitely
# with it's text color set to aqua
--------------------------------
===================
'delay' parameter is used to specify the time between two transitions. The default value is set to 0.67 seconds which can be changed.
--------------------------------Eg:
# Changing color transition time:
li = [ 'black','bright white' ]
print("Hello World !")
color( 'aqua' , li , delay = 1 )
# and hence the color transition would take 1 second.
--------------------------------
===================
'repeat' parameter is used to specify the number of times the list of colors has to be repeated. The default value is -1 which makes the color transition occur indefinitely. Note that if color transition is set to indefinite, the program will not move further ( The code next to it will not be executed ! ). 'repeat' parameter would allow the code to proceed once the list is iterated the given number of times. Time taken for this is dependent on both 'delay' and 'repeat'.
--------------------------------Eg:
# repeating the color transition only certain number of times
li = [ 'black','bright white' ]
print("Hello World !")
color( 'aqua' , li , delay = 1 , repeat = 2 )
# The transition will be repeated two times with a time delay of 1 second each and hence would take 4 seconds
# since the number of elements in the list is 2.
--------------------------------
Total time required to complete transition can be found out by using 'transTime()' which will be explained later.
'delay' and 'repeat' are optional parameters.
===================

When the parameters of both "text" and "bg" are lists, the color transition is as follows:
--------------------------------Eg:
# When both text and bg recieve arguements that are of list type,
# the corresponding text and bg colors are used as they are iterated
print("Hello World")
color( ['green','blue'] , ['black','bright white'] )
# This would result in a console with the following text and bg color which repeats indefinitely
# green text color with black as bg color
# blue text color with bright white as bg color
--------------------------------
Note that if the size of two lists are different, an error will be thrown.**
===================
A dictionary with valid color combinations can be passed to **'dict'** to get an output similar to the previous one using two lists.
--------------------------------Eg:
# Passing dictionary to color()
Dictionary={
'green' : 'black' ,
'blue' : 'bright white'
}
color( dict = Dictionary )
# This output is similar to the previous one.
--------------------------------
Limitations in passing a dictionary:
A color in the key cannot be present in the value. So Don't mix the keys and values in a dictionary.
Reminder: 'dictionary ={ key1 : value1 , key2 : value2 }' Dictionary consists of key:value pairs
--------------------------------Eg:
Dictionary={
'green' : 'black' ,
'black' : 'bright white'
}
print("Hello World")
color( dict=Dictionary )
# This code would throw an error since 'black' is both in keys and values of the dictionary.
--------------------------------
--------------------------------Eg:
Dictionary={
'red'   : 'bright white',
'black' : 'bright white'
}
print("Hello World")
color( dict=Dictionary )
# This code wouldn't throw an error since 'bright white' is only values and not in keys of the dictionary.
--------------------------------
Thus repetition of colors is allowed but intermixing of keys and values of a dictionary are not permitted!
===================
ctext()
--------------------------------
'ctext()' is used to change the text and background color of only one line in the python console.
'ctext( String , text = "white" , bg = "black" , delay = 0 , repeat = 1 , dict = {} )' is the function header.
'String' is used to send the required string to be colored.
'text' is used to specify the color of the text.
'bg' is used to specify the color of the background.
===================
The permitted colors are:
1.  Blue
2.  Green
3.  Red
4.  Magenta
5.  Yellow
6.  White
7.  Cyan
8.  Black only for background
None of the arguements are case sensitive. Text color and background color cannot be the same.
===================
> Note:
>     'ctext()' requires two modules namely 'colorama' and 'termcolor' to work.
>     Whenever you run ctext, the presence of these two modules are verified and imported automatically. If absent these two modules are automatically installed via pip. In such a case, good internet connection is recommended. If the installation process fails even in the presence of internet (the program will notify you!), try installing these two modules via pip manually.
===================
Similarities between ctext and color:
Parameters like 'text', 'bg', 'delay', 'repeat' and 'dict' work in a similar manner with slight exceptions which will be discussed later.
===================
Exceptions:
'String' parameter takes a string as an arguement and this line alone is printed with different colors as instructed by text and bg parameters. Passing a string alone to 'ctext()' would be similar to 'print()' statement.
'String' parameter is a mandatory one and should not be omitted
--------------------------------Eg:
ctext("Hello World","Green",'white') # This would affect only this line unlike color()
ctext("Hello World") # This statement is similar to print()
--------------------------------
===================
The permitted colors are different for 'color()' and 'ctext()' and they were already mentioned above
===================
'delay' refers to the time between printing consecutive statements in a list. When a list is passed to text or bg, the 'String' is printed in the respective colors one after the other depending on 'repeat' parameter. The default value of 'delay' is set to 0 units and 'repeat' is set to 1
===================
transTime()
'transTime' is used to find the total time required to complete all color transitions. Only after all the transitions are complete, the code following 'color()' or 'ctext()' will be executed.
'transTime( n , delay , repeat , print = True )' is the function header.
Either the 'number of colors in the list or dictionary' or 'the list and dictionary itself' can be passed to 'n'.
'delay' parameter takes the delay value you are planning to use.
'repeat' parameter takes the delay value you are planning to use.
This function both prints and returns the total transition time. Not using the return value will not throw an error.
'print' is an optional parameter which is set to True by default. If this is changed to False, 'transTime()' would only return a value and not print anything on the console.
--------------------------------Eg:
Dictionary = {
'red'   : 'bright white',
'black' : 'bright white'
}
li = ['red' , 'black']
number_of_elements = 2
transTime(Dictionary,1,3)
transTime(li,1,3)
transTime(number_of_elements,1,3)
# All this will result in the same output "Total time required = 6 units" and return 6
time = transTime(li,1,3,print=False) # This will only return a value and not print anything else
print(time) # This would print "6"
--------------------------------
===================
hackerMan()
This function is added just for fun in case if you wish to look like a hacker amongst your friends.
This would make the text color 'green' and background 'black'.
This takes no arguements. Just add this function at the beginning of your program !
--------------------------------Eg:
hackerMan()
print("ipconfig /flushdns")
print("ping www.google.com")
print("tracert www.google.com")
print("bruteForce -library='n10' someone's_mail@gmail.com")
# All these statements will be printed in green with black background.
--------------------------------
===================
help()
'help()' will provide you the same information in a python console offline
'help( c = True )' is the function header.
If you use 'help()' the text and background will start changing automatically based on a predefined instruction of colors after 30 seconds. If you find it disturbing, you can use 'help(False)' to shut down the color transitions and display instructions in default color.
===================
#             Developed by SAYAD PERVEZ
#             Email-Id : pervez2504@gmail.com
===================



                             $$$$         $$$$
                           $$$$$$$$     $$$$$$$$
                         $$$$$$$$$$$$ $$$$$$$$$$$$
                        $$$$$$$$$$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$$$$$$$$$$$$$$$$$
                         $$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$$$$$$$$
                            $$$$$$$$$$$$$$$$$$$
                               $$$$$$$$$$$$$
                                  $$$$$$$
                                    $$$
                                     $
    ''')
    if(c==True):
        time.sleep(30)
        while(1):
            color(text=__li1__,bg="bright white",repeat=2,delay=1.5)
            color(text="bright white",bg=__li1__,delay=1.5,repeat=2)       # No need to hide

def ctext(String,text="white",bg="black",delay=0,repeat=1,dict={}):
    delay=int(delay)
    repeat=int(repeat)
    String=str(String)
    #If a dictionary is passed.
    if(dict!={}):
        text,bg=__lidict__(dict)
        if((len(dict)!=len(text))&(len(dict)!=len(bg))):
            print("A color in dictionary key cannot be present in the dictionary as a value\nDon't mix keys and values of a dictionary\n:(")

    #both are not lists and hence usual coloring is done !!
    if(type(text)!=type([]))&(type(bg)!=type([])):
        __ctxt__(String,text,bg)

    #both are lists with only one color and hence are equivalent to the first if statement !!!
    elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)==1)&(len(bg)==1):
        __ctxt__(String,text[1],bg[1])

    #both are list but number of elements in both of them are not equal !!!
    elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)!=len(bg)):
        print("Length of the two lists are different !!")
        return


    elif(type(text)==type([]))&(type(bg)!=type([])):
        n=1
        while(1):
            for color in range(len(text)):
                __ctxt__(String,text[color],bg)
                time.sleep(delay)
            if(n>=repeat)&(repeat!=-1):
                break
            n+=1


    elif(type(text)!=type([]))&(type(bg)==type([])):
        n=1
        while(1):
            for color in range(len(bg)):
                __ctxt__(String,text,bg[color])
                time.sleep(delay)
            if(n>=repeat)&(repeat!=-1):
                break
            n+=1

    elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)==len(bg)):
        n=1
        while(1):
            for color in range(len(text)):
                __ctxt__(String,text[color],bg[color])
                time.sleep(delay)
            if(n>=repeat)&(repeat!=-1):
                break
            n+=1


    else:
        try:
            __ctxt__(String,text,bg)
        except Exception as e:
            print(str(e))
            print("""
            Maybe your arguement was not a list, dictionary or a string.
            Try again ;)
            """)       # No need to hide

def transTime(n,delay,repeat,print=True):
    try:
        if((type(n)==type([]))|(type(n)==type({}))):#if list
            n=len(n)
        elif(type(n)==type(1)):
            pass
        else:
            n=int(n)
        ans=n*int(delay)*int(repeat)
        if(ans<0):
            if(print==True):
                ctext("This program will run indefinitely !!","green")
            return("This program will run indefinitely !!")
        else:
            if(print==True):
                ctext("Total time required = {} units".format(ans),"green")
            return(ans)
    except Exception as t:
        print(t)
        print("Invalid_Parameter_Type")
        return("Invalid_Parameter_Type")
        raise TypeError

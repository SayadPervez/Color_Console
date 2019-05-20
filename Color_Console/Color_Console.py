import time
import os
class Color_Console:
    li1=["blue","green","black","purple","blue","red"]
    def cmd(command):
        os.system(command)

    color_dict={
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


    def C(text_color,bg_color):
        if(text_color==bg_color):
            print("Your text color and background color are the same")
            raise AssertionError
        else:
            pass
        try:
            Color_Console.cmd("color {0}{1}".format(Color_Console.color_dict[bg_color.lower()],Color_Console.color_dict[text_color.lower()]))
        except Exception as e:
            print(e)
            print("""
            Its human to err.
            Though I am not a human,
            The person who coded me is.
            Sorry for the bug and I take this back if you were the reason for this exception.
            ;)
            """)

    def color(text,bg,delay=0.67,repeat=-1):

        #both are not lists and hence usual coloring is done !!
        if(type(text)!=type([]))&(type(bg)!=type([])):
            Color_Console.C(text,bg)

        #both are lists with only one color and hence are equivalent to the first if statement !!!
        elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)==1)&(len(bg)==1):
            Color_Console.C(text[1],bg[1])

        #both are list but number of elements in both of them are not equal !!!
        elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)!=len(bg)):
            print("Length of the two lists are different !!")
            return


        elif(type(text)==type([]))&(type(bg)!=type([])):
            n=1
            while(1):
                for color in range(len(text)):
                    Color_Console.C(text[color],bg)
                    time.sleep(delay)
                if(n>=repeat)&(repeat!=-1):
                    break
                n+=1


        elif(type(text)!=type([]))&(type(bg)==type([])):
            n=1
            while(1):
                for color in range(len(bg)):
                    Color_Console.C(text,bg[color])
                    time.sleep(delay)
                if(n>=repeat)&(repeat!=-1):
                    break
                n+=1

        elif(type(text)==type([]))&(type(bg)==type([]))&(len(text)==len(bg)):
            n=1
            while(1):
                for color in range(len(text)):
                    Color_Console.C(text[color],bg[color])
                    time.sleep(delay)
                if(n>=repeat)&(repeat!=-1):
                    break
                n+=1


        else:
            try:
                Color_Console.C(text,bg)
            except Exception as e:
                print(str(e))
                print("""
                Its err to human.
                Though I am not a human,
                The person who coded me is.
                Sorry for the bug and I take this back if you were the reason for this exception.
                ;)
                """)


    def help():
        print('''

        This module is used to colour the whole python console designed for Windows.

        "from Color_Console import color" statement is used to import color function from Color_Console module.

        The permitted colors are:
            black
            blue
            green
            aqua
            red
            purple
            yellow
            white
            gray
            light blue
            light green
            light aqua
            light red
            light purple
            light yellow
            bright white

        None of the arguement are case sensitive. Text color and background color cannot be the same.

        "color ( text , bg , delay , repeat ) "
        color function is used to change the text color and background color of the python console.

        "text" arguement is used to specify the color of the text.
        "bg" arguement is used to specify the color of the background.
        Note that both background color and text color can't be the same.

        If a list of permitted colors is passed to either "text" or "bg", the colors change in accordance to their position in the list.
        "delay" parameter is used to specify the time between two transitions.The default value is set to 0.67 seconds which can be changed.
        "repeat" parameter is used to specify the number of times the list of colors has to be repeated. The default value is -1 which makes the color transition occur indefinitely.
        "delay" and "repeat" are optional parameters.
        Eg:
            color( ['purple','black','red','blue'] , 'white' ) will result in text color changing from purple to black and so on with background color as white.
            color( 'white' , ['purple','black','red','blue'] ) will result in background color changing from purple to black and so on with text color as white.

        When the parameters of both "text" and "bg" are lists, the color transition is as follows:
        Eg:
            color(['green','black','red'],['blue','aqua','bright white'])

        This will result in:
        green text with blue         background
        black text with aqua         background
        red   text with bright white background
        in which the color transition takes 0.67 seconds and this is repeated indefinitely since repeat value is set to a default of -1.
        Note that if the size of two lists are different, an error will be thrown.




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
        time.sleep(30)
        Color_Console.color(text=Color_Console.li1,bg="bright white",repeat=2,delay=1.5)
        Color_Console.color(text="bright white",bg=Color_Console.li1,delay=1.5)

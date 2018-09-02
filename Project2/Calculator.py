# Python program to  create a simple GUI 
# calculator using Tkinter
 
# import everything from tkinter module
import Tkinter  as tk
import Calconfig as cf
import math as mt
from itertools import cycle as cy
# globally declare the expression variable
expression = ""
recall=[]
recl = cy(recall)


def recallfn(exp):
    recall.append(exp)


def press(num):
    global expression
    if num == "=":
        recallfn(expression)
        equalpress()
    elif num == "Clear":
        clear()
    elif num == "sin":
        recallfn(expression)
        expression = str(round(mt.sin((float(expression)/180)*3.14),2))
        equation.set(expression)
        expression = ""
    elif num == "cos":
        recallfn(expression)
        expression = str(round(mt.cos((float(expression) / 180) * 3.14), 2))
        equation.set(expression)
        expression = ""
    elif num == "tan":
        recallfn(expression)
        try:
            expression=str(round(mt.sin((float(expression)/180)*3.14),2)/round(mt.cos((float(expression)/180)*3.14),2))
            equation.set(expression)
            expression = ""
        except:
            expression="math error"
            equation.set(expression)
            expression = ""
    elif num == "Recall":
         try:
            expression=next(recl)
            equation.set(expression)
         except:
            expression="No more recalls"
            equation.set(expression)

    else:
        expression = expression + str(num)
        equation.set(expression)

#    return expression

def equalpress():

    try:

        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set(cf.exprwindow[0])


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = tk.Tk()

    # set the background colour of GUI window
    gui.configure(background=cf.calcwindow[1])
 
    # set the title of GUI window
    gui.title(cf.calcwindow[0])
 
    # set the configuration of GUI window
    gui.geometry(cf.calcwindow[2])
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = tk.StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = tk.Label(gui, textvariable=equation, anchor=cf.exprwindow[1], bg=cf.exprwindow[2], bd=cf.exprwindow[3], height=cf.exprwindow[5], width=cf.exprwindow[4], relief=cf.exprwindow[6], pady=0)
    expression_field.config(font = (cf.exprwindow[7],cf.exprwindow[8]))
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=len(cf.buttonmatrix[0]), ipadx=70, pady=10)
 
    equation.set(cf.exprwindow[0])

    for i in range(0,len(cf.buttonmatrix)):
         for j in range(0,len(cf.buttonmatrix[i])):
                buttonm = tk.Button(gui, text=str(cf.buttonmatrix[i][j]), command = lambda txt=cf.buttonmatrix[i][j]: press(txt), fg=cf.buttondesc[0], bg=cf.buttondesc[1], height=cf.buttondesc[2], width=cf.buttondesc[3])
                buttonm.grid(row=i + 2, column=j)




    # start the GUI
    gui.mainloop()

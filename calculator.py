import tkinter as tk
import math


# CALCULATIONS FUNCTIONS

calculation = ""

def add_to_calculatons(symbol):
    global calculation
    calculation += str(symbol)
    textbox.delete(1.0, "end")
    textbox.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)
    except:
        clear_field()
        textbox.insert(1.0, "error")

def clear_field():
    global calculation
    calculation = ""
    textbox.delete(1.0, "end")


# The GUI

root = tk.Tk()
root.title("Wolfgang's Calculator")
root.geometry("290x310")

# textbox is the display of the calculator
textbox = tk.Text(root, height=5)
textbox.pack(padx=10, pady=20)

# buttonFrame is a frame inside root where we can fill it with buttons in a grid layout.
# So the grid is inside the buttonFrame, and the frame is inside the root.
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1) # weight=1 means it will stretch across the x axis
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonFrame, text="1", command=lambda: add_to_calculatons(1)) # button is nested in buttonFrame
btn1.grid(row=0, column=0, sticky=tk.W + tk.E) # .grid() takes rows and columns as parameters and starts from o

btn2 = tk.Button(buttonFrame, text="2", command=lambda: add_to_calculatons(2))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E) # sticky means it will try to stick to the left (West) or right (East)

btn3 = tk.Button(buttonFrame, text="3", command=lambda: add_to_calculatons(3))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonFrame, text="4", command=lambda: add_to_calculatons(4))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonFrame, text="5", command=lambda: add_to_calculatons(5))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonFrame, text="6", command=lambda: add_to_calculatons(6))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

btn7 = tk.Button(buttonFrame, text="7", command=lambda: add_to_calculatons(7))
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

btn8 = tk.Button(buttonFrame, text="8", command=lambda: add_to_calculatons(8))
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

btn9 = tk.Button(buttonFrame, text="9", command=lambda: add_to_calculatons(9))
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

btnopen = tk.Button(buttonFrame, text="(", command=lambda: add_to_calculatons("("))
btnopen.grid(row=4, column=0, sticky=tk.W + tk.E)

btnclose = tk.Button(buttonFrame, text=")", command=lambda: add_to_calculatons(")"))
btnclose.grid(row=4, column=2, sticky=tk.W + tk.E)

btn0 = tk.Button(buttonFrame, text="0", command=lambda: add_to_calculatons(0))
btn0.grid(row=3, column=1, sticky=tk.W + tk.E)

btndiv = tk.Button(buttonFrame, text="/", command=lambda: add_to_calculatons("/"))
btndiv.grid(row=0, column=3, sticky=tk.W + tk.E)

btnmal = tk.Button(buttonFrame, text="*", command=lambda: add_to_calculatons("*"))
btnmal.grid(row=1, column=3, sticky=tk.W + tk.E)

btnminus = tk.Button(buttonFrame, text="-", command=lambda: add_to_calculatons("-"))
btnminus.grid(row=2, column=3, sticky=tk.W + tk.E)

btnplus = tk.Button(buttonFrame, text="+", command=lambda: add_to_calculatons("+"))
btnplus.grid(row=3, column=3, sticky=tk.W + tk.E)

btnequals = tk.Button(buttonFrame, text="=", command=evaluate_calculation)
btnequals.grid(row=4, column=3, sticky=tk.W + tk.E, columnspan="2")

btnclear = tk.Button(buttonFrame, text="C", command=clear_field)
btnclear.grid(row=4, column=1, sticky=tk.W + tk.E)

buttonFrame.pack(fill="x", padx=10, pady=5) # Displays the buttonFrame in pack(). fill=x means it will fill the x-axis





root.mainloop()
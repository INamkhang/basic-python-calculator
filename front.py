from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

def change_text(number):
    label1.insert(tk.END, number)

def equal():
    try:
        y = str(eval(label1.get()))
        label1.delete(0, tk.END)
        label1.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")  

def clear():
    label1.delete(0, tk.END)


window = Tk()
window.title("Python Calculator")
window.geometry("326x300")
window.configure(bg='#252A2D')


label1=tk.Entry(window, text= " ",width=45,bg='#252A2D',fg='white',highlightthickness=2, highlightbackground='white',borderwidth=3)
label1.grid(row=0, column=0,columnspan=4)
label2=Label(window, text= "Input Your Number",width=45,height=1,bg='#252A2D',fg='white')
label2.grid(row=1, column=0,columnspan=4)



#Create a button widget number
button1= tk.Button(window, text="1",bg='#252A2D',fg='white', width=10,command=lambda:change_text(1))
button1.grid(row=4, column=0,pady=1, ipady=10)

button2= tk.Button(window, text="2",bg='#252A2D',fg='white', width=10,command=lambda:change_text(2))
button2.grid(row=4, column=1,pady=1, ipady=10)

button3= tk.Button(window, text="3",bg='#252A2D',fg='white', width=10,command=lambda:change_text(3))
button3.grid(row=4, column=2,pady=1, ipady=10)

button4= tk.Button(window, text="4",bg='#252A2D',fg='white', width=10,command=lambda:change_text(4))
button4.grid(row=3, column=0,pady=1, ipady=10)

button5= tk.Button(window, text="5",bg='#252A2D',fg='white', width=10,command=lambda:change_text(5))
button5.grid(row=3, column=1,pady=1, ipady=10)

button6= tk.Button(window, text="6",bg='#252A2D',fg='white', width=10,command=lambda:change_text(6))
button6.grid(row=3, column=2,pady=1, ipady=10)

button7= tk.Button(window, text="7",bg='#252A2D',fg='white', width=10,command=lambda:change_text(7))
button7.grid(row=2, column=0,pady=1, ipady=10)

button8= tk.Button(window, text="8",bg='#252A2D',fg='white', width=10,command=lambda:change_text(8))
button8.grid(row=2, column=1,pady=1, ipady=10)

button9= tk.Button(window, text="9",bg='#252A2D',fg='white', width=10,command=lambda:change_text(9))
button9.grid(row=2, column=2,pady=1, ipady=10)

button0= tk.Button(window, text="0",bg='#252A2D',fg='white', width=10,command=lambda:change_text(0))
button0.grid(row=5, column=1,pady=1, ipady=10)

#Create a button widget symbol
buttonPlus= tk.Button(window, text="+",bg='#252A2D',fg='white', width=10,command=lambda:change_text("+"))
buttonPlus.grid(row=2, column=3,pady=1, ipady=10)

buttonminus= tk.Button(window, text="-",bg='#252A2D',fg='white', width=10,command=lambda:change_text("-"))
buttonminus.grid(row=3, column=3,pady=1, ipady=10)

buttonmulti= tk.Button(window, text="x",bg='#252A2D',fg='white', width=10,command=lambda:change_text("x"))
buttonmulti.grid(row=4, column=3,pady=1, ipady=10)

buttonhan= tk.Button(window, text="/",bg='#252A2D',fg='white', width=10,command=lambda:change_text("/"))
buttonhan.grid(row=5, column=3,pady=1, ipady=10)

buttonhan= tk.Button(window, text="=",bg='#252A2D',fg='white', width=30,command=lambda:equal())
buttonhan.grid(row=6, column=0,pady=1,columnspan=3, ipady=10)

buttonhan= tk.Button(window, text="clr",bg='#252A2D',fg='white', width=10,command=lambda:clear())
buttonhan.grid(row=6, column=3,pady=1, ipady=10)


window.mainloop()